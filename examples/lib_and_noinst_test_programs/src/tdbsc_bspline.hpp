//
// Copyright 2013 Timothy John Giese
//
#ifndef _twdbsc_bspline_hpp_
#define _twdbsc_bspline_hpp_

void periodic_bspline_spread
( double const x, int const order, 
  double const rngx, int const nx, 
  int * gidx, 
  double * wx, 
  double * dx );

void aperiodic_bspline_spread
( double const x, int const order, 
  double const rngx, int const nx, 
  int * gidx, 
  double * wx, 
  double * dx );

void bspline_eval
( double const w, int const order, double * array );

void bspline_eval
( double const w, int const order, double * array, double * darray );

#endif

