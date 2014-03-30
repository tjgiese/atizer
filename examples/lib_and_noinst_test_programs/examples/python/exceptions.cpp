//
// Copyright 2013 Timothy John Giese
//
#include "exceptions.hpp"


PyObject * python_exception = 0;

PyObject* createExceptionClass(const char* name, PyObject* baseTypeObj)
{
    using std::string;
    namespace bp = boost::python;

    string scopeName = bp::extract<string>(bp::scope().attr("__name__"));
    string qualifiedName0 = scopeName + "." + name;
    char* qualifiedName1 = const_cast<char*>(qualifiedName0.c_str());

    PyObject* typeObj = PyErr_NewException(qualifiedName1, baseTypeObj, 0);
    if(!typeObj) bp::throw_error_already_set();
    bp::scope().attr(name) = bp::handle<>(bp::borrowed(typeObj));
    return typeObj;
}

void raise_exception( std::string msg )
{
  PyErr_SetString( python_exception, msg.c_str() );
  boost::python::throw_error_already_set();
}
