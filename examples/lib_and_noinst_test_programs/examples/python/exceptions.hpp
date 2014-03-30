//
// Copyright 2013 Timothy John Giese
//
#ifndef _exceptions_hpp_
#define _exceptions_hpp_

#include <boost/python.hpp>
#include <string>

extern PyObject * python_exception;

PyObject* createExceptionClass
( char const * name, 
  PyObject * baseTypeObj = PyExc_Exception);

void raise_exception( std::string msg );

#endif
