#include "test1.hpp"
#include <iostream>
#include <boost/array.hpp>
#include <boost/python.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>

void test1fcn()
{
  boost::array<double,3> a;
  a[0] = 1.;
  std::cout << "test1 " << a[0] << "\n";
}




BOOST_PYTHON_MODULE_INIT(test1)
{
  boost::python::def("test1fcn",&test1fcn,
		     "a dummy function that prints to stdout" );
}

