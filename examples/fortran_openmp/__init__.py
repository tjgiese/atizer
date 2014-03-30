#!/usr/bin/env python

from atizer import *
from atizer.dbase import *

import sys
#sys.path.insert(0,here() + "/../..")
#from targets import *
#del sys.path[0]


class fortran_example(autoprog):
    def __init__(self,basedir=None):
        super(fortran_example,self).__init__( "fortran_example", basedir )
        self.libs = [ ]
        self.noinst = True


targets = [ fortran_example(here()) ]
subdirs = []
package = autopackage("fortran_example",targets,subdirs)

if __name__ == "__main__":
    package.configure()





