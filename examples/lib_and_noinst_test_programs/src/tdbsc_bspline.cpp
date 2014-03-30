//
// Copyright 2013 Timothy John Giese
//
#include "tdbsc_bspline.hpp"
#include <cassert>
#include <cmath>


void one_pass_bspline( double * c, double const w, int const n )
{
  int nm1 = n-1;
  double const div = 1. / nm1;
  c[nm1] = div * w * c[nm1 - 1];  
  for ( int j=1; j<nm1; ++j )
    c[nm1 - j] = div * ((w + j) * c[nm1 - j - 1] + (n - j - w) * c[nm1 - j]);
  c[0] = div * (1 - w) * c[0];
}


void diff_bspline( int const order, double const * array, double * diff )
{
  assert( order > 1 );
  int const nm1 = order-1;
  diff[0] = -array[0];
  for ( int j=1; j<nm1; ++j )
    diff[j] = array[j-1] - array[j];
  diff[nm1] = array[nm1-1];
}



void bspline_eval
( double const w, int const order, double * array )
{
  array[0] = 1. - w;
  array[1] = w;

  if (order > 2)
    {
      // One pass to order 3:
      array[2] = 0.5 * w * array[1];
      array[1] = 0.5 * ((w + 1.) * array[0] + (2. - w) * array[1]);
      array[0] = 0.5 * (1. - w) * array[0];
      
      if (order > 3)
        {
          // One pass to order 4:         
          double const div = 1./3.;
          array[3] = div * w * array[2];
          array[2] = div * ((w + 1.) * array[1] + (3. - w) * array[2]);
          array[1] = div * ((w + 2.) * array[0] + (2. - w) * array[1]);
          array[0] = div * (1. - w) * array[0];

          // and the rest
          for ( int k = 5; k <= order; ++k )
            one_pass_bspline(array, w, k);
        };
    };
}



void bspline_eval
( double const w, int const order, double * array, double * darray )
{
  assert( order > 2 );
  double const div = 1./3.;

  array[0] = 1. - w;
  array[1] = w;

  if (order == 4)
    {
      // One pass to order 3:
      array[2] = 0.5 * w * array[1];
      array[1] = 0.5 * ((w + 1.) * array[0] + (2. - w) * array[1]);
      array[0] = 0.5 * (1. - w) * array[0];
      
      darray[0] = -array[0];
      darray[1] = array[0]-array[1];
      darray[2] = array[1]-array[2];
      darray[3] = array[2];

      // One pass to order 4:     
      array[3] = div * w * array[2];
      array[2] = div * ((w + 1.) * array[1] + (3. - w) * array[2]);
      array[1] = div * ((w + 2.) * array[0] + (2. - w) * array[1]);
      array[0] = div * (1. - w) * array[0];
      
    }
  else if ( order > 4 )
    {
      array[2] = 0.5 * w * array[1];
      array[1] = 0.5 * ((w + 1.) * array[0] + (2. - w) * array[1]);
      array[0] = 0.5 * (1. - w) * array[0];

      array[3] = div * w * array[2];
      array[2] = div * ((w + 1.) * array[1] + (3. - w) * array[2]);
      array[1] = div * ((w + 2.) * array[0] + (2. - w) * array[1]);
      array[0] = div * (1. - w) * array[0];

      // and the rest
      for ( int k = 5; k < order; ++k ) // don't do k==order
        one_pass_bspline(array, w, k);

      diff_bspline(order,array,darray);

      // One more recursion: // do the k==order
      one_pass_bspline(array, w, order);

    }
  else // order == 3
    {
      darray[0] = -array[0];
      darray[1] = array[0]-array[1];
      darray[2] = array[1];

      // One pass to order 3:
      array[2] = 0.5 * w * array[1];
      array[1] = 0.5 * ((w + 1.) * array[0] + (2. - w) * array[1]);
      array[0] = 0.5 * (1. - w) * array[0];
    };
}





void periodic_bspline_spread
( double const x, 
  int const bsplineOrder,
  double const lengthx, 
  int const nx,
  int * gidx,
  double * wts,
  double * dwts )
{
  //gidx.resize(bsplineOrder);
  //wts.resize(bsplineOrder);
  //dwts.resize(bsplineOrder);

  double const oonx = 1./nx;
  double const del = lengthx*oonx;

  int ilo;
  double bsplq;
  // ilo is the index below our point
  // bsplq is the bspline coordinate through that point
  if ( bsplineOrder % 2 == 0 )
    {
      ilo = std::floor( x/del )+1;
      bsplq = (x-(ilo-1)*del)/del;
    }
  else
    {
      ilo = std::floor( x/del + 0.5 );
      bsplq = (x-(ilo-0.5)*del)/del;
    };
  // ioff is the left-most point of the bspline
  // fill an array of wrapped global indices
  int ioff = ilo-bsplineOrder/2;
  for ( int b=0; b<bsplineOrder; ++b )
    {
      // this is the index of the bspline point
      int idx = ioff + b;
      // wrap this index into the range of data
      gidx[b] = idx - nx * static_cast<int>( std::floor( idx*oonx ) );
    };
  //printf("         %12.4f\n",bsplq);
  bspline_eval( bsplq, bsplineOrder, wts, dwts );
  for ( int i=0; i<bsplineOrder; ++i )
    dwts[i] /= del;
}



void aperiodic_bspline_spread
( double const x, 
  int const bsplineOrder,
  double const lengthx, 
  int const nx,
  int * gidx,
  double * wts,
  double * dwts )
{
  //gidx.resize(bsplineOrder);
  //wts.resize(bsplineOrder);
  //dwts.resize(bsplineOrder);

  double const oonx = 1./nx;
  double const del = lengthx*oonx;

  int ilo;
  double bsplq;
  // ilo is the index below our point
  // bsplq is the bspline coordinate through that point
  if ( bsplineOrder % 2 == 0 )
    {
      ilo = std::floor( x/del )+1;
      bsplq = (x-(ilo-1)*del)/del;
    }
  else
    {
      ilo = std::floor( x/del + 0.5 );
      bsplq = (x-(ilo-0.5)*del)/del;
    };
  //printf("         %12.4f\n",bsplq);
  bspline_eval( bsplq, bsplineOrder, wts, dwts );
  for ( int i=0; i<bsplineOrder; ++i )
    dwts[i] /= del;
  // ioff is the left-most point of the bspline
  // fill an array of wrapped global indices
  int ioff = ilo-bsplineOrder/2;
  for ( int b=0; b<bsplineOrder; ++b )
    {
      // this is the index of the bspline point
      int idx = ioff + b;
      if ( idx < 0 or idx >= nx )
	{
	  wts[b] = 0.;
	  dwts[b] = 0.;
	};
      // wrap this index into the range of data
      gidx[b] = idx - nx * static_cast<int>( std::floor( idx*oonx ) );
    };
}






