from ..base import *
from ..m4 import *
from .hdf5 import hdf5
import copy

class libarchive(autolib):
    def __init__(self,optional=False):
        super( libarchive , self ).__init__( "libarchive" )
        self.optional=optional
        self.libs = [ hdf5(self.optional) ]
        self.serial.var = "LIBARCHIVE_LIBS"
        self.serial.var_default_value = "-larchive"
        self.serial.name = "libarchive"
        self.serial.cppflags = "$(LIBARCHIVE_CPPFLAGS)"
        self.serial.ldflags = "$(LIBARCHIVE_LDFLAGS)"
        self.serial.fcflags = "$(LIBARCHIVE_FCFLAGS)"
        #self.openmp = copy.deepcopy(self.serial)
        #self.openmp.var = "LIBARCHIVE_OPENMP_LIBS"
        #self.openmp.name = "libarchive/openmp"
        self.openmp = copy.deepcopy(self.serial)
        self.mpi = copy.deepcopy(self.serial)

    def ac_subst_var_serial(self,fh):
        #fh.write( ax_macro("acx_libarchive.m4") )
        #fh.write("""AC_LANG_PUSH([C++])
#ACX_LIBARCHIVE
#AC_LANG_POP([C++])\n""")
        m4_generic_cxx_serial_conftest(
            self,fh,
            "archive.h",
            """
#include <archive.h>
#include <archive_entry.h>
""",
            """
          archive *a;
          a = archive_read_new();
          archive_entry *entry;
          int64_t length = archive_entry_size(entry);
            """)

