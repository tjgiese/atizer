#!/usr/bin/env python

from ..base import *
from ..m4 import *
from .python import *

class boost(autolib):
    def __init__(self):
        super( boost , self ).__init__( "boost" )
        self.serial.var = "" # no library to link
        self.serial.name = "boost"
        self.serial.cppflags = "$(BOOST_CPPFLAGS)"
        self.serial.ldflags = "$(BOOST_LDFLAGS)"
        self.openmp = self.serial
        self.mpi = self.serial

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ax_boost_base.m4") )
        fh.write("""

AX_BOOST_BASE(
  [1.46],
  [],
  [

AC_MSG_ERROR([

Could not locate boost library header files.

If you have boost installed in a nonstandard location, then try
rerunning 

   ./configure --with-boost=/path/to/include

Installation
==================================
Ubuntu: 
   sudo apt-get install libboost-all-dev
Fedora:
   sudo yum install boost-devel

  ])

])

""")




class boost_python(autolib):
    def __init__(self,python_version="2.6"):
        super( boost_python , self ).__init__( "boost_python" )
        self.serial.var = "BOOST_PYTHON_LIB"
        self.serial.name = "boost_python"
        self.openmp = self.serial
        self.mpi = self.serial
        self.libs = [ boost(), python_devel(python_version) ]

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ax_boost_python.m4") )
        fh.write("""

AX_BOOST_PYTHON

if test "x$ac_cv_boost_python" != "xyes"; then

AC_MSG_ERROR([

Could not locate libboost_python library.

If you have boost_python installed in a nonstandard location, then try
rerunning 

   ./configure --with-boost-python=/path/to/include

Installation
==================================
Ubuntu: 
   sudo apt-get install libboost-all-dev
Fedora:
   sudo yum install boost-devel

])

fi

""")


class boost_program_options(autolib):
    def __init__(self):
        super( boost_program_options , self ).__init__( "boost_program_options" )
        self.serial.var = "BOOST_PROGRAM_OPTIONS_LIB"
        self.serial.name = "boost_program_options"
        self.openmp = self.serial
        self.mpi = self.serial
        self.libs = [ boost() ]

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ax_boost_program_options.m4") )
        fh.write("""

AX_BOOST_PROGRAM_OPTIONS

if test "x$ax_cv_boost_program_options" != "xyes"; then

AC_MSG_ERROR([

Could not locate libboost_program_options library.

If you have libboost_program_options installed in a nonstandard location, then try
rerunning 

   ./configure --with-boost-python=/path/to/include

Installation
==================================
Ubuntu: 
   sudo apt-get install libboost-all-dev
Fedora:
   sudo yum install boost-devel

])

fi

""")




class boost_asio(autolib):
    def __init__(self):
        super( boost_asio , self ).__init__( "boost_asio" )
        self.serial.var = "BOOST_ASIO_LIB"
        self.serial.name = "boost_asio"
        self.openmp = self.serial
        self.mpi = self.serial
        self.libs = [ boost() ]

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ax_boost_asio.m4") )
        fh.write("""

AX_BOOST_ASIO

if test "x$ax_cv_boost_asio" != "xyes"; then

AC_MSG_ERROR([

Could not locate libboost_asio library.

If you have libboost_asio installed in a nonstandard location, then try
rerunning 

   ./configure --with-boost-python=/path/to/include

Installation
==================================
Ubuntu: 
   sudo apt-get install libboost-all-dev
Fedora:
   sudo yum install boost-devel

])

fi

""")



