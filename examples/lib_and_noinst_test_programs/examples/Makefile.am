dist_noinst_SCRIPTS = autodel.sh autogen.sh
dist_bin_SCRIPTS =
EXTRA_DIST =
SUBDIRS = 
lib_LTLIBRARIES = 
noinst_LTLIBRARIES = 
pyexec_LTLIBRARIES = 
bin_PROGRAMS = 
noinst_PROGRAMS = 
EXTRA_DIST += LICENSE.fortran_example
EXTRA_DIST += LICENSE.pytdbsc
EXTRA_DIST += LICENSE.cxx_example
EXTRA_DIST += cxx/ade.xyz cxx/ade.2dbspl

noinst_PROGRAMS += cxx/cxx_example
cxx_cxx_example_CPPFLAGS =  $(AM_CPPFLAGS)
cxx_cxx_example_LDFLAGS = $(STATIC_LINK_LDFLAGS) $(AM_LDFLAGS)
cxx_cxx_example_LDADD = $(TDBSC_LIBS) $(FFTW3_LIBS) $(FCLIBS)
cxx_cxx_example_SOURCES = cxx/main.cpp cxx/pucker.cpp cxx/pucker.hpp


dist_noinst_SCRIPTS += python/python_example.py
EXTRA_DIST += python/ade.xyz python/ade.2dbspl

python_pytdbscdir = $(PWD)/python
python_pytdbsc_LTLIBRARIES = python/pytdbsc.la
python_pytdbsc_la_CPPFLAGS =    $(BOOST_CPPFLAGS) $(PYTHON_CPPFLAGS) $(AM_CPPFLAGS)
python_pytdbsc_la_LDFLAGS = -avoid-version -no-undefined -module    $(BOOST_LDFLAGS) $(PYTHON_LDFLAGS) $(PYTHON_EXTRA_LDFLAGS) $(AM_LDFLAGS)
python_pytdbsc_la_LIBADD = $(TDBSC_LIBS) $(FFTW3_LIBS) $(BOOST_PYTHON_LIB) $(PYTHON_EXTRA_LIBS) $(FCLIBS)
python_pytdbsc_la_SOURCES = python/exceptions.cpp python/pyiface.cpp python/pucker.cpp python/exceptions.hpp python/pucker.hpp

EXTRA_DIST += fortran/ade.xyz fortran/ade.2dbspl

noinst_PROGRAMS += fortran/fortran_example
fortran_fortran_example_CPPFLAGS =  $(AM_CPPFLAGS)
fortran_fortran_example_LDFLAGS = $(STATIC_LINK_LDFLAGS) $(AM_LDFLAGS)
fortran_fortran_example_LDADD = $(TDBSC_LIBS) $(FFTW3_LIBS) $(FCLIBS)
fortran_fortran_example_SOURCES = fortran/main.f90 fortran/puckermod.f90

fortran/puckermod.$(OBJEXT) : fortran/puckermod.f90
fortran/main.$(OBJEXT) : fortran/main.f90 fortran/puckermod.$(OBJEXT)


.PHONY: opt
opt: AM_MAKEFLAGS=CPPFLAGS="-DNDEBUG $(CPPFLAGS)" CFLAGS="$(OPT_CFLAGS)" FCFLAGS="$(OPT_FCFLAGS)" CXXFLAGS="$(OPT_CXXFLAGS)"
opt: AM_MAKEFLAGS+=$(if $(V),V=$(V),V=0 -s)
opt: all

.PHONY: debug
debug: AM_MAKEFLAGS=CFLAGS="$(DEBUG_CFLAGS)" FCFLAGS="$(DEBUG_FCFLAGS)" CXXFLAGS="$(DEBUG_CXXFLAGS)"
debug: AM_MAKEFLAGS+=$(if $(V),V=$(V),V=0 -s)
debug: all

# install-exec-hook:
#	To use this hook, set your package's self.install_exec_hook variable.  Be sure that each line starts with \t

clean-local:
	-rm -f *.mod

