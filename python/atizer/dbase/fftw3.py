from ..base import *
from ..m4 import *
import copy
class fftw3(autolib):
    def __init__(self):
        super( fftw3 , self ).__init__( "fftw3" )
        self.serial.var = "FFTW3_LIBS"
        self.serial.var_default_value = "-lfftw3"
        self.serial.name = "fftw3"
        self.serial.cppflags = ""
        self.serial.ldflags = ""
        self.openmp = copy.deepcopy(self.serial)
        self.openmp.var = "FFTW3_OPENMP_LIBS"
        self.openmp.var_default_value = "-lfftw3_omp -lfftw3"
        self.openmp.name = "fftw3/openmp"
        self.mpi = self.serial

    def ac_subst_var_serial(self,fh):
        m4_generic_cxx_serial_conftest(
            self,fh,
            # header
            "fftw3.h",
            # preamble
            """
#include <fftw3.h>
""", 
            # body
            """
fftw_malloc(3);
""") 



    def ac_subst_var_openmp(self,fh):
        m4_generic_cxx_openmp_conftest(
            self,fh,
            # header
            "fftw3.h",
            # preamble
            """
#include <omp.h>
#include <fftw3.h>
""", 
            # body
            """
fftw_plan_with_nthreads( omp_get_max_threads() );
fftw_malloc(3);
""") 