class boost_chrono(autolib):
    def __init__(self):
        super( boost_chrono , self ).__init__( "boost_chrono" )
        self.serial.var = "BOOST_CHRONO_LIB"
        self.serial.name = "boost_chrono"
        self.openmp = self.serial
        self.mpi = self.serial
        self.libs = [ boost() ]

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ax_boost_chrono.m4") )
        fh.write("""

AX_BOOST_CHRONO

if test "x$ax_cv_boost_chrono" != "xyes"; then

AC_MSG_ERROR([

Could not locate libboost_chrono library.

If you have libboost_chrono installed in a nonstandard location, then try
rerunning 

   ./configure --with-boost-python=/path/to/include

Installation
==================================
Ubuntu: 
   sudo apt-get install libboost-all-dev
Fedora:
   sudo yum install boost-devel

])

fi

""")

class boost_date_time(autolib):
    def __init__(self):
        super( boost_date_time , self ).__init__( "boost_date_time" )
        self.serial.var = "BOOST_DATE_TIME_LIB"
        self.serial.name = "boost_date_time"
        self.openmp = self.serial
        self.mpi = self.serial
        self.libs = [ boost() ]

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ax_boost_date_time.m4") )
        fh.write("""

AX_BOOST_DATE_TIME

if test "x$ax_cv_boost_date_time" != "xyes"; then

AC_MSG_ERROR([

Could not locate libboost_date_time library.

If you have libboost_date_time installed in a nonstandard location, then try
rerunning 

   ./configure --with-boost-python=/path/to/include

Installation
==================================
Ubuntu: 
   sudo apt-get install libboost-all-dev
Fedora:
   sudo yum install boost-devel

])

fi

""")



class boost_filesystem(autolib):
    def __init__(self):
        super( boost_filesystem , self ).__init__( "boost_filesystem" )
        self.serial.var = "BOOST_FILESYSTEM_LIB"
        self.serial.name = "boost_filesystem"
        self.openmp = self.serial
        self.mpi = self.serial
        self.libs = [ boost() ]

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ax_boost_filesystem.m4") )
        fh.write("""

AX_BOOST_FILESYSTEM

if test "x$ax_cv_boost_filesystem" != "xyes"; then

AC_MSG_ERROR([

Could not locate libboost_filesystem library.

If you have libboost_filesystem installed in a nonstandard location, then try
rerunning 

   ./configure --with-boost-python=/path/to/include

Installation
==================================
Ubuntu: 
   sudo apt-get install libboost-all-dev
Fedora:
   sudo yum install boost-devel

])

fi

""")



class boost_iostreams(autolib):
    def __init__(self):
        super( boost_iostreams , self ).__init__( "boost_iostreams" )
        self.serial.var = "BOOST_IOSTREAMS_LIB"
        self.serial.name = "boost_iostreams"
        self.openmp = self.serial
        self.mpi = self.serial
        self.libs = [ boost() ]

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ax_boost_iostreams.m4") )
        fh.write("""

AX_BOOST_IOSTREAMS

if test "x$ax_cv_boost_iostreams" != "xyes"; then

AC_MSG_ERROR([

Could not locate libboost_iostreams library.

If you have libboost_iostreams installed in a nonstandard location, then try
rerunning 

   ./configure --with-boost-python=/path/to/include

Installation
==================================
Ubuntu: 
   sudo apt-get install libboost-all-dev
Fedora:
   sudo yum install boost-devel

])

fi

""")


class boost_locale(autolib):
    def __init__(self):
        super( boost_locale , self ).__init__( "boost_locale" )
        self.serial.var = "BOOST_LOCALE_LIB"
        self.serial.name = "boost_locale"
        self.openmp = self.serial
        self.mpi = self.serial
        self.libs = [ boost() ]

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ax_boost_locale.m4") )
        fh.write("""

AX_BOOST_LOCALE

if test "x$ax_cv_boost_locale" != "xyes"; then

AC_MSG_ERROR([

Could not locate libboost_locale library.

If you have libboost_locale installed in a nonstandard location, then try
rerunning 

   ./configure --with-boost-python=/path/to/include

Installation
==================================
Ubuntu: 
   sudo apt-get install libboost-all-dev
Fedora:
   sudo yum install boost-devel

])

fi

""")



