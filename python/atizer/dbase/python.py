#!/usr/bin/env python


from ..base import *
from ..m4 import *


class python_devel(autolib):
    def __init__(self,version="2.6"):
        super( python_devel , self ).__init__( "python_devel" )
        self.serial.var = "PYTHON_EXTRA_LIBS"
        self.serial.name = "python_devel"
        self.serial.cppflags = "$(PYTHON_CPPFLAGS)"
        self.serial.ldflags = "$(PYTHON_LDFLAGS) $(PYTHON_EXTRA_LDFLAGS)"
        self.openmp = self.serial
        self.mpi = self.serial
        self.required_version = ">= '"+version+"'"

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ax_python_devel.m4") )
        fh.write("""
AC_PYTHON_DEVEL([%s])
"""%(self.required_version))

