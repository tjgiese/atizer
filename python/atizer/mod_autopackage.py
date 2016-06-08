#!/usr/bin/env python

import inspect,sys,os,stat,glob,subprocess,copy
from collections import defaultdict as ddict
from collections import OrderedDict as odict
import m4
from mod_autolib import autolib
from mod_autoprog import autoprog
from .utilities import *

class autopackage(object):
    """A package is a list of 1 or more targets and/or subdirectories.
    A target is either an autolib object corresponding to a library
    to be built or an autoprog object for a program.
    A subdirectory is a child directory that should be entered 
    and built.  That subdirectory cannot be a symbolic link to
    a parent directory outside of the top-level of the build.
    The subdirectory must contain a config.py file which defines
    a global variable "package" that is, itself, an autopackage
    object for that directory, e.g.

    foo/config.py:
    #!/usr/bin/env python
    from atizer import *
    package = autopackage("foo",[libfoo(here())],[])
    EOF

    name = the name of the package, e.g., foo
    targets = a list of autolib and/or autoprog objects
    subdirs = a list of subdirectory names to traverse and build
    """

    ################################################################
    ################################################################

    def __init__(self,name,targets,subdirs,directory=None, \
                     version="0.1",apiversion="0:0:0"):
        # self.directory is the filesystem location of the
        # script that actually instantiated this class, i.e.
        # it is the directory of the config.py file that describes
        # the package
        if directory is None:
            filename = inspect.getfile(sys._getframe(1))
            self.directory = os.path.dirname(os.path.realpath(filename))
        else:
            self.directory = os.path.realpath(directory)
        self.path_from_configure = self.directory
        self.path_from_makefile  = self.directory
        # the name of the package - the affects the name of the
        # distribution tarball, but it is NOT the name of the
        # executable or program that you are creating; a package
        # can provide multiple libraries and/or programs
        self.name = name
        #
        self.version = version
        # the api version is a series of 3 numbers x:y:z
        # used when creating shared object files
        self.apiversion = apiversion
        # prefix is the default installation directory, 
        # e.g. $HOME/devel/local
        # if prefix is None, then the standard atizer
        # default is used
        self.prefix = None
        self.install_exec_hook = None
        self.clean_local = None
        self.distclean_local = None

        # a list of extra files that are included in the distribution
        # but are not installed via make install
        self.dist_noinst_SCRIPTS = []

        self.recursive_make = False

        # for each header and source file, rewrite the full-path
        # to be a relative path to the top-level directory
        self.targets = targets
        for c in targets:
            c.parent = self
            c.apiversion = self.apiversion
            c.path_from_makefile = RemoveBasePathFromFilePath(self.directory,c.directory)
            for array in [ c.sources, c.headers, c.dist_bin_SCRIPTS, c.python_package, c.EXTRA_DIST ]:
                for i in range(len(array)):
                    array[i] = RemoveBasePathFromFilePath( c.directory, array[i] )

        # transform the list of subdirectories into a dict
        # of names, whose values are the package objects
        self.subdirs = {}
        self.parent = None
        for subdir in subdirs:
            self.subdirs[ subdir.directory ] = subdir
            self.subdirs[ subdir.directory ].parent = self        
        self.__root(self)
        

    ################################################################
    ################################################################

    def write(self):
        """
        Writes configure.ac and all required Makefile.am's
        """
        self.am_write()
        self.ac_write()


    ################################################################
    ################################################################


    def configure(self):
        import subprocess
        self.write()
        subprocess.call(["./ac-aux/autogen.sh"]+sys.argv[1:])


    ################################################################
    ################################################################


    def __init_recursion(self,Print=False):
        if self == self.root:
            self.__all_child_targets()
            self.__all_targets()
            self.__all_child_deps()
            self.__path_from_configure()
            self.__path_from_makefile()
        self.__determine_languages()
        self.__inspect_targets()
        if Print:
            print "package.name ",self.name
            print "        all_child_targets",[ x for x in self.all_child_targets ]
            print "        all_targets      ",[ x for x in self.all_targets ]
            print "        all_child_deps   ",[ x for x in self.all_child_deps ]
        if self == self.root:
            for t in self.all_targets:
                self.all_targets[t].print_license()


    def __directories_with_source(self):
        dirs = {}
        for t in self.all_targets:
            lib = self.all_targets[t]
            srcs = PrependPathToFiles( lib.path_from_configure, lib.sources )
            for s in srcs:
                p,f = os.path.split(s)
                p = RemoveBasePathFromFilePath( self.root.directory, p )
                dirs[p] = None
        return [ d for d in dirs ]
    
                    


    def am_write(self,fh=None):
        """
        Writes a Makefile.am for this package and recursively write 
        Makefile.am's for each subpackage
        """
        close = False
        if fh == None:
            close = True
            fh = file(self.directory + "/Makefile.am","w")

        self.__init_recursion(True)


        if self == self.root or self.recursive_make:
            fh.write("dist_noinst_SCRIPTS =")
            if self == self.root:
                fh.write(" ./ac-aux/autodel.sh ./ac-aux/autogen.sh")
            fh.write("\n")
            fh.write("dist_bin_SCRIPTS =\n")
            fh.write("EXTRA_DIST =\n")
            fh.write("BUILT_SOURCES = \n")
            fh.write("opt_FCFLAGS = $(OPT_FCFLAGS)\n")
            fh.write("debug_FCFLAGS = $(DEBUG_FCFLAGS)\n")
            fh.write("_FCFLAGS := $(FCFLAGS)\n")
            fh.write("opt_V=0\n")
            fh.write("debug_V=0\n")
            fh.write("_V:=$(V)\n")
            fh.write("$(BUILT_SOURCES): FCFLAGS=$($(MAKECMDGOALS)_FCFLAGS)\n")
            fh.write("$(BUILT_SOURCES): V=$($(MAKECMDGOALS)_V)\n")

            if self.recursive_make:
                fh.write("SUBDIRS = %s\n"%(" ".join(self.subdirs[d].path_from_makefile for d in self.subdirs)))
            else:
                fh.write("SUBDIRS = \n")
            if self.has_library:
                fh.write("lib_LTLIBRARIES = \n")
                fh.write("noinst_LTLIBRARIES = \n")
            if self.has_python_module:
                fh.write("pyexec_LTLIBRARIES = \n")
            if self.has_program:
                fh.write("bin_PROGRAMS = \n")
                fh.write("noinst_PROGRAMS = \n")

        if self == self.root:
            for name in self.all_targets:
                fh.write("EXTRA_DIST +=")
                t = self.all_targets[name]
                lfile = t.license_filename()
                if not lfile is None:
                    fh.write(" %s"%(lfile))
                fh.write("\n")

        for target in self.targets:
            target.recursive_make = self.recursive_make
            target.am_write( fh )

        if self.recursive_make:
            for d in self.subdirs:
                self.subdirs[d].recursive_make = self.recursive_make
                self.subdirs[d].am_write()
        else:
            for d in self.subdirs:
                self.subdirs[d].recursive_make = self.recursive_make
                self.subdirs[d].am_write(fh)

        if self != self.root and not self.recursive_make:
            return

        fh.write("""
.PHONY: opt
opt: AM_MAKEFLAGS=CPPFLAGS="-DNDEBUG $(CPPFLAGS)" CFLAGS="$(OPT_CFLAGS)" FCFLAGS="$(OPT_FCFLAGS)" CXXFLAGS="$(OPT_CXXFLAGS)"
opt: AM_MAKEFLAGS+=$(if $(V),V=$(V),V=0 -s)
opt: all

.PHONY: debug
debug: AM_MAKEFLAGS=CFLAGS="$(DEBUG_CFLAGS)" FCFLAGS="$(DEBUG_FCFLAGS)" CXXFLAGS="$(DEBUG_CXXFLAGS)"
debug: AM_MAKEFLAGS+=$(if $(V),V=$(V),V=0 -s)
debug: all

""")        

        self.doxygen = False
        for t in self.all_child_targets:
            dep = self.all_child_targets[t]
            if dep.doxygen:
                self.doxygen = True

        if self.doxygen:
            fh.write( self.__am_doxygen() )
            self.__doxyfile()

        if self.install_exec_hook is not None:
            fh.write("install-exec-hook:\n%s\n\n"%(self.install_exec_hook))
        else:
            fh.write("# install-exec-hook:\n#\tTo use this hook, set your package's self.install_exec_hook variable.  Be sure that each line starts with \\t\n\n")

        if self.clean_local is not None:
            fh.write("clean-local:\n%s\n\n"%(self.clean_local))
        else:
            fh.write("clean-local:\n\t-rm -f *.mod\n")
            for d in self.__directories_with_source():
                fh.write("\t-rm %s/*.$(OBJEXT) %s/*.lo\n"%(d,d))
            fh.write("\n")


        if self.distclean_local is not None:
            fh.write("distclean-local:\n%s\n\n"%(self.distclean_local))
        else:
            pass
            #install-sh config.sub config.guess ltmain.sh missing Makefile.in 
            #fh.write("distclean-local:\n\t-rm -fr *~ *.mod autom4te.cache aclocal.m4 depcomp AUTHORS COPYING NEWS README ChangeLog config.log config.status libtool Doxyfile.bak\n\n")

        if close: fh.close()


    ################################################################
    ################################################################

    def ac_write(self,fh=None):
        close = False
        if fh == None:
            close = True
            fh = file(self.directory + "/configure.ac","w")

        self.__init_recursion(False)

        if self.doxygen:
            fh.write( m4.ax_macro("ax_prog_doxygen.m4") + "\n" )
        fh.write( m4.ax_macro("ax_openmp.m4") + "\n" )
        fh.write( m4.ax_macro("ay_openmp_fc.m4") + "\n" )
        fh.write( m4.ax_macro("ax_prog_cc_mpi.m4") + "\n" )
        fh.write( m4.ax_macro("ax_prog_cxx_mpi.m4") + "\n" )
        fh.write( m4.ax_macro("ax_prog_fc_mpi.m4") + "\n" )
        fh.write( m4.ax_macro("ay_extra_flags.m4") + "\n" )

        self.__ac_init(fh)
        if self.doxygen:
            self.__ac_doxygen(fh)
        self.__enable_parallel(fh)
        self.__setup_compilers(fh)
        self.__lt_init(fh)
        self.__enable_static(fh)
        self.__add_prefix_to_flags(fh)
        self.__test_deps(fh)
        self.__ac_output(fh)
        if close: fh.close()
        self.__autodel()
        self.__autogen()
        self.__make_sh()


    def __am_doxygen(self):
        return """

dist_noinst_SCRIPTS += Doxyfile

## --------------------------------- ##
## Format-independent Doxygen rules. ##
## --------------------------------- ##

if DX_COND_doc

## ------------------------------- ##
## Rules specific for HTML output. ##
## ------------------------------- ##

if DX_COND_html

DX_CLEAN_HTML = @DX_DOCDIR@/html

endif DX_COND_html

## ------------------------------ ##
## Rules specific for CHM output. ##
## ------------------------------ ##

if DX_COND_chm

DX_CLEAN_CHM = @DX_DOCDIR@/chm

if DX_COND_chi

DX_CLEAN_CHI = @DX_DOCDIR@/@PACKAGE@.chi

endif DX_COND_chi

endif DX_COND_chm

## ------------------------------ ##
## Rules specific for MAN output. ##
## ------------------------------ ##

if DX_COND_man

DX_CLEAN_MAN = @DX_DOCDIR@/man

endif DX_COND_man

## ------------------------------ ##
## Rules specific for RTF output. ##
## ------------------------------ ##

if DX_COND_rtf

DX_CLEAN_RTF = @DX_DOCDIR@/rtf

endif DX_COND_rtf

## ------------------------------ ##
## Rules specific for XML output. ##
## ------------------------------ ##

if DX_COND_xml

DX_CLEAN_XML = @DX_DOCDIR@/xml

endif DX_COND_xml

## ----------------------------- ##
## Rules specific for PS output. ##
## ----------------------------- ##

if DX_COND_ps

DX_CLEAN_PS = @DX_DOCDIR@/@PACKAGE@.ps

DX_PS_GOAL = doxygen-ps

doxygen-ps: @DX_DOCDIR@/@PACKAGE@.ps

@DX_DOCDIR@/@PACKAGE@.ps: @DX_DOCDIR@/@PACKAGE@.tag
    cd @DX_DOCDIR@/latex; \
    rm -f *.aux *.toc *.idx *.ind *.ilg *.log *.out; \
    $(DX_LATEX) refman.tex; \
    $(MAKEINDEX_PATH) refman.idx; \
    $(DX_LATEX) refman.tex; \
    countdown=5; \
    while $(DX_EGREP) 'Rerun (LaTeX|to get cross-references right)' \
                      refman.log > /dev/null 2>&1 \
       && test $$countdown -gt 0; do \
        $(DX_LATEX) refman.tex; \
        countdown=`expr $$countdown - 1`; \
    done; \
    $(DX_DVIPS) -o ../@PACKAGE@.ps refman.dvi

endif DX_COND_ps

## ------------------------------ ##
## Rules specific for PDF output. ##
## ------------------------------ ##

if DX_COND_pdf

DX_CLEAN_PDF = @DX_DOCDIR@/@PACKAGE@.pdf

DX_PDF_GOAL = doxygen-pdf

doxygen-pdf: @DX_DOCDIR@/@PACKAGE@.pdf

@DX_DOCDIR@/@PACKAGE@.pdf: @DX_DOCDIR@/@PACKAGE@.tag
    cd @DX_DOCDIR@/latex; \
    rm -f *.aux *.toc *.idx *.ind *.ilg *.log *.out; \
    $(DX_PDFLATEX) refman.tex; \
    $(DX_MAKEINDEX) refman.idx; \
    $(DX_PDFLATEX) refman.tex; \
    countdown=5; \
    while $(DX_EGREP) 'Rerun (LaTeX|to get cross-references right)' \
                      refman.log > /dev/null 2>&1 \
       && test $$countdown -gt 0; do \
        $(DX_PDFLATEX) refman.tex; \
        countdown=`expr $$countdown - 1`; \
    done; \
    mv refman.pdf ../@PACKAGE@.pdf

endif DX_COND_pdf

## ------------------------------------------------- ##
## Rules specific for LaTeX (shared for PS and PDF). ##
## ------------------------------------------------- ##

if DX_COND_latex

DX_CLEAN_LATEX = @DX_DOCDIR@/latex

endif DX_COND_latex

.PHONY: doxygen-run doxygen-doc $(DX_PS_GOAL) $(DX_PDF_GOAL)

.INTERMEDIATE: doxygen-run $(DX_PS_GOAL) $(DX_PDF_GOAL)

doxygen-run: @DX_DOCDIR@/@PACKAGE@.tag

doxygen-doc: doxygen-run $(DX_PS_GOAL) $(DX_PDF_GOAL)

@DX_DOCDIR@/@PACKAGE@.tag: $(DX_CONFIG) $(pkginclude_HEADERS)
	rm -rf @DX_DOCDIR@
	$(DX_ENV) $(DX_DOXYGEN) $(srcdir)/$(DX_CONFIG)

DX_CLEANFILES = \
    @DX_DOCDIR@/@PACKAGE@.tag \
    -r \
    $(DX_CLEAN_HTML) \
    $(DX_CLEAN_CHM) \
    $(DX_CLEAN_CHI) \
    $(DX_CLEAN_MAN) \
    $(DX_CLEAN_RTF) \
    $(DX_CLEAN_XML) \
    $(DX_CLEAN_PS) \
    $(DX_CLEAN_PDF) \
    $(DX_CLEAN_LATEX)

endif DX_COND_doc

"""

    def __ac_doxygen(self,fh):
        fh.write("""
DX_HTML_FEATURE(ON)
DX_CHM_FEATURE(OFF)
DX_CHI_FEATURE(OFF)
DX_MAN_FEATURE(OFF)
DX_RTF_FEATURE(OFF)
DX_XML_FEATURE(OFF)
DX_PDF_FEATURE(OFF)
DX_PS_FEATURE(OFF)
DX_INIT_DOXYGEN([$PACKAGE_NAME])
""")

    def __doxyfile(self):
        f = "./" + self.path_from_makefile + "/Doxyfile"
        f = f.replace(r"//",r"/")
        subprocess.call("doxygen -g %s"%(f),shell=True)
        df = file(f,"a")
        df.write("""
DOT_CLEANUP            = YES
GENERATE_HTML          = $(GENERATE_HTML)
GENERATE_HTMLHELP      = $(GENERATE_HTMLHELP)
HHC_LOCATION           = $(HHC_PATH)
GENERATE_CHI           = $(GENERATE_CHI)
GENERATE_LATEX         = $(GENERATE_LATEX)
PAPER_TYPE             = $(PAPER_SIZE)
USE_PDFLATEX           = $(GENERATE_PDF)
GENERATE_RTF           = $(GENERATE_RTF)
GENERATE_MAN           = $(GENERATE_MAN)
GENERATE_XML           = $(GENERATE_XML)
GENERATE_TAGFILE       = $(DOCDIR)/$(PROJECT).tag
HAVE_DOT               = $(HAVE_DOT)
DOT_PATH               = $(DOT_PATH)
EXTRA_PACKAGES = amsmath
""")
        df.write("INPUT = ")
        for t in self.all_child_targets:
            dep = self.all_child_targets[t]
