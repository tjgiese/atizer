//
// Copyright 2013 Timothy John Giese
//
#ifndef _tdbsc_dihed_hpp_
#define _tdbsc_dihed_hpp_

double dihedral_angle
( double const * I, double const * J, 
  double const * K, double const * L, 
  bool & linear );

double dihedral_angle
( double const * I, double const * J, 
  double const * K, double const * L, 
  bool & linear, 
  double * dddI, double * dddJ, 
  double * dddK, double * dddL );

#endif

