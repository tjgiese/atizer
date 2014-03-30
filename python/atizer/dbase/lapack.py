from ..base import *
from ..m4 import *
import copy
class lapack(autolib):
    def __init__(self):
        super( lapack , self ).__init__( "lapack" )
        self.serial.var = "LAPACK_LIBS"
        self.serial.name = "lapack"
        self.serial.cppflags = ""
        self.serial.ldflags = ""
        self.openmp = copy.deepcopy(self.serial)
        self.openmp.var = "LAPACK_OPENMP_LIBS"
        self.openmp.name = "lapack/openmp"
        self.mpi = self.serial

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ay_lapack.m4") )
        fh.write("AY_LAPACK\n")

    def ac_subst_var_openmp(self,fh):
        fh.write( ax_macro("ay_lapack_openmp.m4") )
        fh.write("AY_LAPACK_OPENMP\n")
