//
// Copyright 2013 Timothy John Giese
//
#include "pucker.hpp"
#include <vector>
#include <tr1/array>
#include <iostream>
#include <fstream>
#include <iomanip>

std::vector<double> read_xyz( char const * fname );

int main()
{
  std::vector<double> crd( read_xyz("ade.xyz") );
  int const nat = crd.size()/3;
  std::vector<double> grd(3*nat,0.);

  pucker p( "ade.2dbspl" );
  p.push_back( dihed(0,1,2,3), dihed(2,3,4,5) );

  double E = p.eval( crd.data(), grd.data() );

  std::cout.precision(4);
  std::cout.setf( std::ios::scientific, std::ios::floatfield );
  std::cout << "E = " << std::setw(12) << E << "\n";
  for ( int i=0; i<nat; ++i )
    {
      for ( int k=0; k<3; ++k )
	std::cout << std::setw(12) << grd[k+i*3];
      std::cout << "\n";
    };

  return 0;
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
