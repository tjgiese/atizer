from ..base import *
from ..m4 import *
import copy
class hdf5(autolib):
    def __init__(self):
        super( hdf5 , self ).__init__( "hdf5" )
        self.serial.var = "HDF5_LIBS"
        self.serial.name = "hdf5"
        self.serial.cppflags = "$(HDF5_CPPFLAGS)"
        self.serial.ldflags = "$(HDF5_LDFLAGS)"
        #self.openmp = copy.deepcopy(self.serial)
        #self.openmp.var = "HDF5_OPENMP_LIBS"
        #self.openmp.name = "hdf5/openmp"
        self.openmp = copy.deepcopy(self.serial)
        self.mpi = copy.deepcopy(self.serial)

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("acx_hdf5.m4") )
        fh.write("ACX_HDF5\n")

        
