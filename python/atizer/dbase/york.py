#!/usr/bin/env python
from ..base import *
from ..m4 import *
from .. import licenses
from .rt import rt
from .lapack import lapack
from .fftw3 import fftw3
import copy


class ygxx(autolib):
    def __init__( self, srcdir=None ):
        super( ygxx, self ).__init__( "ygxx", srcdir )

        self.copyright_holder = "Timothy J. Giese"
        self.license = licenses.MIT

#        if self.directory is not None:
#            self.sources = recursive_find_any_of([\
#                    "*.f90", "*.F90" ], self.directory )

        ## @brief List of autolib objects representing library dependencies
        self.libs = [ lapack(), rt() ]

        ## @brief List of filenames to be distributed, but not installed
        self.dist_noinst_SCRIPTS = []
        self.EXTRA_DIST = []

        ## @brief If True, then compile the target without installing it
        #         (default False)
        self.noinst = False

        ## @brief If True, then install the library within the build tree
        #         (default False)
        self.install_here = False

        ## @brief If True, then link the library in a manner suitable
        #         for importing it into a python script
        #         (default False)
        self.python_module = False

        ## @brief If True, "make doxygen-doc" create documentation html
        self.doxygen = False

        self.enable_openmp()
        # self.enable_mpi()


    def ac_subst_var_serial(self,fh):
        m4_generic_cxx_serial_conftest(
            self,fh,
            "ygxx/YGXX_PeriodicTableMod.hpp",
            """#include <ygxx/YGXX_PeriodicTableMod.hpp>""",
            """bool ok = YGXX::IsAValidElement("H");""")

    def ac_subst_var_openmp(self,fh):
        m4_generic_cxx_openmp_conftest(
            self,fh,
            "ygxx/YGXX_Timer.hpp",
            """#include <ygxx/YGXX_Timer.hpp>""",
            """YGXX::Timer t; t.Start(); t.Stop();""")

    # def ac_subst_var_mpi(self,fh):
    #     m4_generic_cxx_mpi_conftest(
    #         self,fh,
    #         "ygxx.hpp",
    #         """#include <ygxx/ygxx.hpp>""",
    #         """ygxx();""")





class ccdl(autolib):
    def __init__( self, srcdir=None ):
        super( ccdl, self ).__init__( "ccdl", srcdir )

        self.copyright_holder = "Timothy J. Giese"
        self.license = licenses.MIT

        ## @brief List of autolib objects representing library dependencies
        self.libs = [ lapack(), fftw3(), rt() ]

        ## @brief List of filenames to be distributed, but not installed
        self.dist_noinst_SCRIPTS = []
        self.EXTRA_DIST = []

        ## @brief If True, then compile the target without installing it
        #         (default False)
        self.noinst = False

        ## @brief If True, then install the library within the build tree
        #         (default False)
        self.install_here = False

        ## @brief If True, then link the library in a manner suitable
        #         for importing it into a python script
        #         (default False)
        self.python_module = False

        ## @brief If True, "make doxygen-doc" create documentation html
        self.doxygen = False

        self.enable_openmp()
        # self.enable_mpi()

    def ac_subst_var_serial(self,fh):
        m4_generic_cxx_serial_conftest(
            self,fh,
            "ccdl/math.hpp",
            """#include <ccdl/math.hpp>""",
            """
std::vector<double> v(3,0.);
ccdl::v b(1,v.data());
ccdl::ge A(1,1,b.end());
ccdl::v x(1,A.end());
b.dot(A,x);
            """)

    def ac_subst_var_openmp(self,fh):
        m4_generic_cxx_openmp_conftest(
            self,fh,
            "ccdl/math.hpp",
            """#include <ccdl/math.hpp>""",
            """
std::vector<double> v(3,0.);
ccdl::v b(1,v.data());
ccdl::ge A(1,1,b.end());
ccdl::v x(1,A.end());
b.dot(A,x);
            """)

    # def ac_subst_var_mpi(self,fh):
    #     m4_generic_cxx_mpi_conftest(
    #         self,fh,
    #         "ccdl.hpp",
    #         """#include <ccdl/ccdl.hpp>""",
    #         """ccdl();""")


