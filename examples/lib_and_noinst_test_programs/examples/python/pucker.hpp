//
// Copyright 2013 Timothy John Giese
//
#ifndef _pucker_hpp_
#define _pucker_hpp_

#include <tdbsc/tdbsc.hpp>
#include <boost/python.hpp>

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

  pucker( boost::python::str fname );

  double eval( boost::python::list const & x, boost::python::list & g );
  void push_back( int const a1, int const b1, 
		  int const c1, int const d1, 
		  int const a2, int const b2,
		  int const c2, int const d2 );



private:
  std::vector< std::tr1::array<dihed,2> > torsion;
  int order;
  std::tr1::array<int,2> dimsize;
  std::tr1::array<double,4> minmax;
  std::tr1::array<bool,2> periodic;
  std::vector<double> data;
};


#endif
