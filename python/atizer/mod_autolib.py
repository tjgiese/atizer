#!/usr/bin/env python

from .utilities import *
from collections import defaultdict as ddict
from .f90deps import f90deps as f90deps
from .f90deps import printf90deps as printf90deps
from .f90deps import replace_ext as replace_ext
from .mod_autotarget import *

class autolib(autotarget):

    def __init__(self,name,directory=None):
        autotarget.__init__(self,name,directory)
        self.name = self.__class__.__name__
        # the location where header and module files should be
        # copied after compilation
        self.include = "$(includedir)/" + self.serial.name
        self.include_srcdir = self.directory
        self.python_module = False
        self.doxygen = True

    def is_a_python_module(self):
        self.python_module = True

    def ac_subst_var_serial(self,fh):
        raise Exception("autolib.ac_check undefined for class %s\n"%(\
                self.__class__.__name__))

    def ac_subst_var_openmp(self,fh):
        if len(self.openmp.var) > 0 and len(self.serial.var) > 0:
            fh.write("AC_SUBST([%s],[$%s])\n"%(\
                    self.openmp.var,self.serial.var))

    def ac_subst_var_mpi(self,fh):
        if len(self.mpi.var) > 0 and len(self.serial.var) > 0:
            fh.write("AC_SUBST([%s],[$%s])\n"%(\
                    self.mpi.var,self.serial.var))


    def am_write(self,fh=None):
        """
        Writes the contents of a Makefile.am to a file handle
        If no file handle is given, then it is written to Makefile.am
        """
        if fh == None: fh = open("Makefile.am","w")
        self.determine_languages()
        am_name = "lib%s"%(self.serial.name)
        if not self.recursive_make:
            am_name = UnderscorePath( self.path_from_configure ) + am_name
        libs    = RecursiveLibs(self)
        serials = [(dep,dep.serial) for dep in libs]
        openmps = [(dep,dep.openmp) for dep in libs]
        mpis    = [(dep,dep.mpi)    for dep in libs]
        ssource = ["$(%s_la_SOURCES)"%(am_name)]

        if len(self.dist_noinst_SCRIPTS) > 0:
            if self.recursive_make:
                fh.write("dist_noinst_SCRIPTS += %s\n"%(
                        " ".join(self.dist_noinst_SCRIPTS)))
            else:
                fh.write("dist_noinst_SCRIPTS += %s\n"%(
                        " ".join(PrependPathToFiles(self.path_from_configure,self.dist_noinst_SCRIPTS))))

        if len(self.EXTRA_DIST) > 0:
            if self.recursive_make:
                fh.write("EXTRA_DIST += %s\n"%(
                        " ".join(self.EXTRA_DIST)))
            else:
                fh.write("EXTRA_DIST += %s\n"%(
                        " ".join(PrependPathToFiles(self.path_from_configure,self.EXTRA_DIST))))

        if len(self.sources + self.headers) > 0:

            f90depinfo = f90deps( self.sources, self.directory )
            
            
            if self.recursive_make:
                sources = PrependPathToFiles( self.path_from_makefile, self.sources + self.headers )
            else:
                sources = PrependPathToFiles( self.path_from_configure, self.sources + self.headers )
            self.__am_write(fh,self.serial,serials,sources)
            if self.openmp.name != self.serial.name:
                fh.write("\nif WITH_OPENMP\n")
                self.__am_write(fh,self.openmp,openmps,ssource)


                fh.write("\nendif\n\n")
            if self.mpi.name != self.serial.name:
                fh.write("\nif WITH_MPI\n")
                self.__am_write(fh,self.mpi,mpis,ssource)
                fh.write("\nendif\n\n")


        # create the header include directories
        if not self.python_module:
            hdirs = ddict( list )
            for h in self.headers:
                if os.path.isfile( self.directory + "/" + h ):
                    
                    hdir = os.path.abspath(self.directory + "/" + h )
                    hdir_old = hdir
                    hdir = os.path.dirname(hdir).replace(os.path.abspath(self.include_srcdir),"")
                    if len(hdir) > len(hdir_old):
                        raise Exception("header "+h+" has to be (but is not) within (or within a subdirectory of) "+os.path.dirname(self.include_srcdir))

                    hdir = hdir.lstrip(r"/")
                else:
                    print("Error locating header")
                    print("h   =",h)
                    print("path=",os.path.abspath(h))
                    print("exis?",os.path.isfile( os.path.abspath(h) ))
                    print("fdir=",fdir)
                    print("sdir=",sdir)