class boost_regex(autolib):
    def __init__(self):
        super( boost_regex , self ).__init__( "boost_regex" )
        self.serial.var = "BOOST_REGEX_LIB"
        self.serial.name = "boost_regex"
        self.openmp = self.serial
        self.mpi = self.serial
        self.libs = [ boost() ]

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ax_boost_regex.m4") )
        fh.write("""

AX_BOOST_REGEX

if test "x$ax_cv_boost_regex" != "xyes"; then

AC_MSG_ERROR([

Could not locate libboost_regex library.

If you have libboost_regex installed in a nonstandard location, then try
rerunning 

   ./configure --with-boost-python=/path/to/include

Installation
==================================
Ubuntu: 
   sudo apt-get install libboost-all-dev
Fedora:
   sudo yum install boost-devel

])

fi

""")


class boost_serialization(autolib):
    def __init__(self):
        super( boost_serialization , self ).__init__( "boost_serialization" )
        self.serial.var = "BOOST_SERIALIZATION_LIB"
        self.serial.name = "boost_serialization"
        self.openmp = self.serial
        self.mpi = self.serial
        self.libs = [ boost() ]

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ax_boost_serialization.m4") )
        fh.write("""

AX_BOOST_SERIALIZATION

if test "x$ax_cv_boost_serialization" != "xyes"; then

AC_MSG_ERROR([

Could not locate libboost_serialization library.

If you have libboost_serialization installed in a nonstandard location, then try
rerunning 

   ./configure --with-boost-python=/path/to/include

Installation
==================================
Ubuntu: 
   sudo apt-get install libboost-all-dev
Fedora:
   sudo yum install boost-devel

])

fi

""")



class boost_signals(autolib):
    def __init__(self):
        super( boost_signals , self ).__init__( "boost_signals" )
        self.serial.var = "BOOST_SIGNALS_LIB"
        self.serial.name = "boost_signals"
        self.openmp = self.serial
        self.mpi = self.serial
        self.libs = [ boost() ]

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ax_boost_signals.m4") )
        fh.write("""

AX_BOOST_SIGNALS

if test "x$ax_cv_boost_signals" != "xyes"; then

AC_MSG_ERROR([

Could not locate libboost_signals library.

If you have libboost_signals installed in a nonstandard location, then try
rerunning 

   ./configure --with-boost-python=/path/to/include

Installation
==================================
Ubuntu: 
   sudo apt-get install libboost-all-dev
Fedora:
   sudo yum install boost-devel

])

fi

""")


class boost_system(autolib):
    def __init__(self):
        super( boost_system , self ).__init__( "boost_system" )
        self.serial.var = "BOOST_SYSTEM_LIB"
        self.serial.name = "boost_system"
        self.openmp = self.serial
        self.mpi = self.serial
        self.libs = [ boost() ]

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ax_boost_system.m4") )
        fh.write("""

AX_BOOST_SYSTEM

if test "x$ax_cv_boost_system" != "xyes"; then

AC_MSG_ERROR([

Could not locate libboost_system library.

If you have libboost_system installed in a nonstandard location, then try
rerunning 

   ./configure --with-boost-python=/path/to/include

Installation
==================================
Ubuntu: 
   sudo apt-get install libboost-all-dev
Fedora:
   sudo yum install boost-devel

])

fi

""")

class boost_test_exec_monitor(autolib):
    def __init__(self):
        super( boost_test_exec_monitor , self ).__init__( "boost_test_exec_monitor" )
        self.serial.var = "BOOST_TEST_EXEC_MONITOR_LIB"
        self.serial.name = "boost_test_exec_monitor"
        self.openmp = self.serial
        self.mpi = self.serial
        self.libs = [ boost() ]

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ax_boost_test_exec_monitor.m4") )
        fh.write("""

AX_BOOST_TEST_EXEC_MONITOR

if test "x$ax_cv_boost_test_exec_monitor" != "xyes"; then

AC_MSG_ERROR([

Could not locate libboost_test_exec_monitor library.

If you have libboost_test_exec_monitor installed in a nonstandard location, then try
rerunning 

   ./configure --with-boost-python=/path/to/include

Installation
==================================
Ubuntu: 
   sudo apt-get install libboost-all-dev
Fedora:
   sudo yum install boost-devel

])

fi

""")


