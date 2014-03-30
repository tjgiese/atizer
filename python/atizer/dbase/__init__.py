#!/usr/bin/env python

import os
import glob

#__all__ = [ os.path.basename(f)[:-3] 
#            for f in glob.glob(os.path.dirname(__file__)+"/*.py")
#            if not f.endswith('__init__.py')
#            and
#            os.path.isfile(f)
#            ]

#for f in glob.glob(os.path.dirname(__file__)+"/*.py"):
#    if not f.endswith('__init__.py') and os.path.isfile(f):
#        from os.path.basename(f)[:-3] import *

from .boost import *
from .python import *
from .lapack import *
from .rt import *
from .fftw3 import *
from .york import *

