#!/usr/bin/env python

from .utilities import *
from .f90deps import f90deps as f90deps
from .f90deps import printf90deps as printf90deps
from .f90deps import replace_ext as replace_ext
from .mod_autotarget import *

class autoprog(autotarget):

    def __init__(self,name,directory=None):
        autotarget.__init__(self,name,directory)
        self.name = self.__class__.__name__
        if name is not None:
            self.name = name

    def am_write(self,fh=None):
        """
        Writes the contents of a Makefile.am to a file handle
        If no file handle is given, then it is written to Makefile.am
        """
        if fh == None: fh = file("Makefile.am","w")
        self.determine_languages()
        self.query_links_to_an_openmp_target()

        if ( self.compiles_an_openmp_target or self.links_to_an_openmp_target ) and self.openmp.var == self.serial.var:
            self.enable_openmp()

        am_name = "%s"%(self.serial.name).replace("-","_")
        if not self.recursive_make:
            am_name = UnderscorePath( self.path_from_configure ) + am_name

        libs = RecursiveLibs(self)
        serials = [(dep,dep.serial) for dep in libs]
        openmps = [(dep,dep.openmp) for dep in libs]
        mpis    = [(dep,dep.mpi)    for dep in libs]
        ssource = ["$(%s_SOURCES)"%(am_name)]

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


        dirs = dict_by_directory( self.python_package )
        if self.recursive_make:
            if len(self.dist_bin_SCRIPTS) > 0:
                fh.write("dist_bin_SCRIPTS += %s\n"%(
                        " ".join(self.dist_bin_SCRIPTS)))
            for d in dirs:
                name = re.sub(r"/",r"_",d)
                fh.write("%sdir = $(pythondir)/%s\n"%(name,d))
                fh.write("%s_PYTHON = %s\n"%(name," ".join(dirs[d]) ))
        else:
            if len(self.dist_bin_SCRIPTS) > 0:
                fh.write("dist_bin_SCRIPTS += %s\n"%(
                        " ".join(PrependPathToFiles(self.path_from_configure,self.dist_bin_SCRIPTS))))
            for d in dirs:
                name = re.sub(r"/",r"_",d)
                fh.write("%sdir = $(pythondir)/%s\n"%(name,d))
                fh.write("%s_PYTHON = %s\n"%(name," ".join(PrependPathToFiles(self.path_from_configure,dirs[d])) ))


        if len(self.sources + self.headers) > 0:
            f90depinfo = f90deps( self.sources, self.directory )
            if self.recursive_make:
                sources = PrependPathToFiles( self.path_from_makefile, self.sources + self.headers )
            else:
                sources = PrependPathToFiles( self.path_from_configure, self.sources + self.headers )


            if self.has_python_embed:
                fh.write("\nif PYTHON_USE\n")
            self.__am_write(fh,self.serial,serials,sources)
            if self.openmp.name != self.serial.name:
                fh.write("\nif WITH_OPENMP\n")
                self.__am_write(fh,self.openmp,openmps,ssource)
                fh.write("\nendif\n\n")
            if self.mpi.name != self.serial.name:
                fh.write("\nif WITH_MPI\n")
                self.__am_write(fh,self.mpi,mpis,ssource)
                fh.write("\nendif\n\n")
            if self.has_python_embed:
                fh.write("\nendif\n")

        fh.write( "\n" )

        if len(self.sources + self.headers) > 0:

            if self.has_python_embed:
                fh.write("\nif PYTHON_USE\n")
                
            if self.recursive_make:
                #            fh.write( printf90deps( f90deps( self.sources, self.directory ) ) )
                fh.write( printf90deps( f90depinfo, None ) )
            else:
                #            fh.write( printf90deps( f90deps( self.sources, self.directory ), self.path_from_configure ) )
                fh.write( printf90deps( f90depinfo, self.path_from_configure ) )

            fh.write("\n\nBUILT_SOURCES += ")
            for src in f90depinfo:
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
                f = replace_ext( f, ".$(OBJEXT)" ).lstrip(r"/")
                if len( f90depinfo[src].provides ) > 0:
                    fh.write(" : " + f + "\n")

            if self.has_python_embed:
                fh.write("\nendif\n")
                
        # print the extra make rules
        fh.write("%s\n"%(self.extra_make_rules))



    def __am_write(self,fh,prog,deps,sources):
        target = prog.name
        am_name = prog.name.replace("-","_")
        if not self.recursive_make:
            target = PrependPathToFiles( self.path_from_configure, [target] )[0]
            am_name = UnderscorePath( self.path_from_configure ) + am_name

            
        fh.write("\n")
        if self.noinst:
            fh.write("noinst_PROGRAMS += %s\n"%( target ))
#        elif self.install_here:
#            fh.write("%sdir = $(PWD)\n"%(prog.name))
#            fh.write("%s_PROGRAMS = %s\n"%( prog.name, prog.name ))
        else:
#            if "_mpi" in target:
#               fh.write("bin_PROGRAMS  = %s\n"%( target ))
#            else:
            fh.write("bin_PROGRAMS += %s\n"%( target ))
        fh.write("%s_CPPFLAGS = %s $(AM_CPPFLAGS)\n"%(\
                am_name,prog.cppflags ))
        if len(prog.cflags) > 0 or self.has_python_embed:
            cflags = prog.cflags
            if self.has_python_embed:
                cflags += " $(PYTHON_CSPEC)"
            fh.write("%s_CFLAGS = %s\n"%(am_name,cflags))
        if len(prog.cxxflags) > 0 or self.has_python_embed:
            cxxflags = prog.cxxflags
            if self.has_python_embed:
                cxxflags += " $(PYTHON_CSPEC)"
            fh.write("%s_CXXFLAGS = %s\n"%(am_name,cxxflags))
        if len(prog.fcflags) > 0 or self.has_python_embed:
            fcflags = prog.fcflags
            if self.has_python_embed:
                fcflags += " $(PYTHON_CSPEC)"
            fh.write("%s_FCFLAGS = %s\n"%(am_name,fcflags))

        ldflags = "$(STATIC_LINK_LDFLAGS) $(AM_LDFLAGS)"
        if self.has_python_embed:
            ldflags = "$(AM_LDFLAGS) $(PYTHON_LSPEC)"
        fh.write("%s_LDFLAGS = %s\n"%( am_name, ldflags ))

        is_mixed_lang = False
        if self.has_fortran:
            if self.has_c or self.has_cxx:
                is_mixed_lang = True
        if len(deps) == 0 and not is_mixed_lang:
            fh.write("#")
        flags = []
        for dep,info in deps:
            if dep.can_compile():
#                print "dep.parent",dep.parent.path
                flags.append(\
                    "$(top_builddir)/%s/lib%s.la"%(\
#                        dep.path,info.name ) )
#                        dep.parent.path,info.name ) )
                        dep.path_from_configure,info.name ) )
            else:
                flags.append( "$(%s)"%(info.var) )

        fh.write("%s_LDADD = %s $(FCLIBS)\n"%(\
                am_name, " ".join(flags) ))

        fh.write("%s_SOURCES = %s\n"%(\
                am_name, " ".join(sources) ))


