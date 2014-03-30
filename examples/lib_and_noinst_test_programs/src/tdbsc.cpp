//
// Copyright 2013 Timothy John Giese
//
#include "tdbsc.hpp"
#include "tdbsc_fft.hpp"
#include "tdbsc_bspline.hpp"
#include "tdbsc_dihed.hpp"

#include <fstream>
#include <sstream>
#include <iostream>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <tr1/memory>

std::tr1::shared_ptr<std::ifstream> tdbsc_readheader
( char const * filename,
  int * order, 
  int * dimsize_2,
  double * minmax_2x2,
  bool * periodicity_2 )
{

  std::tr1::shared_ptr<std::ifstream> cin( new std::ifstream() );
  cin->open( filename );

  if ( ! cin->good() )
    {
      std::cerr << "tdbsc_readheader : "
		<< "Could not open '" << filename << "'";
      abort();
    };

  int dim;
  *cin >> dim >> *order;

  if ( dim != 2 )
    {
      std::cerr << "tdbsc_readheader : Excepted 2-d data, " 
		<< "but '" << filename << "' supplies dim=" << dim;
      abort();
    };

  if ( *order < 2 or *order > 10 )
    {
      std::cerr << "tdbsc_readheader : received nonsensical "
		<< "bspline order: '" << order 
		<< "'; expected range [2,10]";
      abort();
    };

  for ( int i=0; i<2; ++i )
    *cin >> dimsize_2[i] 
	 >> minmax_2x2[0+i*2] >> minmax_2x2[1+i*2] 
	 >> periodicity_2[i];

  return cin;
}



int tdbsc_readdatasize_
( char const * filename )
{
  int order[1], dimsize[2];
  double minmax[4];
  bool periodicity[2];
  tdbsc_readheader(filename,order,dimsize,minmax,periodicity);
  return dimsize[0]*dimsize[1];
}



void tdbsc_readdata_
( char const * filename,
  int * order, 
  int * dimsize,
  double * minmax,
  bool * periodicity,
  double * data )
{
  std::tr1::shared_ptr<std::ifstream> cin
    ( tdbsc_readheader
      (filename,order,dimsize,minmax,periodicity) );

  for ( int i=0; i<dimsize[0]; ++i )
    for ( int j=0; j<dimsize[1]; ++j )
      *cin >> data[j+i*dimsize[1]];

  tdbsc_renormalize(*order,dimsize,minmax,data);
}


double tdbsc_cptvalue_
( double const * q,
  double * grd,
  int const * order, 
  int const * dimsize, 
  double const * minmax,
  bool const * periodicity,
  double const * data )
{
  double val = 0.;
  grd[0] = 0.;
  grd[1] = 0.;

  std::vector<int> gidx(*order),gidy(*order);
  std::vector<double> wx(*order),wy(*order),dx(*order),dy(*order);
  int nx = dimsize[0];
  int ny = dimsize[1];
  double minx = minmax[0];
  double miny = minmax[2];
  double rngx = minmax[1]-minx;
  double rngy = minmax[3]-miny;
  double x=q[0];
  double y=q[1];

  if ( periodicity[0] )
    {
      periodic_bspline_spread
	( x+minx, *order, rngx, nx, gidx.data(), wx.data(), dx.data() );
    }
  else
    {
      aperiodic_bspline_spread
	( x+minx, *order, rngx, nx, gidx.data(), wx.data(), dx.data() );
    };
  if ( periodicity[1] )
    {
      periodic_bspline_spread
	( y+miny, *order, rngy, ny, gidy.data(), wy.data(), dy.data() );
    }
  else
    {
      aperiodic_bspline_spread
	( y+miny, *order, rngy, ny, gidy.data(), wy.data(), dy.data() );
    };
  for ( int i=0; i<*order; ++i )
    for ( int j=0; j<*order; ++j )
      {
        double d = data[ gidy[j] + gidx[i]*ny ];
        val    += wx[i] * wy[j] * d;
        grd[0] += dx[i] * wy[j] * d;
        grd[1] += wx[i] * dy[j] * d;
      };
  return val;
}


double tdbsc_pucker_
( double const * x3n,
  double * g3n,
  int const * a1, int const * a2, int const * a3, int const * a4,
  int const * b1, int const * b2, int const * b3, int const * b4,
  int const * order, 
  int const * dimsize, 
  double const * minmax,
  bool const * periodicity,
  double const * data )
{
  double q[2] = {0.,0.};
  double dEdq[2] = {0.,0.};
  bool linear = false;

  double ga1[3] = {0.,0.,0.};
  double ga2[3] = {0.,0.,0.};
  double ga3[3] = {0.,0.,0.};
  double ga4[3] = {0.,0.,0.};
  double gb1[3] = {0.,0.,0.};
  double gb2[3] = {0.,0.,0.};
  double gb3[3] = {0.,0.,0.};
  double gb4[3] = {0.,0.,0.};

  q[0] = dihedral_angle
    ( x3n+3**a1, 
      x3n+3**a2, 
      x3n+3**a3, 
      x3n+3**a4,
      linear,ga1,ga2,ga3,ga4);

  if ( linear ) return 0.;

  q[1] = dihedral_angle
    ( x3n+3**b1, 
      x3n+3**b2, 
      x3n+3**b3, 
      x3n+3**b4,
      linear,gb1,gb2,gb3,gb4);

  if ( linear ) return 0.;

  double E = tdbsc_cptvalue_
    (q,dEdq, order,dimsize,minmax,periodicity,data);

  for ( int k=0; k<3; ++k )
    {
      g3n[k+*a1*3] += ga1[k] * dEdq[0];
      g3n[k+*a2*3] += ga2[k] * dEdq[0];
      g3n[k+*a3*3] += ga3[k] * dEdq[0];
      g3n[k+*a4*3] += ga4[k] * dEdq[0];
    };
  for ( int k=0; k<3; ++k )
    {
      g3n[k+*b1*3] += gb1[k] * dEdq[1];
      g3n[k+*b2*3] += gb2[k] * dEdq[1];
      g3n[k+*b3*3] += gb3[k] * dEdq[1];
      g3n[k+*b4*3] += gb4[k] * dEdq[1];
    };
  return E;
}
