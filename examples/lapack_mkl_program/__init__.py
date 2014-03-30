#!/usr/bin/env python

from atizer import *
from atizer.dbase import *

class lapack_mkl_program(autoprog):
    def __init__(self,basedir=None):
        super( lapack_mkl_program , self ).__init__( "lapack_mkl_program", basedir )
        self.libs = [ lapack(), rt() ]
        self.noinst = True

targets = [lapack_mkl_program(here()+"/src")]
subdirs = []
package = autopackage("lapack_mkl_program",targets,subdirs)

if __name__ == "__main__":
    package.configure()



