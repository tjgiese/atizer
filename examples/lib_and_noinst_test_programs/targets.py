#!/usr/bin/env python

from atizer import *
from atizer.dbase import *

class tdbsc(autolib):
    def __init__(self,basedir=None):
        super(tdbsc,self).__init__( "tdbsc", basedir )
        self.copyright_holder = "Timothy J. Giese"
        self.license = licenses.MIT
        self.libs = [ fftw3() ]

    def ac_subst_var_serial(self,fh):
        m4_generic_cxx_serial_conftest(
            self,fh,
            # header
            "tdbsc/tdbsc.hpp",
            # preamble
            """#include <tdbsc/tdbsc.hpp>""", 
            # body
            """int n = tdbsc_readdatasize_("filename");""") 

