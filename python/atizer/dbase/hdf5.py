from ..base import *
from ..m4 import *
import copy
class hdf5(autolib):
    def __init__(self,optional=False):
        super( hdf5 , self ).__init__( "hdf5" )
        self.optional = optional
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
        if self.optional:
            fh.write("ACX_HDF5(atp_ok=yes,atp_ok=no)\n")
            fh.write("""

AM_CONDITIONAL([HAVE_%s],[test "x$atp_ok" = "xyes"])

AS_IF( [test "x$atp_ok" = "xyes"],
[
AC_SUBST([AM_CPPFLAGS],["-DHAVE_%s ${AM_CPPFLAGS}"])
])
"""%(self.serial.var,self.serial.var))
            
        else:
            fh.write("ACX_HDF5(AC_DEFINE(HAVE_HDF5,1,[Define if you have the HDF5 library.]),%s)\n"%(m4_error("Could not link to HDF5 library")))
            
#        if not self.optional:
#            fh.write("AS_IF( [test \"x$acx_hdf5_ok\"

        
