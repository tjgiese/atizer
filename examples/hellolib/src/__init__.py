#!/usr/bin/env python
from atizer import *
from atizer.dbase import *

class hello(autolib):
    def __init__( self, srcdir=None ):
        super( hello, self ).__init__( "hello", srcdir )

        self.copyright_holder = "Timothy J. Giese"
        self.license = licenses.MIT

        ## @brief List of autolib objects representing library dependencies
        self.libs = []

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

        # self.enable_openmp()
        # self.enable_mpi()

    def ac_subst_var_serial(self,fh):
        m4_generic_cxx_serial_conftest(
            self,fh,
            "hello.hpp",
            """#include <hello/hello.hpp>""",
            """hello();""")

    # def ac_subst_var_openmp(self,fh):
    #     m4_generic_cxx_openmp_conftest(
    #         self,fh,
    #         "hello.hpp",
    #         """#include <hello/hello.hpp>""",
    #         """hello();""")

    # def ac_subst_var_mpi(self,fh):
    #     m4_generic_cxx_mpi_conftest(
    #         self,fh,
    #         "hello.hpp",
    #         """#include <hello/hello.hpp>""",
    #         """hello();""")

package = autopackage(
    "hello",
    targets=[ hello( here() ) ],
    subdirs=[],
    version="0.1",
    apiversion="0:0:0")

if __name__ == "__main__":
    package.configure()
