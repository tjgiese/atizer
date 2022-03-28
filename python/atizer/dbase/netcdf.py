from ..base import *
from ..m4 import *
from .hdf5 import hdf5
import copy

class netcdf(autolib):
    def __init__(self,optional=False):
        super( netcdf , self ).__init__( "netcdf" )
        self.optional=optional
        self.libs = [ hdf5() ]
        self.serial.var = "NETCDF_LIBS"
        self.serial.var_default_value = "-lnetcdf_c++ -lnetcdf"
        self.serial.name = "netcdf"
        self.serial.cppflags = "$(NETCDF_CPPFLAGS)"
        self.serial.ldflags = "$(NETCDF_LDFLAGS)"
        self.serial.fcflags = "$(NETCDF_FCFLAGS)"
        #self.openmp = copy.deepcopy(self.serial)
        #self.openmp.var = "NETCDF_OPENMP_LIBS"
        #self.openmp.name = "netcdf/openmp"
        self.openmp = copy.deepcopy(self.serial)
        self.mpi = copy.deepcopy(self.serial)

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("acx_netcdf.m4") )
        fh.write("""AC_LANG_PUSH([C++])
ACX_NETCDF
AC_LANG_POP([C++])\n""")
        m4_generic_cxx_serial_conftest(
            self,fh,
            "netcdfcpp.h",
            """#include <netcdfcpp.h>""",
            """
            NcFile f("");
            bool ok = f.is_valid();
            """)

