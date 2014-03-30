#!/usr/bin/env python
from atizer import *
from atizer.dbase import *
from finitediff import package as finitediff

package = autopackage(
    "tests",
    targets=[],
    subdirs=[finitediff],
    version="0.1",
    apiversion="0:0:0")

if __name__ == "__main__":
    package.configure()
