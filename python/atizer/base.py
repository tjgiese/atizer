#!/usr/bin/env python

import sys,os,stat,inspect,fnmatch
from glob import *
from collections import defaultdict as ddict

from .m4 import *

from .utilities import *
from .mod_autolib import autolib
from .mod_autoprog import autoprog
from .mod_autopackage import autopackage

# todo
#
# am_write should only set bin_PROGRAMS = [empty] and lib_LTLIBRARIES = [empty] 
# only immediately upon opening Makefile.am
#
# am_write needs to recursively determine the dependency var's instead of just looking at the top level
#



def here():
    """
    Returns the directory-part of the full path of the script
    that called this function.
    """
    filename = inspect.getfile(sys._getframe(1))
    return os.path.dirname(os.path.realpath(filename))