#            df.write(" $(SRCDIR)/%s"%(dep.path.replace(self.path,"")))
            df.write(" $(SRCDIR)/%s"%(RemoveBasePathFromFilePath(self.directory,dep.directory)))
        df.write("\n")

#PROJECT_NAME           = $(PROJECT)-$(VERSION)
        df.write("""
PROJECT_NAME           = %s
STRIP_FROM_PATH        = $(SRCDIR)
"""%(self.name))
        df.write("OUTPUT_DIRECTORY = $(DOCDIR)\n")
        


    ################################################################
    ################################################################

    def __ac_init(self,fh):
        fh.write("\n\n%s\n\n"%("dnl " + "="*76))
        fh.write("AC_INIT([%s], [%s],[],[%s])\n"%(self.name,self.version,self.name))
        if self.prefix is not None:
            fh.write("AC_PREFIX_DEFAULT([%s])\n"%(self.prefix))

        fh.write("""
AC_CONFIG_AUX_DIR([ac-aux])
AM_INIT_AUTOMAKE([1.10 -Wall no-define foreign tar-pax subdir-objects])
AM_SILENT_RULES
""")



    ################################################################
    ################################################################

    def __enable_parallel(self,fh):
        fh.write("""

# If --with-mpi=auto is used, try to find MPI, but use standard C compiler if it is not found.
# If --with-mpi=yes is used, try to find MPI and fail if it isn't found.
# If --with-mpi=no is used, use a standard C compiler instead.
AC_ARG_WITH(mpi, [AS_HELP_STRING([--with-mpi],
     [compile the MPI targets. If a mpi compiler is not found, then
    MPI is not used. Default: no])
],
[case "${withval}" in
  yes) with_mpi=yes ;;
  no)  with_mpi=no ;;
  auto) with_mpi=auto ;;
  *) AC_MSG_ERROR([bad value ${withval} for --with-mpi no/yes/auto]) ;;
esac]
,[with_mpi=no])

AM_CONDITIONAL([WITH_MPI], [test x$with_mpi != xno])

#if test x"$with_mpi" = xyes; then
#  AC_SUBST([AM_CPPFLAGS],["-DWITH_MPI ${AM_CPPFLAGS}"])
#fi

AC_ARG_WITH(openmp,
[AS_HELP_STRING([--with-openmp],
     [compile the OPENMP targets. Default: no])
],
[case "${withval}" in
  yes) with_openmp=yes ;;
  no)  with_openmp=no ;;
  *) AC_MSG_ERROR([bad value ${withval} for --with-openmp no/yes]) ;;
esac]
,[with_openmp=no])

AM_CONDITIONAL([WITH_OPENMP], [test x$with_openmp != xno])

""")



    ################################################################
    ################################################################

    def __setup_compilers(self,fh):
        self.__setup_c(fh)
        self.__setup_fc(fh)
        self.__setup_cxx(fh)
        if self.has_fortran or self.has_c or self.has_cxx:
            fh.write("AC_FC_LIBRARY_LDFLAGS\n")



    ################################################################
    ################################################################

    def __setup_c(self,fh):
        if self.has_c:
            fh.write("""
AX_PROG_CC_MPI([test x"$with_mpi" != xno],[WITH_MPI=yes],[
  WITH_MPI=no
  if test x"$with_mpi" = xyes; then
     AC_MSG_FAILURE([MPI compiler requested, but couldn't use MPI.])
  else
       if test x"$with_mpi" = xauto; then
          AC_MSG_WARN([No C MPI compiler found, won't use MPI for anything.])
       fi
  fi
])
AC_LANG_PUSH([C])
AX_OPENMP
AC_LANG_POP([C])
AC_SUBST([OPENMP_CFLAGS])
AY_OPT_CFLAGS
AY_DEBUG_CFLAGS

""")



    ################################################################
    ################################################################

    def __setup_fc(self,fh):
        if self.has_fortran:
            fh.write("""
AC_FC_SRCEXT(f90)
AX_PROG_FC_MPI([test x"$with_mpi" != xno],[WITH_MPI=yes],[
  WITH_MPI=no
  if test x"$with_mpi" = xyes; then
     AC_MSG_FAILURE([MPI compiler requested, but couldn't use MPI.])
  else
       if test x"$with_mpi" = xauto; then
          AC_MSG_WARN([No Fortran MPI compiler found, won't use MPI for anything.])
       fi
  fi
])
AC_LANG_PUSH([Fortran])
AY_FC_OPENMP
AC_LANG_POP([Fortran])
AC_SUBST([OPENMP_FCFLAGS])
AY_OPT_FCFLAGS
AY_DEBUG_FCFLAGS

""")



    ################################################################
    ################################################################

    def __setup_cxx(self,fh):
        if self.has_cxx:
            fh.write("""
AX_PROG_CXX_MPI([test x"$with_mpi" != xno],[WITH_MPI=yes],[
  WITH_MPI=no
  if test x"$with_mpi" = xyes; then
     AC_MSG_FAILURE([MPI compiler requested, but couldn't use MPI.])
  else
       if test x"$with_mpi" = xauto; then
          AC_MSG_WARN([No C++ MPI compiler found, won't use MPI for anything.])
       fi
  fi
])
AC_LANG_PUSH([C++])
AX_OPENMP
AC_LANG_POP([C++])
AC_SUBST([OPENMP_CXXFLAGS])
AY_OPT_CXXFLAGS
AY_DEBUG_CXXFLAGS

""")  



    ################################################################
    ################################################################

    def __lt_init(self,fh):
        if self.has_library:
            fh.write("m4_ifdef([AM_PROG_AR], [AM_PROG_AR])\nLT_INIT\n")
        if self.has_python_module or self.has_python:
            fh.write("AM_PATH_PYTHON\n")
