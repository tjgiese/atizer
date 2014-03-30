#!/usr/bin/env python
from atizer import *
from atizer.dbase import *

class test1(autolib):
    def __init__( self, srcdir=None ):
        super( test1, self ).__init__( "test1", srcdir )

        self.copyright_holder = "Timothy J. Giese"
        self.license = licenses.MIT

        ## @brief List of autolib objects representing library dependencies
        self.libs = [ boost_python() ]

        ## @brief List of filenames to be distributed, but not installed
        self.dist_noinst_SCRIPTS = []

        ## @brief If True, then compile the target without installing it
        #         (default False)
        self.noinst = False

        ## @brief If True, then install the library within the build tree
        #         (default False)
        self.install_here = False

        ## @brief If True, then link the library in a manner suitable
        #         for importing it into a python script
        #         (default False)
        self.python_module = True

        ## @brief If True, "make doxygen-doc" create documentation html
        self.doxygen = False

        # self.enable_openmp()
        # self.enable_mpi()

package = autopackage(
    "test1",
    targets=[ test1( here() ) ],
    subdirs=[],
    version="0.1",
    apiversion="0:0:0")

if __name__ == "__main__":
    package.configure()
