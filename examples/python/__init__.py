#!/usr/bin/env python
import os
from atizer import *
from atizer.dbase import *

class python_package_python(autoprog):
    def __init__( self, srcdir=None ):
        super( python_package_python, self ).__init__( "python_package_python", srcdir )
        if len(self.sources) > 0 or len(self.headers) > 0:
            print "python_module python_package_python contains headers",self.headers
            print "python_module python_package_python contains sources",self.sources
            raise Exception("Invalid python_module")
        self.dist_bin_SCRIPTS = []
        self.python_package = []
        for py in recursive_find("*.py", self.directory ):
            p,f=os.path.split(py)
            p = p.replace( os.path.abspath(os.getcwd()), "").lstrip(r"/")
            if p == "":
                if f != "__init__.py":
                    self.dist_bin_SCRIPTS.append( py )
            else:
                self.python_package.append( py )

package = autopackage(
    "python_package_python",
    targets=[ python_package_python( here() ) ],
    subdirs=[],
    version="0.1",
    apiversion="0:0:0")

if __name__ == "__main__":
    package.configure()
