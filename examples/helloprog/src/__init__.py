#!/usr/bin/env python
from atizer import *
from atizer.dbase import *

class helloprog(autoprog):
    def __init__( self, srcdir=None ):
        super( helloprog, self ).__init__( "helloprog", srcdir )

        self.copyright_holder = "Timothy J. Giese"
        self.license = licenses.MIT

        ## @brief List of autolib objects representing library dependencies
        self.libs = []

        ## @brief List of filenames to be distributed, but not installed
        self.dist_noinst_SCRIPTS = []

        ## @brief If True, then compile the target without installing it
        #         (default False)
        self.noinst = False

        ## @brief If True, "make doxygen-doc" create documentation html
        self.doxygen = False

        # self.enable_openmp()
        # self.enable_mpi()

package = autopackage(
    "helloprog",
    targets=[ helloprog( here() ) ],
    subdirs=[],
    version="0.1",
    apiversion="0:0:0")

if __name__ == "__main__":
    package.configure()
