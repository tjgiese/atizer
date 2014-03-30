#!/usr/bin/env python

import re,sys,os,copy
from collections import defaultdict as ddict


class f90depinfo(object):
    def __init__(self):
        self.uses = ddict()
        self.provides = ddict()

def getline( liter ):
    line = ""
    while len(line.strip()) < 1:
        line = liter.next().upper()
        line = re.sub(r"^(.*?)!.*$",r"\1",line)
    line = re.sub(r"ONLY.*$","",line)
    line = line.strip()
    if line[-1] == "&":
        line += getline( liter )
    line = re.sub(r"&","",line)
    return line

def replace_ext(name,ext):
    fileName, fileExtension = os.path.splitext(name)
    return fileName + ext

def f90deps(srcs,directory=None):

    files = []
    exts = [ ".f90", ".F90", ".F", ".f", ".f77", ".f03", ".F03", ".f08", ".F08" ]
    for src in srcs:
        fileName, fileExtension = os.path.splitext(src)
        if fileExtension in exts:
            files.append(src)
    srcs = files

    use_line_re  = re.compile(r"^\s*use\s+(\S.+)\s*$",re.IGNORECASE)
    mod_line_re  = re.compile(r"^\s*module\s+(\S+)\s*$",re.IGNORECASE)
    cont_line_re = re.compile(r"^(.*)&\s*$")
    split_re = re.compile(r"\s*,\s*")
    dep_re   = re.compile(r"(.*)")
    mod_re   = re.compile(r"(.*)")

    info = ddict()
    for src in srcs:
        info[src] = f90depinfo()
        if directory is not None and directory != "":
            fh = file(directory + "/" + src,"r")
        else:
            fh = file(src,"r")

        liter = iter(fh)
        while True:
            try:
                line = getline(liter)
                
                has_use = re.match( use_line_re, line )
                has_mod = re.match( mod_line_re, line )
                if has_use is not None:
                    for mod in has_use.group(1).split(","):
                        info[src].uses[ mod.strip() ] = None
                elif has_mod is not None:
                    info[src].provides[ has_mod.group(1).strip() ] = None
            except Exception as e:
#                print "exception: ",e
                break
    modules = ddict()
    for src in srcs:
        for m in info[src].provides:
            modules[m] = src
    for src in srcs:
        tmp = copy.deepcopy( info[src].uses )
        for m in info[src].uses:
            if not m in modules:
                tmp.pop(m,None)
            else:
                tmp[m] = modules[m]
        for m in info[src].provides:
            if m in tmp:
                tmp.pop(m,None)
        info[src].uses = tmp
    return info

def printf90deps(info,directory=None,extension="$(OBJEXT)",fileprefix=""):
    result = ""
    for src in info:
        fname = src
        oname = src
        if directory is not None:
            fname = ("/".join([directory,src])).replace(r"//",r"/").lstrip(r"/")
            p,f = os.path.split(fname)
            oname = p + "/" + fileprefix + f
#        print src,directory,oname

            #oname = ("/".join([directory,re.sub(r"/","_",fname)])).replace(r"//",r"/")  # if AM_INIT_AUTOMAKE([subdir-objects])
            #oname = fname
        result += replace_ext(oname,"." + extension) + " : " + fname
        for m in info[src].uses:
            oname = info[src].uses[m]
            if directory is not None:
                oname = ("/".join([directory,oname])).replace(r"//",r"/").lstrip(r"/") # if AM_INIT_AUTOMAKE([subdir-objects])
                p,f = os.path.split(oname)
                oname = p + "/" + fileprefix + f
            
            result += " " + replace_ext( oname, "." + extension )
        result += "\n"
    return result

if __name__ == "__main__":
    print printf90deps( f90deps(sys.argv[1:]), None, "o" )
