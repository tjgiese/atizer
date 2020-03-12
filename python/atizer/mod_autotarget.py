#!/usr/bin/env python

from .utilities import *
from .f90deps import f90deps as f90deps
from .f90deps import printf90deps as printf90deps
from .f90deps import replace_ext as replace_ext
from . import licenses
import copy

class autotarget(object):

    def __init__(self,name,directory=None):
        self.name = self.__class__.__name__
        if name is not None:
            self.name = name

        # self.directory is the subdirectory relative to neareset
        # Makefile.am
        # that contains the source and header files to be searched
        # for.  E.g., if directory=here()/src, where here() is the PWD
        # of the config.py script that instantiated this object,
        # then the source code is presumed to be 
        # PWD/src/*.c PWD/src/*.cpp  PWD/src/*.f90 ...etc
        # and all subdirectories, recursively
        # PWD/src/*/*.c PWD/src/*/*/*.c ...
        self.copyright_holder = None
        self.license = licenses.MIT
        self.directory = directory
        self.path_from_configure = directory
        self.path_from_makefile = directory
        # language used to link the library C++, C, Fortran
        self.lang = "C++"
        self.sources = []
        self.headers = []
        if directory is not None:
            self.sources = recursive_find_any_of([\
                    "*.c", "*.cpp", "*.f90", "*.F90" ], self.directory )
            self.headers = recursive_find_any_of(["*.h","*.hpp","*.tpp"],\
                                                     self.directory)

        # these are copied to $(prefix)/bin
        self.dist_bin_SCRIPTS = []
        # these are copied to $(pythondir),
        # which is where python packages are stored
        self.python_package = []

        self.dist_noinst_SCRIPTS = []

        # other files that are included in the tarball, 
        # but are not installed
        self.EXTRA_DIST = []

        # a list of other autolib objects that this library depends on
        self.libs = []

        # name of this lib when compiled in serial,   e.g. foo
        self.serial = serialinfo(name)
        self.openmp = serialinfo(name)
        self.mpi    = serialinfo(name)


        # extra makefile rules that are verbatim added to the makefile
        self.extra_make_rules = ""

        # extra actions to perform when someone does a "make clean"
        self.clean = "\t" + "-rm -f *.mod" + "\n"
        # extra actions when someone does a "make distclean"
        self.distclean = "\t" + "-rm -fr *.mod *~ autom4te.cache " \
            + "aclocal.m4 config.guess config.sub configure depcomp " \
            + "install-sh ltmain.sh Makefile.in missing AUTHORS " \
            + "COPYING NEWS README ChangeLog config.log " \
            + "config.status libtool" + "\n"

        #=============================
        # if true, then compile as 
        #   noinst_PROGRAMS += name
        self.noinst = False
        #=============================
        # if true, then compile as 
        #   namedir = directory
        #   name_PROGRAMS = name
        self.install_here = False
        # ============================
        # if true, then create doxygen docs for this program
        self.doxygen = False


    def enable_openmp(self):
        self.openmp = openmpinfo(self.name)

        
    def enable_mpi(self):
        self.mpi = mpiinfo(self.name)

    def can_compile(self):
        return ( len(self.sources) > 0 or len(self.headers) > 0 or len(self.dist_bin_SCRIPTS) > 0 or len(self.python_package) > 0 )


    def determine_languages(self):
        """
        Sets 
        self.has_fortran
        self.has_c
        self.has_cxx
        self.has_python
        by examining the source code of each target
        """

        self.has_fortran = False
        self.has_c = False
        self.has_cxx = False
        self.has_python = False

        for s in self.sources:
            if ".f90" == s[-4:] or ".F90" == s[-4:] \
                    or ".f" == s[-2:] or ".F" == s[-2:] \
                    or ".f77" == s[-4:] or ".F77" == s[-4:]:
                self.has_fortran = True
            elif ".c" == s[-2:]:
                self.has_c = True
            elif ".cpp" == s[-4:]:
                self.has_cxx = True
        for s in self.dist_bin_SCRIPTS + self.python_package:
            if ".py" == s[-3:]:
                self.has_python = True


    def query_compiles_an_openmp_target(self):
        try:
            already_tested = self.compiles_an_openmp_target
        except:
            self.compiles_an_openmp_target = ( self.openmp.var != self.serial.var )
            for s in PrependPathToFiles( self.path_from_configure, self.sources + self.headers ):
                for line in open(s,"r"):
                    if "OPENMP" in line or "omp.h" in line or "#pragma omp" in line or "!$OMP" in line or " omp_" in line:
                        self.compiles_an_openmp_target = True
                        break
                if self.compiles_an_openmp_target:
                    break

    def query_links_to_an_openmp_target(self):
        self.links_to_an_openmp_target = False
        self.query_compiles_an_openmp_target()
        for lib in self.libs:
            lib.query_links_to_an_openmp_target()
            if lib.compiles_an_openmp_target:
                self.links_to_an_openmp_target = True
                break


    def license_filename(self):
        lfile = None
        if len( self.headers + self.python_package ) > 0 or self.can_compile():
            if self.copyright_holder is not None:
                lfile = "LICENSE.%s"%(self.name)
        return lfile


    def print_license(self):
        lfile = self.license_filename()
        if self.copyright_holder is None:
            sys.stderr.write("""\n\n\n\nTARGET %s in directory %s should set self.copyright_holder = "John Doe" in its class constructor.  You can adjust the license by setting self.license = license.<type> where <type> is a function defined in the license package\n\n\n\n"""%(self.name,self.directory))
        if not lfile is None:
            if not os.path.exists(lfile):
                fh = open(lfile,"w")
                fh.write("The following files are provided using the license described below:\n")
                fh.write("%s\n\n\n"%( " ".join( PrependPathToFiles(self.path_from_configure, self.sources+self.headers+self.python_package+self.dist_bin_SCRIPTS )) ))
                fh.write( self.license( self.copyright_holder ) )
                fh.close()
