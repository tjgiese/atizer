#!/usr/bin/env python
from atizer import *
from atizer.dbase import *

import sys
sys.path.insert(0,here() + "/../..")
from targets import *
del sys.path[0]


class fortran_example(autoprog):
    def __init__( self, srcdir=None ):
        super( fortran_example, self ).__init__( "fortran_example", srcdir )

        self.copyright_holder = "Timothy J. Giese"
        self.license = licenses.MIT

        ## @brief List of autolib objects representing library dependencies
        self.libs = [ tdbsc() ]

        ## @brief List of filenames to be distributed, but not installed
        self.dist_noinst_SCRIPTS = []
        self.EXTRA_DIST = [ "ade.xyz", "ade.2dbspl" ]

        ## @brief If True, then compile the target without installing it
        #         (default False)
        self.noinst = True

        ## @brief If True, "make doxygen-doc" create documentation html
        self.doxygen = False

        # self.enable_openmp()
        # self.enable_mpi()

package = autopackage(
    "fortran_example",
    targets=[ fortran_example( here() ) ],
    subdirs=[],
    version="0.1",
    apiversion="0:0:0")

if __name__ == "__main__":
    package.configure()
