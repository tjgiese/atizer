#!/usr/bin/env python
import os
from ..utilities import RecursiveLibs

__ALREADY_PRINTED_MACRO = []



def ax_macro(ax_filename):
    data = "\n"
    if not ax_filename in __ALREADY_PRINTED_MACRO:
        with open (os.path.dirname(__file__)+"/m4/"+ax_filename, "r") as myfile:
            data=myfile.read().replace("#serial ","### serial ")
        __ALREADY_PRINTED_MACRO.append(ax_filename)
    return data



def m4_generic_cxx_serial_conftest(self,fh,header,preamble,body):
    var  = self.serial.var
    var_default = self.serial.var_default_value
    name = self.name

    if var in __ALREADY_PRINTED_MACRO:
        return
    else:
        __ALREADY_PRINTED_MACRO.append(var_default)

    # FOO_LIB=-lfoo
    fh.write(
        m4_define_new_env(
            var,var_default,"Serial "+name+" libraries") )
    # foo/foo.hpp
    if header is not None:
        fh.write( m4_check_header_or_die(header,name) )

    # function foo in -lfoo
    fh.write(
        m4_checking(
            "serial compilation linked to $(eval echo ${"+var+"})"))


    linkage = "${" + var + "}"
    for name in [dep.serial.var for dep in RecursiveLibs(self)]:
        linkage += " ${"+name+"}"

    fh.write(
        m4_cxx_serial_test(
            linkage,
#            "${"+var+"}", # link to these libraries
            preamble, # header
            body) # body
        +
        m4_if_failed( 
            m4_error("""

FAILED TO LINK AGAINST ${"""+var+"""}

This may mean that the library is installed in a nonstandard location
or are not installed anywhere.  You need to locate them or install
them.  If you configured with --enable-static-link, then it may mean
you have the shared library, e.g., libfoo.so, but are missing the
archive file, e.g., libfoo.a

    If you can locate the libraries in /path/to/lib/, then you can
    reconfigure with
    ./configure LDFLAGS="-L/path/to/lib \$LDFLAGS"

    On some supercomputers, you may have to "module load" a package to
    make it available for use.  
    Type "module list" to see a list of loadable modules.
    Upon loading a module, you can use "module show" to help find
    the appropriate /path/to/lib
""") ) )

#            m4_error(
#                "Link tests failed against "+name)) )



def m4_generic_cxx_openmp_conftest(self,fh,header,preamble,body):
    var  = self.openmp.var
    var_default = self.openmp.var_default_value
    name = self.name
    #lib  = self.lib_openmp

    if var in __ALREADY_PRINTED_MACRO:
        return
    else:
        __ALREADY_PRINTED_MACRO.append(var_default)

    # FOO_LIB=-lfoo
    fh.write(
        m4_define_new_env(
            var,var_default,"OpenMP "+name+" libraries") )
    # foo/foo.hpp
    if header is not None:
        fh.write( m4_check_openmp_header_or_die(header,name) )

    # function foo in -lfoo
    fh.write(
        m4_checking(
            "OpenMP compilation linked to $(eval echo ${"+var+"})"))


    linkage = "${" + var + "}"
    for name in [dep.openmp.var for dep in RecursiveLibs(self)]:
        linkage += " ${"+name+"}"

    fh.write(
        m4_cxx_openmp_test(
#            "${"+var+"}", # link to these libraries
            linkage,
            preamble, # header
            body) # body
        +
        m4_if_failed(
             m4_error("""

FAILED TO LINK AGAINST ${"""+var+"""}

This may mean that the library is installed in a nonstandard location
or are not installed anywhere.  You need to locate them or install
them.  If you configured with --enable-static-link, then it may mean
you have the shared library, e.g., libfoo.so, but are missing the
archive file, e.g., libfoo.a

    If you can locate the libraries in /path/to/lib/, then you can
    reconfigure with
    ./configure LDFLAGS="-L/path/to/lib \$LDFLAGS"

    On some supercomputers, you may have to "module load" a package to
    make it available for use.  
    Type "module list" to see a list of loadable modules.
    Upon loading a module, you can use "module show" to help find
    the appropriate /path/to/lib
""") ) )



def m4_result(msg):
    return "AC_MSG_RESULT([%s])"%(msg)



def m4_warning(msg):
    return "AC_MSG_WARNING([%s])"%(msg)



def m4_error(msg):
    return "AC_MSG_ERROR([%s])"%(msg)



def m4_checking(msg):
    return "AC_MSG_CHECKING([%s])"%(msg)



def m4_test_ok():
    return m4_result("yes") + "\n" + m4_clear_failed()



def m4_test_failed():
    return m4_result("no") + "\n" + m4_set_failed()



def m4_clear_failed():
    return "atp_test_failed=no"



def m4_set_failed():
    return "atp_test_failed=yes"



def m4_if_failed(do_if_failed):
    return """AS_IF( [test "x$atp_test_failed" != "xno"],
[
%s
]) dnl failbit was on
"""%(do_if_failed)



def m4_save_flags(extra_flags=""):
    return """
saved_CFLAGS="$CFLAGS"
saved_FCFLAGS="$FCFLAGS"
saved_CXXFLAGS="$CXXFLAGS"
saved_CPPFLAGS="$CPPFLAGS"
saved_LDFLAGS="$LDFLAGS"
saved_LIBS="$LIBS"
CPPFLAGS+=" $AM_CPPFLAGS"
LDFLAGS+=" $AM_LDFLAGS"
""" + extra_flags




def m4_restore_flags():
    return """
CFLAGS=$saved_CFLAGS
FCFLAGS=$saved_FCFLAGS
CXXFLAGS=$saved_CXXFLAGS
CPPFLAGS=$saved_CPPFLAGS
LDFLAGS=$saved_LDFLAGS
LIBS=$saved_LIBS

"""