class boost_thread(autolib):
    def __init__(self):
        super( boost_thread , self ).__init__( "boost_thread" )
        self.serial.var = "BOOST_THREAD_LIB"
        self.serial.name = "boost_thread"
        self.openmp = self.serial
        self.mpi = self.serial
        self.libs = [ boost() ]

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ax_boost_thread.m4") )
        fh.write("""

AX_BOOST_THREAD

if test "x$ax_cv_boost_thread" != "xyes"; then

AC_MSG_ERROR([

Could not locate libboost_thread library.

If you have libboost_thread installed in a nonstandard location, then try
rerunning 

   ./configure --with-boost-python=/path/to/include

Installation
==================================
Ubuntu: 
   sudo apt-get install libboost-all-dev
Fedora:
   sudo yum install boost-devel

])

fi

""")


class boost_unit_test_framework(autolib):
    def __init__(self):
        super( boost_unit_test_framework , self ).__init__( "boost_unit_test_framework" )
        self.serial.var = "BOOST_UNIT_TEST_FRAMEWORK_LIB"
        self.serial.name = "boost_unit_test_framework"
        self.openmp = self.serial
        self.mpi = self.serial
        self.libs = [ boost() ]

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ax_boost_unit_test_framework.m4") )
        fh.write("""

AX_BOOST_UNIT_TEST_FRAMEWORK

if test "x$ax_cv_boost_unit_test_framework" != "xyes"; then

AC_MSG_ERROR([

Could not locate libboost_unit_test_framework library.

If you have libboost_unit_test_framework installed in a nonstandard location, then try
rerunning 

   ./configure --with-boost-python=/path/to/include

Installation
==================================
Ubuntu: 
   sudo apt-get install libboost-all-dev
Fedora:
   sudo yum install boost-devel

])

fi

""")


class boost_wave(autolib):
    def __init__(self):
        super( boost_wave , self ).__init__( "boost_wave" )
        self.serial.var = "BOOST_WAVE_LIB"
        self.serial.name = "boost_wave"
        self.openmp = self.serial
        self.mpi = self.serial
        self.libs = [ boost() ]

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ax_boost_wave.m4") )
        fh.write("""

AX_BOOST_WAVE

if test "x$ax_cv_boost_wave" != "xyes"; then

AC_MSG_ERROR([

Could not locate libboost_wave library.

If you have libboost_wave installed in a nonstandard location, then try
rerunning 

   ./configure --with-boost-python=/path/to/include

Installation
==================================
Ubuntu: 
   sudo apt-get install libboost-all-dev
Fedora:
   sudo yum install boost-devel

])

fi

""")

class boost_wserialization(autolib):
    def __init__(self):
        super( boost_wserialization , self ).__init__( "boost_wserialization" )
        self.serial.var = "BOOST_WSERIALIZATION_LIB"
        self.serial.name = "boost_wserialization"
        self.openmp = self.serial
        self.mpi = self.serial
        self.libs = [ boost() ]

    def ac_subst_var_serial(self,fh):
        fh.write( ax_macro("ax_boost_wserialization.m4") )
        fh.write("""

AX_BOOST_WSERIALIZATION

if test "x$ax_cv_boost_wserialization" != "xyes"; then

AC_MSG_ERROR([

Could not locate libboost_wserialization library.

If you have libboost_wserialization installed in a nonstandard location, then try
rerunning 

   ./configure --with-boost-python=/path/to/include

Installation
==================================
Ubuntu: 
   sudo apt-get install libboost-all-dev
Fedora:
   sudo yum install boost-devel

])

fi

""")
