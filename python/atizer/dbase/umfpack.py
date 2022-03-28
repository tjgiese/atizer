from ..base import *
from ..m4 import *
import copy
class umfpack(autolib):
    def __init__(self,optional=False):
        super( umfpack , self ).__init__( "umfpack" )
        self.optional = optional
        self.serial.var = "UMFPACK_LIBS"
        self.serial.var_default_value = "-lumfpack -lamd"
        self.serial.name = "umfpack"
        self.serial.cppflags = ""
        self.serial.ldflags = ""
        self.openmp = self.serial
        self.mpi = self.serial

    def ac_subst_var_serial(self,fh):
        m4_generic_cxx_serial_conftest(
            self,fh,
            # header
            "suitesparse/umfpack.h",
            # preamble
            """
#include <suitesparse/umfpack.h>
""", 
            # body
            """
  double * null = (double*) NULL;
  int * inull = (int*) NULL;
  int n = 0;
  void * Symbolic;
  (void) umfpack_di_symbolic(n,n,inull,inull,null,&Symbolic,null,null);
""") 



    def ac_subst_var_openmp(self,fh):
        return self.ac_subst_var_serial(fh)

