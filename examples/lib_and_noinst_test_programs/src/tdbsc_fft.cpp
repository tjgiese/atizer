//
// Copyright 2013 Timothy John Giese
//

#include "tdbsc_fft.hpp"
#include "tdbsc_bspline.hpp"

#include <vector>
#include <complex>
#include <cmath>
#include <fftw3.h>

double const TWO_PI = 2. * 3.141592653589793238462643383279502884197;

////////////////////////////////////////////////////////////////////
// discrete cosine expansion; computes the fourier coefficients
// of an even function positioned according to the fftw3 conventions
////////////////////////////////////////////////////////////////////
void bspline_dct
( int const N, int const order, double const * in, double * out )
{
  for ( int i=0; i<N; ++i ) out[i] = 0.;
  
  int const o = (order-1)/2;
  int const Np = (order)/2+1;
  int const Nh = N-o;
  
  double const tpion = TWO_PI/N;
  for ( int m=0; m<N; ++m )
    {
      double const k = m * tpion;
      for ( int n=0; n<Np; ++n )
        out[m] += in[n+o] * std::cos(k*n);
      for ( int i=0; i<o; ++i )
        out[m] += in[i] * std::cos(k*(Nh+i));
    };
}

////////////////////////////////////////////////////////////////////
// discrete cosine expansion; computes the fourier coefficients
// of an even function positioned according to the fftw3 conventions
// This version computes only half of the spectrum on account
// of the symmetry of the complex numbers in the fast-loop
////////////////////////////////////////////////////////////////////
void bspline_hdct
( int const N, int const order, double const * in, double * out )
{
  for ( int i=0; i<N/2+1; ++i ) out[i] = 0.;
  
  int const Nmax = N/2+1;
  int const o = (order-1)/2;
  int const Np = (order)/2+1;
  int const Nh = N-o;
  
  double const tpion = TWO_PI/N;
  for ( int m=0; m<Nmax; ++m )
    {
      double const k = m * tpion;
      for ( int n=0; n<Np; ++n )
        out[m] += in[n+o] * std::cos(k*n);
      for ( int i=0; i<o; ++i )
        out[m] += in[i] * std::cos(k*(Nh+i));
    };
}


////////////////////////////////////////////////////////////////////
// Computes the fourier transform of a b-spline
////////////////////////////////////////////////////////////////////
void bspline_fourier_coef_full
( int const N, int const order, double * fc )
{
  std::vector<double> wts( order, 0. );
  bspline_eval( ( order%2 == 0 ? 0.0 : 0.5 ), order, wts.data() );
  bspline_dct( N, order, wts.data(), fc );
}

////////////////////////////////////////////////////////////////////
// Computes the fourier transform of a b-spline
// This version only computes half of the fourier spectrum on
// account of the complex number symmetry within the fast loop
////////////////////////////////////////////////////////////////////
void bspline_fourier_coef_half
( int const N, int const order, double * fc )
{
  std::vector<double> wts( order, 0. );
  bspline_eval( ( order%2 == 0 ? 0.0 : 0.5 ), order, wts.data() );
  bspline_hdct( N, order, wts.data(), fc );
}


///////////////////////////////////////////////////////////////////
// renormalizes a uniform grid of data so that b-spline
// interpolation exactly passes through the data
///////////////////////////////////////////////////////////////////
void tdbsc_renormalize
( int const order, 
  int const * dimsize,
  double const * minmax,
  double * data )
{
  int const nx       = dimsize[0];
  int const ny       = dimsize[1];
  int const n        = nx*ny;
  int const nyf      = ny/2+1;
  int const nfourier = nx*nyf;
  
  //
  // allocate fft data and plans
  //
  double * value = fftw_alloc_real( n );

  std::complex<double> * fourier 
    = reinterpret_cast< std::complex<double> * >
    ( fftw_alloc_complex( nfourier ) );

  fftw_plan * fplan = new fftw_plan
    ( fftw_plan_dft_r2c_2d
      ( nx, ny, 
	value, 
	reinterpret_cast< fftw_complex *>( fourier ), 
	FFTW_ESTIMATE ) );

  fftw_plan * rplan = new fftw_plan
    ( fftw_plan_dft_c2r_2d
      ( nx, ny, 
	reinterpret_cast< fftw_complex *>( fourier ), 
	value, 
	FFTW_ESTIMATE ) );

  //
  // forward fft of data
  //
  for ( int i=0; i<n; ++i )
    value[i] = data[i];
  fftw_execute( *fplan );
  double const dx = minmax[1]-minmax[0];
  double const dy = minmax[3]-minmax[2];
  double const volElement = dx*dy/n;
  for ( int i=0; i<nfourier; ++i )
    fourier[i] *= volElement;
  //
  // forward fft of b-splines
  //
  std::vector<double> fx( dimsize[0] ), fy( dimsize[1] );
  bspline_fourier_coef_full( dimsize[0], order, fx.data() );
  bspline_fourier_coef_half( dimsize[1], order, fy.data() );
  //
  // scale the fourier coefs
  //
  int ij=0;
  for ( int i=0; i < nx; ++i )
    for ( int j=0; j < nyf; ++j, ++ij )
      fourier[ij] /= ( fx[i] * fx[j] );
  //
  // reverse fft
  //
  fftw_execute( *rplan ); 
  double const ooV = 1./(dx*dy);
  for ( int i=0; i<n; ++i )
    data[i] = ooV * value[i];
  //
  // delete
  //
  fftw_destroy_plan( *fplan );
  delete fplan;
  fplan = NULL;
  fftw_destroy_plan( *rplan );
  delete rplan;
  rplan = NULL;
  fftw_free(reinterpret_cast< fftw_complex * &>(fourier));
  fourier = NULL;
  fftw_free( value );
  value = NULL;
}