def m4_define_new_env(var,value,msg):
    return """
AC_ARG_VAR(%s,%s (default); %s)
if test "x$%s" = "x"; then
   %s="%s"
   AC_SUBST([%s])
fi

"""%(var,value,msg,
     var,var,value,var)


def m4_check_openmp_header(header,ok="",fail=""):
    return m4_check_header(header,ok,fail,"""
CFLAGS="$CFLAGS $OPENMP_CFLAGS"
CXXFLAGS="$CXXFLAGS $OPENMP_CXXFLAGS"
FFLAGS="$FFLAGS $OPENMP_FFLAGS"
""")


def m4_check_header(header,ok="",fail="",extra_flags=""):
    return m4_save_flags(extra_flags) \
        + "AC_LANG_PUSH([C++])\n" \
        + """
AC_CHECK_HEADER(
  [%s],
  [
%s
  ], dnl AC_CHECK_HEADER ok
  [
%s
  ] dnl AC_CHECK_HEADER failed
) dnl AC_CHECK_HEADER
"""%(header,ok,fail) \
        + "AC_LANG_POP([C++])\n" \
        + m4_restore_flags()



def m4_check_header_or_die(header,libname,yum=None,deb=None):
    helper = ""
    if yum is not None:
        helper += """
    If you have yum, then try typing "sudo yum -y install %s"
"""%(yum)
    if deb is not None:
        helper += """
    If you have apt-get, then try typing "sudo apt-get install %s"
"""%(deb)

    line = "\n\n################### HEADER TEST %s\n"%(header)  

    line+= m4_check_header(header,
                           "",
                           m4_error("""

THE HEADER FILE %s COULD NOT BE FOUND

This may mean that either:

(*) Library "%s" is installed in a nonstandard location

    In this case, locate /path/to/include/%s on your computer 
    and reconfigure with
    ./configure CPPFLAGS="-I/path/to/include \$CPPFLAGS"

    On some supercomputers, you may have to "module load" a package to make it
    available for use.  If you have the module command, then try typing
    "module list" to see if %s is a loadable module.
    Upon loading, you can use "module show" to help find /path/to/include

    On most machines, you can type "locate '%s'" to find a file;
    however, this rarely works to locate files mounted on a network filesystem.
    The printed results of the locate command may be out-of-date as well.
    To update the database that the locate command uses, try "sudo updatedb"

(*) Library "%s" is not installed, and you need to install it
%s
"""%(header,libname,header,libname,header,libname,helper)))
    return line



def m4_check_openmp_header_or_die(header,libname,yum=None,deb=None):
    helper = ""
    if yum is not None:
        helper += """
    If you have yum, then try typing "sudo yum -y install %s"
"""%(yum)
    if deb is not None:
        helper += """
    If you have apt-get, then try typing "sudo apt-get install %s"
"""%(deb)

    line = "\n\n################### HEADER TEST %s\n"%(header)  

    line+= m4_check_openmp_header(header,
                                  "",
                                  m4_error("""

THE HEADER FILE %s COULD NOT BE FOUND

This may mean that either:

(*) Library "%s" is installed in a nonstandard location

    In this case, locate /path/to/include/%s on your computer 
    and reconfigure with
    ./configure CPPFLAGS="-I/path/to/include \$CPPFLAGS"

    On some supercomputers, you may have to "module load" a package to make it
    available for use.  If you have the module command, then try typing
    "module list" to see if %s is a loadable module.
    Upon loading, you can use "module show" to help find /path/to/include

    On most machines, you can type "locate '%s'" to find a file;
    however, this rarely works to locate files mounted on a network filesystem.
    The printed results of the locate command may be out-of-date as well.
    To update the database that the locate command uses, try "sudo updatedb"

(*) Library "%s" is not installed, and you need to install it
%s
"""%(header,libname,header,libname,header,libname,helper)))
    return line




def m4_cxx_serial_test(libs,preamble,body):
    line = "\n\n################### LINK TEST TO %s\n"%(libs)  
    line+= m4_save_flags()
    line+= "AC_LANG_PUSH([C++])\n"
    line+= """LIBS+=" %s"\n"""%(libs)
    line+= """AC_LINK_IFELSE(
  [AC_LANG_PROGRAM(
     [
%s
     ], dnl preamble
     [
%s
     ]  dnl body
     )], dnl AC_LANG_TEST
  [
%s
  ], dnl ok
  [
%s
  ] dnl failure
) dnl AC_LINK_IFELSE
"""%(preamble,body,m4_test_ok(),m4_test_failed())
    line+= "AC_LANG_POP([C++])\n"
    line+= m4_restore_flags()
    return line



def m4_cxx_openmp_test(libs,preamble,body):
    line = "\n\n################### OPENMP LINK TEST TO %s\n"%(libs)  
    line+= m4_save_flags()
    line+= """CXXFLAGS+=" ${OPENMP_CXXFLAGS}"\n"""
    line+= "AC_LANG_PUSH([C++])\n"
    line+= """LIBS+=" %s"\n"""%(libs)
    line+= """AC_LINK_IFELSE(
  [AC_LANG_PROGRAM(
     [
%s
     ], dnl preamble
     [
%s
     ]  dnl body
     )], dnl AC_LANG_TEST
  [
%s
  ], dnl ok
  [
%s
  ] dnl failure
) dnl AC_LINK_IFELSE
"""%(preamble,body,m4_test_ok(),m4_test_failed())
    line+= "AC_LANG_POP([C++])\n"
    line+= m4_restore_flags()
    return line
