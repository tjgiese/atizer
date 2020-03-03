from ..base import *
from ..m4 import *
import copy
class nlopt(autolib):
    def __init__(self):
        super( nlopt , self ).__init__( "nlopt" )
        self.serial.var = "NLOPT_LIBS"
        self.serial.var_default_value = "-lnlopt"
        self.serial.name = "nlopt"
        self.serial.cppflags = ""
        self.serial.ldflags = ""
        self.openmp = self.serial;
        self.mpi = self.serial

    def ac_subst_var_serial(self,fh):
        m4_generic_cxx_serial_conftest(
            self,fh,
            # header
            "nlopt.hpp",
            # preamble
            """
#include <nlopt.hpp>
""", 
            # body
            """
  nlopt::opt nlo( nlopt::LN_COBYLA, 1 );
""") 



    def ac_subst_var_openmp(self,fh):
        return self.ac_subst_var_serial(fh)

