//
// Copyright 2013 Timothy John Giese
//
#include "pucker.hpp"
#include "exceptions.hpp"
#include <iostream>
#include <vector>
#include <tr1/array>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>

double (pucker::*pyeval)
( boost::python::list const & x, boost::python::list & g ) 
= &pucker::eval;

void (pucker::*pypush_back)
( int const a1, int const b1, int const c1, int const d1,
  int const a2, int const b2, int const c2, int const d2 ) 
= &pucker::push_back;


BOOST_PYTHON_MODULE_INIT(pytdbsc)
{

  python_exception = createExceptionClass("exception");

  boost::python::class_< pucker >
    ( "pucker", 
      "documentation\n",
      //
      boost::python::init<boost::python::str>
      ( boost::python::args("self","filename"), 
	"description") )
    //
    .def("eval",pyeval,
         boost::python::args("self","crd","grd"),
         "description")
    //
    .def("push_back",pypush_back,
         boost::python::args("self",
			     "a1","b1","c1","d1",
			     "a2","b2","c2","d2"),
         "description");

}



