#!/usr/bin/env python

import os,fnmatch,sys,copy,re
from collections import defaultdict as ddict
import pwd

class serialinfo(object):
    def __init__(self,name):
        self.name = "".join( name.lower() )
        # this is the environmental variable holding the -l flags
        # that is used by other libraries when linking to this library
        self.var = self.name.upper() + "_LIBS"
        self.var_default_value = "-l"+self.name
        # these are flags used when this library is NOT being compiled
        # i.e., something else is using this library as a dependency
        self.cppflags = ""
        self.ldflags = ""
        # this flags are used when this library IS being compiled
        self.cflags = ""
        self.cxxflags = ""
        self.fcflags = ""


class openmpinfo(object):
    def __init__(self,name):
        self.name = "".join( name.lower() )+"_omp"
        # this is the environmental variable holding the -l flags
        # that is used by other libraries when linking to this library
        self.var = self.name.upper() + "_OPENMP_LIBS"
        self.var_default_value = "-l"+self.name
        # these are flags used when this library is NOT being compiled
        # i.e., something else is using this library as a dependency
        self.cppflags = "-DWITH_OPENMP"
        self.ldflags = ""
        # this flags are used when this library IS being compiled
        self.cflags = "$(OPENMP_CFLAGS)"
        self.cxxflags = "$(OPENMP_CXXFLAGS)"
        self.fcflags = "$(OPENMP_FCFLAGS)"

class mpiinfo(object):
    def __init__(self,name):
        self.name = "".join( name.lower() )+"_mpi"
        # this is the environmental variable holding the -l flags
        # that is used by other libraries when linking to this library
        self.var = self.name.upper() + "_MPI_LIBS"
        self.var_default_value = "-l"+self.name
        # these are flags used when this library is NOT being compiled
        # i.e., something else is using this library as a dependency
        #self.cppflags = "-DMPI"
        self.cppflags = "-DWITH_MPI"
        self.ldflags = ""
        # this flags are used when this library IS being compiled
        self.cflags = ""
        self.cxxflags = ""
        self.fcflags = ""




def recursive_find(wildcard,topdir):
    """
    This is like a recursive glob starting from a top-level directory
    recursive_find("*.c","src/")
    returns src/*.c src/*/*.c src/*/*/*.c ... etc
    """
    matches = []
    for root, dirnames, filenames in os.walk(topdir):
        for filename in fnmatch.filter(filenames, wildcard):
            fname = os.path.join(root, filename)
            if "distrib/" not in fname:
                matches.append(fname)
    return matches



def recursive_find_any_of(wildcards,topdir):
    """
    This is a recursive glob for multiple wildcards, e.g.,
    recursive_find_any_of(["*.c","*.cpp"],"src/")
    returns src/*.c src/*.cpp src/*/*.c src/*/*.cpp ... etc
    """
    matches = []
    for root, dirnames, filenames in os.walk(topdir):
        for wildcard in wildcards:
            for filename in fnmatch.filter(filenames, wildcard):
                fname = os.path.join(root, filename)
                if "distrib/" not in fname:
                    matches.append(fname)
    return matches



# def extract_package(directory):
#     """
#     Opens directory/config.py, and imports a global variable
#     called "package."
#     config.py should therefore look something like

#     #!/usr/bin/env python
#     from atizer import *
#     package = autopackage("name", [ libfoo( here()+"/src" ) ], [] )
#     """
#     if not os.path.isdir(directory):
#         raise Exception("directory "+directory+" does not exist")
#     subpackage = None
#     config = None
#     sys.path.insert(0, directory)
#     print "...Extracting",directory,"using path:\n"
#     print sys.path
#     print ""
#     import config
#     subpackage = None
#     config = reload(config)
#     from config import package as subpackage
#     import copy
#     sp = copy.deepcopy(subpackage)
#     subpackage = None
#     del sys.path[0]
#     print ""
#     print "...Finished extracting",directory,"named",sp.name,"whose path is",sp.directory,"; PYTHONPATH exists as:\n"
#     print sys.path
#     print ""
#     return sp



          

def RecursiveLibs(self):
    a = []
    for lib in self.libs:
        this = [ lib ] + RecursiveLibs( lib )
        names = [ x.name for x in this ]
        a = [ x for x in a if not x.name in names ] + this
    return a

def GetOptionalDictFromLib(self,names):
    if not self.optional or self.name not in names:
        names[self.name] = self.optional
    for lib in self.libs:
        names = GetOptionalDictFromLib(lib,names)
    return names

#def SetOptionalFlags(self):
#    names = GetOptionalDict(self,{})
#    self.set_optional_recursively(names)

def GetOptionalDictFromTarget(self,names):
    for t in self.targets:
        if t.optional:
            t.set_optional_recursively(True)
        names = GetOptionalDictFromLib(t,names)
    for subdir in self.subdirs:
        d = self.subdirs[subdir]
        names = GetOptionalDictFromTarget(d,names)
    return names



def RemoveBasePathFromFilePath(basepath,filepath):
    """
    Removes the base-path from the file-path
    """
    common = os.path.commonprefix( [ basepath, filepath ] )
    if len(common) > 0:
        rel = filepath.replace(common,"")
    else:
        rel = filepath
    if len(rel) > 0:
        if rel[0] == "/":
            rel = rel[1:]
    return rel

def PrependPathToFiles(path,files):
    a = copy.deepcopy(files)
    if path is not None:
        if len(path) > 0:
            if len(path) > 1 and path[-1] == "/":
                a = [ path + f for f in a ]
            else:
                a = [ path + "/" + f for f in a ]
    return a

def UnderscorePath(path):
    s = re.sub(r"/","_",path) + "_"
    s = s.lstrip("_")
    return s


# def RecursiveSerialDepFlags(self):
#     flags = []
#     for dep in self.libs:
#         libdeps = []
#         if dep.can_compile:
#             libdeps.append( "$(top_builddir)/%s/lib%s.la"%(dep.path,dep.lib_serial) )
#         else:
#             libdeps.append( "$(%s)"%(dep.var_serial) )
#         libdeps.extend( RecursiveSerialDepFlags(dep) )
#         flags = [ flag for flag in flags if not flag in libdeps ]
#         flags.extend( libdeps )
#     return flags

# def RecursiveOpenMPDepFlags(self):
#     flags = []
#     for dep in self.libs:
#         libdeps = []
#         if dep.can_compile:
#             libdeps.append( "$(top_builddir)/%s/lib%s.la"%(dep.path,dep.lib_openmp) )
#         else:
#             libdeps.append( "$(%s)"%(dep.var_openmp) )
#         libdeps.extend( RecursiveOpenMPDepFlags(dep) )
#         flags = [ flag for flag in flags if not flag in libdeps ]
#         flags.extend( libdeps )
#     return flags


# def RecursiveMPIDepFlags(self):
#     flags = []
#     for dep in self.libs:
#         libdeps = []
#         if dep.can_compile:
#             libdeps.append( "$(top_builddir)/%s/lib%s.la"%(dep.path,dep.lib_mpi) )
#         else:
#             libdeps.append( "$(%s)"%(dep.var_mpi) )
#         libdeps.extend( RecursiveMPIDepFlags(dep) )
#         flags = [ flag for flag in flags if not flag in libdeps ]
#         flags.extend( libdeps )
#     return flags



def dict_by_directory(files):
    d = ddict( list )
    for pf in files:
        p,f = os.path.split(pf)
        d[p].append( pf )
    return d

def get_user_fullname():
    return pwd.getpwuid(os.getuid()).pw_gecos.split(",")[0]