#        for t in self.compilable_targets:
#            if isinstance(self.compilable_targets[t],autolib):
#                fh.write("LT_INIT\n")
#                break



    ################################################################
    ################################################################

    def __enable_static(self,fh):
        for t in self.all_targets:
            if isinstance(self.all_targets[t],autoprog):
                fh.write("""
AC_ARG_ENABLE(static-link,
  AC_HELP_STRING([--enable-static-link],
                 [link executables to static libraries only (fails to lnk if you are missing a library archive, e.g. libfoo.a]),
  [ay_static_link=$enableval],
  [ay_static_link=no])
if test "x$ay_static_link" = "xyes"; then
  AC_SUBST([STATIC_LINK_LDFLAGS],[-static]) 
else
  AC_SUBST([STATIC_LINK_LDFLAGS],[""])
fi

""")
                break



    ################################################################
    ################################################################

    def __subdir_paths(self,skip_leafs=False):
        p = []
        for d in self.subdirs:
            p.extend( self.subdirs[d].__subdir_paths() )
        if len( self.subdirs ) > 0:
            p.append( self.path_from_configure )
        return p;

    def __add_prefix_to_flags(self,fh):
        paths = [ r"-I\$(top_srcdir)/" + p for p in self.__subdir_paths() if p != "" ]
        fh.write( """AC_SUBST([AM_CPPFLAGS],["${AM_CPPFLAGS} %s"]) \n"""%(" ".join(paths)) )

        fh.write("""
if test "x$(eval echo $libdir)" = "xNONE/lib"; then
  if test -d $(eval echo ${prefix}/lib); then
     AC_SUBST([AM_LDFLAGS],["-L$(eval echo ${prefix}/lib) ${AM_LDFLAGS}"])
  fi
else
  AC_SUBST([AM_LDFLAGS],["-L$(eval echo ${libdir}) ${AM_LDFLAGS}"])
fi
if test "x$(eval echo ${includedir})" = "xNONE/include"; then
   if test -d $(eval echo ${prefix}/include); then
      AC_SUBST([AM_CPPFLAGS],["-I$(eval echo ${prefix}/include) ${AM_CPPFLAGS}"])
   fi
else
   AC_SUBST([AM_CPPFLAGS],["-I$(eval echo ${includedir}) ${AM_CPPFLAGS}"])
fi

""")



    ################################################################
    ################################################################

    def __test_deps(self,fh):
        for libname in reversed(self.all_child_deps):
            lib = self.all_child_deps[libname]
            fh.write("\n\n"+"#"*80+"\n")
            fh.write("### BEGIN CHECK FOR %s\n"%(libname))
            fh.write("#"*80+"\n\n")
            lib.ac_subst_var_serial( fh )
            fh.write("\n"+"#"*80+"\n")
            fh.write("### END CHECK FOR %s\n"%(libname))
            fh.write("#"*80+"\n\n")

            if lib.mpi.var != lib.serial.var:
                fh.write("\n\n"+"#"*80+"\n")
                fh.write("### BEGIN CHECK FOR %s MPI\n"%(libname))
                fh.write("#"*80+"\n\n")
                fh.write("if test \"x$with_mpi\" != \"xno\"; then\n\n")
                lib.ac_subst_var_mpi( fh )
                fh.write("\nfi\n")
                fh.write("\n"+"#"*80+"\n")
                fh.write("### END CHECK FOR %s MPI\n"%(libname))
                fh.write("#"*80+"\n\n")

            if lib.openmp.var != lib.serial.var:
                fh.write("\n\n"+"#"*80+"\n")
                fh.write("### BEGIN CHECK FOR %s OPENMP\n"%(libname))
                fh.write("#"*80+"\n\n")
                fh.write("if test \"x$with_openmp\" != \"xno\"; then\n\n")
                lib.ac_subst_var_openmp( fh )
                fh.write("\nfi\n")
                fh.write("\n"+"#"*80+"\n")
                fh.write("### END CHECK FOR %s OPENMP\n"%(libname))
                fh.write("#"*80+"\n\n")



    ################################################################
    ################################################################

    def __ac_output(self,fh):
        fh.write("""AC_SUBST([AM_CPPFLAGS],["-I\$(top_builddir) -I\$(top_srcdir) $AM_CPPFLAGS"])\n""")
        if self.recursive_make:
            fh.write("AC_CONFIG_FILES([Makefile %s])\n"%(" ".join( self.__getmakefiles() )))
        else:
            fh.write("AC_CONFIG_FILES([Makefile])\n")
        fh.write("AC_OUTPUT\n\n")



    ################################################################
    ################################################################

    def __autodel(self):
        if not os.path.exists(self.directory + "/ac-aux"):
            os.mkdir(self.directory + "/ac-aux")
        fname =  self.directory + "/ac-aux/autodel.sh"
        agen = file(fname,"w")
        agen.write("""#!/bin/bash
if [ -f Makefile ]; then
    make distclean
    rm Makefile
fi
rm -f *~ *.o *.la *.lo *.mod Doxyfile.bak doxygen-doc
rm -fr autom4te.cache aclocal.m4 config.guess config.sub depcomp install-sh configure ltmain.sh Makefile.in missing AUTHORS COPYING NEWS README ChangeLog config.log config.status libtool py-compile
rm -fr ./ac-aux
rm -f $(find . -name "*.pyc")
""")
        agen.close()
        st = os.stat(fname)
        os.chmod(fname, st.st_mode | stat.S_IEXEC)



    ################################################################
    ################################################################

    def __autogen(self):
        tar = self.name + "-" + self.version + ".tar.gz"
        if not os.path.exists(self.directory + "/ac-aux"):
            os.mkdir(self.directory + "/ac-aux")
        fname = self.directory + "/ac-aux/autogen.sh"
        agen = file(fname,"w")
        agen.write("""#!/bin/sh -e
maketar() {
    echo ""
    echo "make dist-gzip"
    make dist-gzip
    echo ""
    mkdir -p distrib
    if [ ! -f $1 ]; then
        echo "$1 does not exist; not copying to distrib/"
        rm $1
    else
        if [ ! -f distrib/$1 ]; then
            echo "mv -f  $1 distrib/"
            mv -f $1 distrib/
        else
            echo "tar -xzOf $1 | md5sum" "=" "$(tar -xzOf $1 | md5sum)"
            echo "tar -xzOf distrib/$1 " "=" "$(tar -xzOf distrib/$1 | md5sum)"
            if [ "$(tar -xzOf $1 | md5sum)" = "$(tar -xzOf distrib/$1 | md5sum)" ]; then
                echo "Not copying $1 to distrib/ because they are the same"
                rm $1
            else
                echo "cp -f  $1 distrib/"
                mv -f $1 distrib/
            fi
        fi
    fi
    echo ""
}

touch ./ac-aux/NEWS ./ac-aux/README ./ac-aux/AUTHORS ./ac-aux/ChangeLog
echo "Please refer to the following license files for information on copying: $(ls LICENSE*)" > COPYING
autoreconf -fvi #--force --install --verbose "$srcdir"
./configure $@
maketar %s
"""%(tar))
        agen.close()
        st = os.stat(fname)
        os.chmod(fname, st.st_mode | stat.S_IEXEC)



    ################################################################
    ################################################################

    def __make_sh(self):
        agen = file("make.sh","w")
        agen.write("""#!/bin/bash
set -e
set -u

PREFIX=$HOME/devel/local
OPENMP=--with-openmp

function numcores {
    awk -F: '/^physical/ && !ID[$2] { P++; ID[$2]=1 }; /^cpu cores/ { CORES=$2 };  END { print CORES*P }' /proc/cpuinfo
}

if [ $# -gt 1 ]; then
    echo "Error: You should specify at most one argument to avoid race-conditions"
    echo "./make"
    echo "./make debug"
    echo "./make clean"
    echo "./make doxygen-doc"
    echo "./make dist-gzip"
    echo "./make rm  (note: this delete's everything)"
    exit 1
fi

if [ $# -gt 0 ]; then
    if [ "$1" == "rm" ]; then
	if [ -e Makefile ]; then
	    make uninstall
	fi
	if [ -e ./ac-aux/autodel.sh ]; then
	    ./ac-aux/autodel.sh
	fi
	rm -fr ./ac-aux/autodel.sh ./ac-aux/autogen.sh configure.ac Makefile.am local
        exit
    fi
fi

if [ ! -e configure ]; then
    if [ ! -e configure.ac ]; then
	if [ -e __init__.py ]; then
	    ./__init__.py --prefix=$PREFIX $OPENMP
	fi
    fi
fi

if [ ! -e configure ]; then
    autoreconf -fvi
fi

if [ ! -e Makefile ]; then
    ./configure --prefix=$PREFIX $OPENMP
fi

if [ $# -gt 0 ]; then
    if [ "$1" == "opt" ] || [ "$1" == "debug" ]; then
	make $@ V=0 -j $(numcores)
	make install
    elif [ "$1" == "clean" ] || [ "$1" == "distclean" ]; then
	make uninstall
	make $@
    else
	make $@ -j $(numcores)
    fi
else
    make opt V=0 -j $(numcores)
    make install V=0
fi

""")
        agen.close()
        st = os.stat('make.sh')
        os.chmod('make.sh', st.st_mode | stat.S_IEXEC)


    ################################################################
    ################################################################

    def __root(self,root):
        """
        Recursively sets self.root = root for all compilable libs, progs, and packages
        """
        self.root = root
        for t in self.targets:
            if t.can_compile():
                t.root = root
                for dep in t.libs:
                    dep.root = None
            else:
                t.root = None
        for d in self.subdirs:
            self.subdirs[d].__root(root)

    def __path_from_configure(self):
        """
        Recursively removes the root directory from self.directory and
        stores it in self.path_from_configure
        """
        self.path_from_configure = RemoveBasePathFromFilePath(self.root.directory,self.directory)
        for t in self.targets:
            if t.can_compile() or isinstance(t,autoprog):
                t.path_from_configure = RemoveBasePathFromFilePath(self.root.directory,t.directory)
            else:
                t.path_from_configure = None
        for d in self.subdirs:
            self.subdirs[d].__path_from_configure()

    def __path_from_makefile(self):
        """
        Recursively removes the parent directory from 
        self.directory and stores it in self.path_from_makefile
        """
        if self.parent is None:
            self.path_from_makefile = ""
        else:
            self.path_from_makefile = RemoveBasePathFromFilePath(self.parent.directory,self.directory)
        for t in self.targets:
            if t.can_compile():
                t.path_from_makefile = RemoveBasePathFromFilePath(self.directory,t.directory)
            else:
                t.path_from_makefile = None
        for d in self.subdirs:
            self.subdirs[d].__path_from_makefile()


    def __all_child_targets(self):
        """
        Recursively set all_child_targets to all targets that
        are to be compiled (eventually) by this makefile or
        a sub-make of this makefile 
        """
        self.all_child_targets = ddict(str)
        for t in self.targets:
            if not t.name in self.all_child_targets:
                self.all_child_targets[t.name] = t
        for subdir in self.subdirs:
            d = self.subdirs[subdir]
            d.__all_child_targets()
            for name in d.all_child_targets:
                t = d.all_child_targets[name]
                self.all_child_targets[t.name] = t

    def __all_targets(self):
        """
        Recursively set all_targets to all targets that will
        be compiled as a part of this package, even if it
        is compiled elsewhere, e.g., a child or parent target
        """
        if self.parent is None:
            self.all_targets = self.all_child_targets
        else:
            self.all_targets = self.root.all_targets
        for t in self.targets:
            for i in range(len(t.libs)):
                if t.libs[i].name in self.all_targets:
                    t.libs[i] = self.all_targets[ t.libs[i].name ]
        for subdir in self.subdirs:
            self.subdirs[subdir].__all_targets()

    def __all_child_deps(self):
        """
        Recursively set all_child_deps, which are libraries
        that cannot be compiled anywhere, but are external
        dependencies of the package (as a whole).
        """
        self.all_child_deps = odict()
        for t in self.targets:
            for lib in t.libs:
                for dep in [lib] + RecursiveLibs(lib):
                    if not dep.can_compile():
                        self.all_child_deps[ dep.name ] = dep
        for subdir in self.subdirs:
            d = self.subdirs[subdir]
            d.__all_child_deps()
            for name in d.all_child_deps:
                dep = d.all_child_deps[name]
                if not dep.can_compile():
                    self.all_child_deps[ name ] = dep



    ################################################################
    ################################################################

    def __inspect_targets(self):
        """
        Sets
        self.has_library
        self.has_python_module
        self.has_program
        So configure.ac knows whether to LT_INIT
        and Makefile.am knows whether to set bin_PROGRAMS lib_LTLIBRARIES
        """
        self.has_library = False
        self.has_python_module = False
        self.has_program = False
        for t in self.all_targets:
            dep = self.all_targets[t]
            if isinstance(dep,autolib):
                self.has_library = True
                if dep.python_module:
                    self.has_python_module = True
            elif isinstance(dep,autoprog):
                self.has_program = True



    ################################################################
    ################################################################

    def __determine_languages(self):
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

        for t in self.all_targets:
            for s in self.all_targets[t].sources:
                if ".f90" == s[-4:] or ".F90" == s[-4:] \
                        or ".f" == s[-2:] or ".F" == s[-2:] \
                        or ".f77" == s[-4:] or ".F77" == s[-4:]:
                    self.has_fortran = True
                elif ".c" == s[-2:]:
                    self.has_c = True
                elif ".cpp" == s[-4:]:
                    self.has_cxx = True
            for s in self.all_targets[t].dist_bin_SCRIPTS + self.all_targets[t].python_package:
                if ".py" == s[-3:]:
                    self.has_python = True

    def __getmakefiles(self):
        """
        Recursively determine each Makefile that needs to be created.
        """
        am = []
        for d in self.subdirs:
            am.append( self.subdirs[d].path_from_configure + "/Makefile" )
        for d in self.subdirs:
            am += self.subdirs[d].__getmakefiles()
        return am












    # ################################################################
    # ################################################################

    # def __relativepath(self,path):
    #     """
    #     Removes the root directory from the path
    #     """
    #     common = os.path.commonprefix( [ self.root.directory, path ] )
    #     if len(common) > 0:
    #         rel = path.replace(common,"")
    #     else:
    #         rel = path
    #     if len(rel) > 0:
    #         if rel[0] == "/":
    #             rel = rel[1:]
    #     return rel

    # def __relativepathfromparent(self):
    #     """
    #     Removes the parent directory part from the path
    #     """
    #     path = self.directory
    #     if self.parent is not None:
    #         common = os.path.commonprefix( [ self.parent.directory, path ] )
    #         if len(common) > 0:
    #             rel = path.replace(common,"")
    #         else:
    #             rel = path
    #         if len(rel) > 0:
    #             if rel[0] == "/":
    #                 rel = rel[1:]
    #     else:
    #         rel = ""
    #     return rel




    # ################################################################
    # ################################################################




    # def __setrelativepath(self):
    #     """
    #     Recursively removes the root directory from self.directory and
    #     stores it in self.path
    #     It also removes the root directory from library.directory's
    #     This routine is called multiple times as the package is 
    #     built-up from subpackages, so the library.directory's will be the
    #     path to the source code relative to the nearest Makefile.am
    #     """
    #     self.path = self.__relativepath(self.directory)
    #     for t in self.targets:
    #         if t.can_compile:
    #             t.path = self.__relativepath(t.directory)
    #         else:
    #             t.path = None
    #     for d in self.subdirs:
    #         self.subdirs[d].__setrelativepath()


    # ################################################################
    # ################################################################

    # def __getmakefiles(self):
    #     """
    #     Recursively determine each Makefile that needs to be created.
    #     """
    #     am = []
    #     for d in self.subdirs:
    #         am.append(self.__relativepath(self.subdirs[d].directory)\
    #                       + "/Makefile")
    #     for d in self.subdirs:
    #         am += self.subdirs[d].__getmakefiles()
    #     return am




    ################################################################
    ################################################################

    # def __build_compilable_targets(self):
    #     """
    #     Recursively creates a dictionary self.compilable_targets,
    #     whose keys are the names of autolib classes and whose values
    #     are the autolib objects.  This is used to construct a unique
    #     list of libraries to be compiled
    #     """
    #     self.compilable_targets = ddict(str)
    #     for t in self.targets:
    #         if not t.name in self.compilable_targets:
    #             self.compilable_targets[t.name] = t
    #     for subdir in self.subdirs:
    #         d = self.subdirs[subdir]
    #         d.__build_compilable_targets()
    #         for dep in d.compilable_targets:
    #             lib = d.compilable_targets[dep]
    #             self.compilable_targets[lib.name] = lib
    #     self.compilable_children = copy.deepcopy( self.compilable_targets )





    ################################################################
    ################################################################

    # def __get_all_targets(self):
    #     a = []
    #     for t in self.targets:
    #         if t.name not in [ x.name for x in a ]:
    #             a.append(t)
    #     for subdir in self.subdirs:
    #         d = self.subdirs[subdir]
    #         this = d.__get_all_targets()
    #         names = [ x.name for x in this ]
    #         a = [ x for x in a if x.name not in names ] + this
    #     return a


    # ################################################################
    # ################################################################

    # def __get_all_deps(self):
    #     a = []
    #     for t in self.targets:
    #         for lib in t.libs:
    #             this = [lib] + RecursiveLibs(lib)
    #             names = [ x.name for x in this ]
    #             a = [ x for x in a if x.name not in names ] + this
    #     for subdir in self.subdirs:
    #         d = self.subdirs[subdir]
    #         this = d.__get_all_deps()
    #         names = [ x.name for x in this ]
    #         a = [ x for x in a if x.name not in names ] + this
    #     return a

    # def __set_compilable_deps(self):
    #     """
    #     If a library has a dependency on another library being
    #     compiled, then replace that dependency with a reference to
    #     an autolib object unique to the whole package.
    #     """
    #     for subdir in self.subdirs:
    #         self.subdirs[subdir].compilable_targets = \
    #             self.compilable_targets

    #     if self == self.root:
    #         self.uncompilable_deps = odict()
    #         self.all_libs = self.__get_all_deps()
    #         for lib in self.all_libs:
    #             if not lib.can_compile:
    #                 self.uncompilable_deps[lib.name] = lib
    #     else:
    #         self.all_libs = self.root.all_libs

    #     for t in self.targets:
    #         for i in range(len(t.libs)):
    #             if t.libs[i].name in self.compilable_targets:
    #                 t.libs[i] = self.compilable_targets[ t.libs[i].name ]

    #     for subdir in self.subdirs:
    #         self.subdirs[subdir].__set_compilable_deps()




