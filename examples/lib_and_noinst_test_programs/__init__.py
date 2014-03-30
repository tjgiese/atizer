#!/usr/bin/env python
from atizer import *
from atizer.dbase import *
from tests import package as tests
from src import package as src

package = autopackage(
    "tdbsc",
    targets=[],
    subdirs=[tests,src],
    version="0.1",
    apiversion="0:0:0")

if __name__ == "__main__":
    package.configure()
