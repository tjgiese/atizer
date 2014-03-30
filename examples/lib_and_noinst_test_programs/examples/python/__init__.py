#!/usr/bin/env python
from atizer import *
from atizer.dbase import *

import sys
sys.path.insert(0,here() + "/../..")
from targets import *
del sys.path[0]


class pytdbsc(autolib):
    def __init__( self, srcdir=None ):
        super( pytdbsc, self ).__init__( "pytdbsc", srcdir )

        self.copyright_holder = "Timothy J. Giese"
        self.license = licenses.MIT

        ## @brief List of autolib objects representing library dependencies
        self.libs = [ tdbsc(), boost_python() ]

        ## @brief List of filenames to be distributed, but not installed
        self.dist_noinst_SCRIPTS = [ "python_example.py" ]
        self.EXTRA_DIST = [ "ade.xyz", "ade.2dbspl" ]

        ## @brief If True, then compile the target without installing it
        #         (default False)
        self.noinst = False

        ## @brief If True, then install the library within the build tree
        #         (default False)
        self.install_here = True

        ## @brief If True, then link the library in a manner suitable
        #         for importing it into a python script
        #         (default False)
        self.python_module = True

        ## @brief If True, "make doxygen-doc" create documentation html
        self.doxygen = False

        # self.enable_openmp()
        # self.enable_mpi()

package = autopackage(
    "pytdbsc",
    targets=[ pytdbsc( here() ) ],
    subdirs=[],
    version="0.1",
    apiversion="0:0:0")

if __name__ == "__main__":
    package.configure()