# remove the directory from the path to the header
                    raise Exception("Hmpf")
                hdirs[hdir].append(h)
            for hdir in hdirs:
                #print "________________",hdir,"_________________"
                pref = "%s_%s"%(\
                    am_name,hdir.replace("/","",128))
                fh.write("%s_pkgincludedir = %s\n"%(\
                        pref,self.include+"/"+hdir ))
                if self.recursive_make:
                    fh.write("%s_pkginclude_HEADERS = %s\n"%(\
                            pref," ".join(hdirs[hdir]) ))
                else:
                    fh.write("%s_pkginclude_HEADERS = %s\n"%(\
                            pref," ".join(PrependPathToFiles(self.path_from_configure,hdirs[hdir])) ))
 
        if self.recursive_make:
            fh.write("\n")
            fh.write( printf90deps( f90depinfo, None, "lo" ) )
        else:
            fh.write("\n")
            fh.write( printf90deps( f90depinfo, self.path_from_configure, "lo" ) )


        fh.write("\n\nBUILT_SOURCES += ")
        for src in f90depinfo:
            #print("src %s provides %s"%(src,[mod for mod in f90depinfo[src].provides]))
            for mod in f90depinfo[src].provides:
                m = replace_ext( mod.lower(), ".mod" )
                fh.write(" "+m)
        fh.write("\n\n\n")
        for src in f90depinfo:
            for mod in f90depinfo[src].provides:
                m = replace_ext( mod.lower(), ".mod" )
                fh.write(m + " ")
            if self.recursive_make:
                f = src
            else:
                f = self.path_from_configure + "/" + src
            o = replace_ext( f, ".lo" ).lstrip(r"/") #.replace(r"/","_")
            #o = ( self.path_from_configure + "/" + o ).lstrip(r"/")
            if len( f90depinfo[src].provides ) > 0:
                fh.write( " : " + o )
                for mod in f90depinfo[src].uses:
                    m = replace_ext( mod.lower(), ".mod" )
                    fh.write(" " + m)
                fh.write("\n")
        # print the extra make rules
        fh.write("%s\n"%(self.extra_make_rules))
#-fsyntax-only


    def __am_write(self,fh,lib,deps,sources):
        fh.write("\n")
        name = "lib%s"%(lib.name)
        if self.python_module:
            name = lib.name
        target = name
        if not self.recursive_make:
            target = PrependPathToFiles( self.path_from_configure, [name] )[0]
            name = UnderscorePath( self.path_from_configure ) + name

        infos = [ info for dep,info in deps ]
        cppflags = lib.cppflags + " " + " ".join( [ dep.cppflags for dep in infos ] ) 
        ldflags  = lib.ldflags + " " + " ".join( [ dep.ldflags  for dep in infos ] ) 

        self.query_compiles_an_openmp_target()
        if self.compiles_an_openmp_target and self.openmp.var == self.serial.var and not self.python_module:
            raise Exception("library "+self.name+" has openmp source code, but the class constructor did not specify self.enable_openmp().  Although I *could* do this for you now (because we have the source code and are compiling it), this will cause problems for you when you try to link to this library from some other source that isn't compiling this library (in that case, I *can't* correct this for you).  The solution is to go back and edit your library class' __init__ by adding the line self.enable_openmp()")


        if self.noinst:
            if self.python_module:
                raise Exception("library "+lib.name+" is a python module, so you shouldn't set self.noinst")
            fh.write("noinst_LTLIBRARIES += %s.la\n"%( target ))
        elif self.install_here:
            if self.recursive_make:
                fh.write("%sdir = $(PWD)\n"%( name ))
            else:
                fh.write("%sdir = $(PWD)/%s\n"%( name, self.path_from_configure ))
            fh.write("%s_LTLIBRARIES = %s.la\n"%( name,target ))
        elif self.python_module:
            fh.write("pyexec_LTLIBRARIES += %s.la\n"%( target ))
        else:
            fh.write("lib_LTLIBRARIES += %s.la\n"%( target ))


        fh.write("%s_la_CPPFLAGS = %s $(AM_CPPFLAGS)\n"%(\
                name, cppflags )) #lib.cppflags ))

        if len(lib.cflags) > 0:
            fh.write("%s_la_CFLAGS = %s\n"%(\
                    name,lib.cflags))
        if len(lib.cxxflags) > 0:
            fh.write("%s_la_CXXFLAGS = %s\n"%(\
                    name,lib.cxxflags))
        if len(lib.fcflags) > 0:
            fh.write("%s_la_FCFLAGS = %s\n"%(\
                    name,lib.fcflags))


        if self.apiversion is not None and not self.python_module:
            fh.write("%s_la_LDFLAGS = -version-info %s -no-undefined %s $(AM_LDFLAGS)\n"%(\
                    name,self.apiversion,ldflags ))
        elif self.python_module:
            fh.write("%s_la_LDFLAGS = -avoid-version -no-undefined -module %s $(AM_LDFLAGS)\n"%( name, ldflags ))
        else:
            fh.write("%s_la_LDFLAGS = -avoid-version -no-undefined %s $(AM_LDFLAGS)\n"%( name, ldflags ))



        is_mixed_lang = False
        if self.has_fortran:
            if self.has_c or self.has_cxx:
                is_mixed_lang = True
        if len(deps) == 0 and not is_mixed_lang:
            fh.write("#")

        fh.write("%s_la_LIBADD ="%(name))
        for dep,info in deps:
            if dep.can_compile():
                fh.write(" $(top_builddir)/%s/lib%s.la"%(\
#                        dep.path,info.name))
                        dep.path_from_configure,info.name))
            else:
                if len(info.var) > 0:
                    fh.write(" $(%s)"%( info.var ))
        fh.write(" $(FCLIBS)\n")
# libygxx_la_LDFLAGS = -version-info $(YGXX_SO_VERSION) $(AM_LDFLAGS)
        fh.write("%s_la_SOURCES = %s\n"%(\
                name, " ".join(sources) ))

