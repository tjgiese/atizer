#!/usr/bin/env python

from atizer import *
from targets import *

targets = [ tdbsc(here()) ]
subpkgs = [ ]
package = autopackage("tdbsc",targets,subpkgs)

if __name__ == "__main__":
    package.configure()





