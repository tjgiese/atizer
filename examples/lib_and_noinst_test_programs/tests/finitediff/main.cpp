//
// Copyright 2013 Timothy John Giese
//
#include "../../src/tdbsc.hpp"
#include <vector>
#include <tr1/array>
#include <iostream>
#include <fstream>
#include <iomanip>

struct dihed
{
  dihed(int a,int b,int c,int d) : a(a),b(b),c(c),d(d) {};
  int a,b,c,d;
};


class pucker
{
public:
  pucker( char const * fname );
  double eval( double const * x, double * g );
  void push_back( dihed a, dihed b );

private:
  std::vector< std::tr1::array<dihed,2> > torsion;
  int order;
  std::tr1::array<int,2> dimsize;
  std::tr1::array<double,4> minmax;
  std::tr1::array<bool,2> periodic;
  std::vector<double> data;
};


inline pucker::pucker( char const * fname )
{
  int ndata = tdbsc_readdatasize_(fname);
  data.resize(ndata);
  tdbsc_readdata_(fname,&order,
		  dimsize.data(),minmax.data(),
		  periodic.data(),data.data());
}


inline double pucker::eval( double const * x, double * g )
{
  double E = 0.;
  int const n = torsion.size();
  for ( int i=0; i<n; ++i )
    E += tdbsc_pucker_
      ( x,g,
	&torsion[i][0].a, &torsion[i][0].b, 
	&torsion[i][0].c, &torsion[i][0].d,
	&torsion[i][1].a, &torsion[i][1].b, 
	&torsion[i][1].c, &torsion[i][1].d,
	&order, 
	dimsize.data(), minmax.data(), 
	periodic.data(), data.data() );
  return E;
}


inline void pucker::push_back( dihed a, dihed b )
{
  std::tr1::array<dihed,2> ab = {{ a,b }};
  torsion.push_back(ab);
}


std::vector<double> read_xyz( char const * fname )
{
  std::ifstream cin;
  cin.open( fname );
  int nat;
  std::string s;
  cin >> nat;
  cin >> s;
  std::vector<double> crd(3*nat,0.);
  for ( int i=0; i<nat; ++i )
    cin >> s >> crd[0+i*3] >> crd[1+i*3] >> crd[2+i*3];
  for ( int i=0; i<3*nat; ++i )
    crd[i] *= 1.88972613373440e+00;

  return crd;
}


int main()
{
  std::vector<double> crd( read_xyz("ade.xyz") );
  int const nat = crd.size()/3;
  std::vector<double> anagrd(3*nat,0.);
  std::vector<double> numgrd(3*nat,0.);


  pucker p( "ade.2dbspl" );
  p.push_back( dihed(0,1,2,3), dihed(2,3,4,5) );

  // 
  // finite difference calculation
  //
  double const DEL = 1.e-5;
  for ( int i=0; i<nat; ++i )
    for ( int k=0; k<3; ++k )
      {
	crd[k+i*3] += DEL;
	double Ehi = p.eval( crd.data(), anagrd.data() );
	crd[k+i*3] -= 2*DEL;
	double Elo = p.eval( crd.data(), anagrd.data() );
	crd[k+i*3] += DEL;
	numgrd[k+i*3] = 0.5 * (Ehi-Elo) / DEL;
      };

  //
  // analytic calculation
  //
  for ( int i=0; i<3*nat; ++i )
    anagrd[i] = 0.;
  double E = p.eval( crd.data(), anagrd.data() );


  //
  // compare analytic and numerical results
  //
  std::cout.precision(4);
  std::cout.setf( std::ios::scientific, std::ios::floatfield );
  std::cout << "E = " << std::setw(12) << E << "\n";
  for ( int i=0; i<nat; ++i )
    {
      for ( int k=0; k<3; ++k )
	std::cout << std::setw(12) << anagrd[k+i*3];
      for ( int k=0; k<3; ++k )
	std::cout << std::setw(12) << numgrd[k+i*3];
      for ( int k=0; k<3; ++k )
	std::cout << std::setw(12) << anagrd[k+i*3]-numgrd[k+i*3];
      std::cout << "\n";
    };

  return 0;
}

