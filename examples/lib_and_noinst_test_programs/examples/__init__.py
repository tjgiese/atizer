#!/usr/bin/env python

from atizer import *
from cxx import package as cxx
from python import package as python
from fortran import package as fortran

targets = []
subpkgs = [ cxx, python, fortran ]
package = autopackage("tdbsc-examples",targets,subpkgs)
#package.recursive_make = True

if __name__ == "__main__":
    package.configure()





