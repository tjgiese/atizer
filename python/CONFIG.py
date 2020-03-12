#!/usr/bin/env python
import os
from atizer import *
from atizer.dbase import *

class pyatizer(autoprog):
    def __init__( self, srcdir=None ):
        super( pyatizer, self ).__init__( "atizer", srcdir )
        self.copyright_holder = "Timothy J. Giese"
        if len(self.sources) > 0 or len(self.headers) > 0:
            print("python_module atizer contains headers",self.headers)
            print("python_module atizer contains sources",self.sources)
            raise Exception("Invalid python_module")
        self.dist_bin_SCRIPTS = recursive_find("atizer-*",self.directory)
        self.python_package = []
        for py in recursive_find_any_of(["*.py","*.m4"], self.directory ):
            p,f=os.path.split(py)
            if "m4/m4" in p:
                continue
            p = p.replace( os.path.abspath(os.getcwd()), "").lstrip(r"/")
            if p == "":
                pass
            else:
                self.python_package.append( py )



class m4dir(autoprog):
    def __init__( self, srcdir=None ):
        super( m4dir, self ).__init__( "m4", srcdir )
        for filename in recursive_find("*",self.directory + "/atizer/m4/m4"):
            self.python_package.append(filename)

m4pkg = autopackage(
    "atizer-m4",
    targets=[ m4dir( here() ) ],
    subdirs=[],
    version="0.1",
    apiversion="0:0:0")

package = autopackage(
    "atizer",
    targets=[ pyatizer( here() ) ],
    subdirs=[ m4pkg ],
    version="0.1",
    apiversion="0:0:0")

if __name__ == "__main__":
    package.configure()
