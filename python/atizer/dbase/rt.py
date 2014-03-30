#!/usr/bin/env python

from ..base import *
from ..m4 import *


class rt(autolib):
    def __init__(self,basedir=None):
        super( rt , self ).__init__( "rt", basedir )
        self.enable_openmp()
        self.openmp.var = "RT_OPENMP_LIBS"
        self.openmp.var_default_value = ""

    def ac_subst_var_serial(self,fh):
        m4_generic_cxx_serial_conftest(
            self,fh,
            "time.h", # header
            """#include <time.h>""", # preamble
            """
timespec t;
int n = clock_gettime(CLOCK_PROCESS_CPUTIME_ID,&t);
""") # body

    def ac_subst_var_openmp(self,fh):
        fh.write( m4_define_new_env(self.openmp.var,self.openmp.var_default_value,"real-time library for timings") )
        fh.write("AC_SUBST("+self.openmp.var+")\n")



