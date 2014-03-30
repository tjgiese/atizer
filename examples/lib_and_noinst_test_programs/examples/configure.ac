# ===========================================================================
#         http://www.gnu.org/software/autoconf-archive/ax_openmp.html
# ===========================================================================
#
# SYNOPSIS
#
#   AX_OPENMP([ACTION-IF-FOUND[, ACTION-IF-NOT-FOUND]])
#
# DESCRIPTION
#
#   This macro tries to find out how to compile programs that use OpenMP a
#   standard API and set of compiler directives for parallel programming
#   (see http://www-unix.mcs/)
#
#   On success, it sets the OPENMP_CFLAGS/OPENMP_CXXFLAGS/OPENMP_F77FLAGS
#   output variable to the flag (e.g. -omp) used both to compile *and* link
#   OpenMP programs in the current language.
#
#   NOTE: You are assumed to not only compile your program with these flags,
#   but also link it with them as well.
#
#   If you want to compile everything with OpenMP, you should set:
#
#     CFLAGS="$CFLAGS $OPENMP_CFLAGS"
#     #OR#  CXXFLAGS="$CXXFLAGS $OPENMP_CXXFLAGS"
#     #OR#  FFLAGS="$FFLAGS $OPENMP_FFLAGS"
#
#   (depending on the selected language).
#
#   The user can override the default choice by setting the corresponding
#   environment variable (e.g. OPENMP_CFLAGS).
#
#   ACTION-IF-FOUND is a list of shell commands to run if an OpenMP flag is
#   found, and ACTION-IF-NOT-FOUND is a list of commands to run it if it is
#   not found. If ACTION-IF-FOUND is not specified, the default action will
#   define HAVE_OPENMP.
#
# LICENSE
#
#   Copyright (c) 2008 Steven G. Johnson <stevenj@alum.mit.edu>
#
#   This program is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by the
#   Free Software Foundation, either version 3 of the License, or (at your
#   option) any later version.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
#   Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program. If not, see <http://www.gnu.org/licenses/>.
#
#   As a special exception, the respective Autoconf Macro's copyright owner
#   gives unlimited permission to copy, distribute and modify the configure
#   scripts that are the output of Autoconf when processing the Macro. You
#   need not follow the terms of the GNU General Public License when using
#   or distributing such scripts, even though portions of the text of the
#   Macro appear in them. The GNU General Public License (GPL) does govern
#   all other use of the material that constitutes the Autoconf Macro.
#
#   This special exception to the GPL applies to versions of the Autoconf
#   Macro released by the Autoconf Archive. When you make and distribute a
#   modified version of the Autoconf Macro, you may extend this special
#   exception to the GPL to apply to your modified version as well.

### serial 9

AC_DEFUN([AX_OPENMP], [
AC_PREREQ(2.59) dnl for _AC_LANG_PREFIX

AC_CACHE_CHECK([for OpenMP flag of _AC_LANG compiler], ax_cv_[]_AC_LANG_ABBREV[]_openmp, [save[]_AC_LANG_PREFIX[]FLAGS=$[]_AC_LANG_PREFIX[]FLAGS
ax_cv_[]_AC_LANG_ABBREV[]_openmp=unknown
# Flags to try:  -fopenmp (gcc), -openmp (icc), -mp (SGI & PGI),
#                -xopenmp (Sun), -omp (Tru64), -qsmp=omp (AIX), none
ax_openmp_flags="-fopenmp -openmp -mp -xopenmp -omp -qsmp=omp none"
if test "x$OPENMP_[]_AC_LANG_PREFIX[]FLAGS" != x; then
  ax_openmp_flags="$OPENMP_[]_AC_LANG_PREFIX[]FLAGS $ax_openmp_flags"
fi
for ax_openmp_flag in $ax_openmp_flags; do
  case $ax_openmp_flag in
    none) []_AC_LANG_PREFIX[]FLAGS=$save[]_AC_LANG_PREFIX[] ;;
    *) []_AC_LANG_PREFIX[]FLAGS="$save[]_AC_LANG_PREFIX[]FLAGS $ax_openmp_flag" ;;
  esac
  AC_TRY_LINK([#ifdef __cplusplus
extern "C"
#endif
void omp_set_num_threads(int);], [const int N = 100000;
  int i, arr[N];

  omp_set_num_threads(2);

  #pragma omp parallel for
  for (i = 0; i < N; i++) {
    arr[i] = i;
  }], [ax_cv_[]_AC_LANG_ABBREV[]_openmp=$ax_openmp_flag; break])
done
[]_AC_LANG_PREFIX[]FLAGS=$save[]_AC_LANG_PREFIX[]FLAGS
])
if test "x$ax_cv_[]_AC_LANG_ABBREV[]_openmp" = "xunknown"; then
  m4_default([$2],:)
else
  if test "x$ax_cv_[]_AC_LANG_ABBREV[]_openmp" != "xnone"; then
    OPENMP_[]_AC_LANG_PREFIX[]FLAGS=$ax_cv_[]_AC_LANG_ABBREV[]_openmp
  fi
  m4_default([$1], [AC_DEFINE(HAVE_OPENMP,1,[Define if OpenMP is enabled])])
fi
])dnl AX_OPENMP


# AC_DEFUN([AY_OPENMP_FC], [
# AC_PREREQ(2.59) dnl for _AC_LANG_PREFIX

# AC_CACHE_CHECK([for OpenMP flag of _AC_LANG compiler],
# saved_FCFLAGS="$FCFLAGS"
# ay_openmp_flags="-fopenmp -openmp -mp -xopenmp -omp -qsmp=omp"
# ay_have_openmp_flag="no"
# ay_flag=""

# for ay_openmp_flag in $ax_openmp_flags; do

#    AC_TRY_LINK(
#    [
# PROGRAM hello
#     use omp_lib
#     INTEGER id,nthreads
#     nthreads = omp_get_num_threads()
#     id = omp_get_thread_num()
# END PROGRAM hello
#    ]
#    , 
#    [ay_flag=$ay_openmp_flag]
#    [ay_have_openmp_flag="yes"]
#    [break]
#    )

# done

# if test "x$ay_have_openmp_flag" != "xno"; then
#     OPENMP_FCFLAGS=$ay_flag
#     AC_DEFINE(HAVE_OPENMP,1,[Define if OpenMP is enabled])
# else
#     AC_MSG_RESULT([no])
# fi

# ])dnl AY_OPENMP_FC




AC_DEFUN([AY_FC_OPENMP], [
AC_PREREQ(2.59) dnl for _AC_LANG_PREFIX

AC_CACHE_CHECK([for OpenMP flag of _AC_LANG compiler], ax_cv_[]_AC_LANG_ABBREV[]_openmp, [save[]_AC_LANG_PREFIX[]FLAGS=$[]_AC_LANG_PREFIX[]FLAGS
ax_cv_[]_AC_LANG_ABBREV[]_openmp=unknown
# Flags to try:  -fopenmp (gcc), -openmp (icc), -mp (SGI & PGI),
#                -xopenmp (Sun), -omp (Tru64), -qsmp=omp (AIX), none
ax_openmp_flags="-fopenmp -openmp -mp -xopenmp -omp -qsmp=omp none"
if test "x$OPENMP_[]_AC_LANG_PREFIX[]FLAGS" != x; then
  ax_openmp_flags="$OPENMP_[]_AC_LANG_PREFIX[]FLAGS $ax_openmp_flags"
fi
for ax_openmp_flag in $ax_openmp_flags; do
  case $ax_openmp_flag in
    none) []_AC_LANG_PREFIX[]FLAGS=$save[]_AC_LANG_PREFIX[] ;;
    *) []_AC_LANG_PREFIX[]FLAGS="$save[]_AC_LANG_PREFIX[]FLAGS $ax_openmp_flag" ;;
  esac
  AC_LINK_IFELSE( [ AC_LANG_PROGRAM([],
[
    use omp_lib
    INTEGER id,nthreads
    nthreads = omp_get_num_threads()
    id = omp_get_thread_num()
]) ], 
   [ax_cv_[]_AC_LANG_ABBREV[]_openmp=$ax_openmp_flag; break])
done
[]_AC_LANG_PREFIX[]FLAGS=$save[]_AC_LANG_PREFIX[]FLAGS
])
if test "x$ax_cv_[]_AC_LANG_ABBREV[]_openmp" = "xunknown"; then
  m4_default([$2],:)
else
  if test "x$ax_cv_[]_AC_LANG_ABBREV[]_openmp" != "xnone"; then
    OPENMP_[]_AC_LANG_PREFIX[]FLAGS=$ax_cv_[]_AC_LANG_ABBREV[]_openmp
  fi
  m4_default([$1], [AC_DEFINE(HAVE_OPENMP,1,[Define if OpenMP is enabled])])
fi
])dnl AY_FC_OPENMP

# ===========================================================================
#      http://www.gnu.org/software/autoconf-archive/ax_prog_cc_mpi.html
# ===========================================================================
#
# SYNOPSIS
#
#   AX_PROG_CC_MPI([MPI-WANTED-TEST[, ACTION-IF-FOUND[, ACTION-IF-NOT-FOUND]]])
#
# DESCRIPTION
#
#   This macro tries to find out how to compile C programs that use MPI
#   (Message Passing Interface), a standard API for parallel process
#   communication (see http://www-unix.mcs.anl.gov/mpi/). The macro has to
#   be used instead of the standard macro AC_PROG_CC and will replace the
#   standard variable CC with the found compiler.
#
#   MPI-WANTED-TEST is used to test whether MPI is actually wanted by the
#   user. If MPI-WANTED_TEST is omitted or if it succeeds, the macro will
#   try to find out how to use MPI, if it fails, the macro will call
#   AC_PROG_CC to find a standard C compiler instead.
#
#   When MPI is found, ACTION-IF-FOUND will be executed, if MPI is not found
#   (or MPI-WANTED-TEST fails) ACTION-IF-NOT-FOUND is executed. If
#   ACTION-IF-FOUND is not set, the macro will define HAVE_MPI.
#
#   The following example demonstrates usage of the macro:
#
#     # If --with-mpi=auto is used, try to find MPI, but use standard C compiler if it is not found.
#     # If --with-mpi=yes is used, try to find MPI and fail if it isn't found.
#     # If --with-mpi=no is used, use a standard C compiler instead.
#     AC_ARG_WITH(mpi, [AS_HELP_STRING([--with-mpi],
#         [compile with MPI (parallelization) support. If none is found,
#         MPI is not used. Default: auto])
#     ],,[with_mpi=auto])
#     #
#     AX_PROG_CC_MPI([test x"$with_mpi" != xno],[use_mpi=yes],[
#       use_mpi=no
#       if test x"$with_mpi" = xyes; then
#         AC_MSG_FAILURE([MPI compiler requested, but couldn't use MPI.])
#       else
#         AC_MSG_WARN([No MPI compiler found, won't use MPI.])
#       fi
#     ])
#
# LICENSE
#
#   Copyright (c) 2010,2011 Olaf Lenz <olenz@icp.uni-stuttgart.de>
#
#   This program is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by the
#   Free Software Foundation, either version 3 of the License, or (at your
#   option) any later version.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
#   Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program. If not, see <http://www.gnu.org/licenses/>.
#
#   As a special exception, the respective Autoconf Macro's copyright owner
#   gives unlimited permission to copy, distribute and modify the configure
#   scripts that are the output of Autoconf when processing the Macro. You
#   need not follow the terms of the GNU General Public License when using
#   or distributing such scripts, even though portions of the text of the
#   Macro appear in them. The GNU General Public License (GPL) does govern
#   all other use of the material that constitutes the Autoconf Macro.
#
#   This special exception to the GPL applies to versions of the Autoconf
#   Macro released by the Autoconf Archive. When you make and distribute a
#   modified version of the Autoconf Macro, you may extend this special
#   exception to the GPL to apply to your modified version as well.

### serial 1

AC_DEFUN([AX_PROG_CC_MPI], [
AC_PREREQ(2.50)

# Check for compiler
# Needs to be split off into an extra macro to ensure right expansion
# order.
AC_REQUIRE([_AX_PROG_CC_MPI],[_AX_PROG_CC_MPI([$1])])

AS_IF([test x"$_ax_prog_cc_mpi_mpi_wanted" = xno],
  [ _ax_prog_cc_mpi_mpi_found=no ],
  [
    AC_LANG_PUSH([C])
    # test whether MPI_Init is available
    # We do not use AC_SEARCH_LIBS here, as it caches its outcome and
    # thus disallows corresponding calls in the other AX_PROG_*_MPI
    # macros.
    for lib in NONE mpi mpich; do
      save_LIBS=$LIBS
      if test x"$lib" = xNONE; then
        AC_MSG_CHECKING([for function MPI_Init])
      else
        AC_MSG_CHECKING([for function MPI_Init in -l$lib])
        LIBS="-l$lib $LIBS"
      fi
      AC_LINK_IFELSE([AC_LANG_CALL([],[MPI_Init])],
        [ _ax_prog_cc_mpi_mpi_found=yes ],
        [ _ax_prog_cc_mpi_mpi_found=no ])
      AC_MSG_RESULT($_ax_prog_cc_mpi_mpi_found)
      if test "x$_ax_prog_cc_mpi_mpi_found" = "xyes"; then
        break;
      fi
      LIBS=$save_LIBS
    done

    # Check for header
    AS_IF([test x"$_ax_prog_cc_mpi_mpi_found" = xyes], [
      AC_MSG_CHECKING([for mpi.h])
      AC_COMPILE_IFELSE([AC_LANG_PROGRAM([#include <mpi.h>])],
        [ AC_MSG_RESULT(yes)],
        [ AC_MSG_RESULT(no)
         _ax_prog_cc_mpi_mpi_found=no
      ])
    ])
    AC_LANG_POP([C])
])

# Finally, execute ACTION-IF-FOUND/ACTION-IF-NOT-FOUND:
AS_IF([test x"$_ax_prog_cc_mpi_mpi_found" = xyes], [
        ifelse([$2],,[AC_DEFINE(HAVE_MPI,1,[Define if you have the MPI library.])],[$2])
        :
],[
        $3
        :
])

])dnl AX_PROG_CC_MPI

dnl _AX_PROG_CC_MPI is an internal macro required by AX_PROG_CC_MPI.
dnl To ensure the right expansion order, the main function AX_PROG_CC_MPI
dnl has to be split into two parts.
dnl
dnl Known MPI C compilers:
dnl  mpicc
dnl  mpixlc_r
dnl  mpixlc
dnl  hcc
dnl  mpxlc_r
dnl  mpxlc
dnl  sxmpicc  NEC SX
dnl  mpifcc   Fujitsu
dnl  mpgcc
dnl  mpcc
dnl  cmpicc
dnl  cc
dnl
AC_DEFUN([_AX_PROG_CC_MPI], [
  AC_ARG_VAR(MPICC,[MPI C compiler command])
  ifelse([$1],,[_ax_prog_cc_mpi_mpi_wanted=yes],[
    AC_MSG_CHECKING([whether to compile using MPI])
    if $1; then
      _ax_prog_cc_mpi_mpi_wanted=yes
    else
      _ax_prog_cc_mpi_mpi_wanted=no
    fi
    AC_MSG_RESULT($_ax_prog_cc_mpi_mpi_wanted)
  ])
  if test x"$_ax_prog_cc_mpi_mpi_wanted" = xyes; then
    if test -z "$CC" && test -n "$MPICC"; then
      CC="$MPICC"
    else
      AC_CHECK_TOOLS([CC], [mpicc mpixlc_r mpixlc hcc mpxlc_r mpxlc sxmpicc mpifcc mpgcc mpcc cmpicc cc gcc])
    fi
  fi
  AC_PROG_CC
])dnl _AX_PROG_CC_MPI

# ===========================================================================
#      http://www.gnu.org/software/autoconf-archive/ax_prog_cxx_mpi.html
# ===========================================================================
#
# SYNOPSIS
#
#   AX_PROG_CXX_MPI([MPI-WANTED-TEST[, ACTION-IF-FOUND[, ACTION-IF-NOT-FOUND]]])
#
# DESCRIPTION
#
#   This macro tries to find out how to compile C++ programs that use MPI
#   (Message Passing Interface), a standard API for parallel process
#   communication (see http://www-unix.mcs.anl.gov/mpi/).  The macro has to
#   be used instead of the standard macro AC_PROG_CXX and will replace the
#   standard variable CXX with the found compiler.
#
#   MPI-WANTED-TEST is used to test whether MPI is actually wanted by the
#   user. If MPI-WANTED_TEST is omitted or if it succeeds, the macro will
#   try to find out how to use MPI, if it fails, the macro will call
#   AC_PROG_CC to find a standard C compiler instead.
#
#   When MPI is found, ACTION-IF-FOUND will be executed, if MPI is not found
#   (or MPI-WANTED-TEST fails) ACTION-IF-NOT-FOUND is executed. If
#   ACTION-IF-FOUND is not set, the macro will define HAVE_MPI.
#
#   The following example demonstrates usage of the macro:
#
#     # If --with-mpi=auto is used, try to find MPI, but use standard C compiler if it is not found.
#     # If --with-mpi=yes is used, try to find MPI and fail if it isn't found.
#     # If --with-mpi=no is used, use a standard C compiler instead.
#     AC_ARG_WITH(mpi, [AS_HELP_STRING([--with-mpi],
#         [compile with MPI (parallelization) support. If none is found,
#         MPI is not used. Default: auto])
#     ],,[with_mpi=auto])
#
#     AX_PROG_CXX_MPI([test x"$with_mpi" != xno],[use_mpi=yes],[
#       use_mpi=no
#       if test x"$with_mpi" = xyes; then
#         AC_MSG_FAILURE([MPI compiler requested, but couldn't use MPI.])
#       else
#         AC_MSG_WARN([No MPI compiler found, won't use MPI.])
#       fi
#     ])
#
# LICENSE
#
#   Copyright (c) 2010,2011 Olaf Lenz <olenz@icp.uni-stuttgart.de>
#
#   This program is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by the
#   Free Software Foundation, either version 3 of the License, or (at your
#   option) any later version.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
#   Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program. If not, see <http://www.gnu.org/licenses/>.
#
#   As a special exception, the respective Autoconf Macro's copyright owner
#   gives unlimited permission to copy, distribute and modify the configure
#   scripts that are the output of Autoconf when processing the Macro. You
#   need not follow the terms of the GNU General Public License when using
#   or distributing such scripts, even though portions of the text of the
#   Macro appear in them. The GNU General Public License (GPL) does govern
#   all other use of the material that constitutes the Autoconf Macro.
#
#   This special exception to the GPL applies to versions of the Autoconf
#   Macro released by the Autoconf Archive. When you make and distribute a
#   modified version of the Autoconf Macro, you may extend this special
#   exception to the GPL to apply to your modified version as well.

### serial 1

AC_DEFUN([AX_PROG_CXX_MPI], [
AC_PREREQ(2.50)

# Check for compiler
# Needs to be split off into an extra macro to ensure right expansion
# order.
AC_REQUIRE([_AX_PROG_CXX_MPI],[_AX_PROG_CXX_MPI([$1])])

AS_IF([test x"$_ax_prog_cxx_mpi_mpi_wanted" = xno],
  [ _ax_prog_cxx_mpi_mpi_found=no ],
  [
    AC_LANG_PUSH([C++])

    # test whether MPI::Init is available
    # We do not use AC_SEARCH_LIBS here, as it caches its outcome and
    # thus disallows corresponding calls in the other AX_PROG_*_MPI
    # macros.
    for lib in NONE mpi mpich; do
      save_LIBS=$LIBS
      if test x"$lib" = xNONE; then
        AC_MSG_CHECKING([for function MPI::Init])
      else
        AC_MSG_CHECKING([for function MPI::Init in -l$lib])
        LIBS="-l$lib $LIBS"
      fi
      AC_LINK_IFELSE([
        AC_LANG_PROGRAM([
namespace MPI {
char Init();
};
using MPI::Init;],[MPI::Init;])],
        [ _ax_prog_cxx_mpi_mpi_found=yes ],
        [ _ax_prog_cxx_mpi_mpi_found=no ])
      AC_MSG_RESULT($_ax_prog_cxx_mpi_mpi_found)
      if test "x$_ax_prog_cxx_mpi_mpi_found" = "xyes"; then
        break;
      fi
      LIBS=$save_LIBS
    done

    # Check for header
    AS_IF([test x"$_ax_prog_cxx_mpi_mpi_found" = xyes], [
      AC_MSG_CHECKING([for mpi.h])
      AC_COMPILE_IFELSE([AC_LANG_PROGRAM([#include <mpi.h>])],
        [ AC_MSG_RESULT(yes)],
        [ AC_MSG_RESULT(no)
         _ax_prog_cxx_mpi_mpi_found=no
      ])
    ])
    AC_LANG_POP([C++])
])

# Finally, execute ACTION-IF-FOUND/ACTION-IF-NOT-FOUND:
AS_IF([test x"$_ax_prog_cxx_mpi_mpi_found" = xyes], [
        ifelse([$2],,[AC_DEFINE(HAVE_MPI,1,[Define if you have the MPI library.])],[$2])
        :
],[
        $3
        :
])

])dnl AX_PROG_CXX_MPI

dnl _AX_PROG_CXX_MPI is an internal macro required by AX_PROG_CXX_MPI.
dnl To ensure the right expansion order, the main function AX_PROG_CXX_MPI
dnl has to be split into two parts.
dnl
dnl Known MPI C++ compilers:
dnl  mpic++
dnl  mpicxx
dnl  mpiCC
dnl  sxmpic++     NEC SX
dnl  hcp
dnl  mpxlC_r
dnl  mpxlC
dnl  mpixlcxx_r
dnl  mpixlcxx
dnl  mpg++
dnl  mpc++
dnl  mpCC
dnl  cmpic++
dnl  mpiFCC       Fujitsu
dnl  CC
dnl
AC_DEFUN([_AX_PROG_CXX_MPI], [
  AC_ARG_VAR(MPICXX,[MPI C++ compiler command])
  ifelse([$1],,[_ax_prog_cxx_mpi_mpi_wanted=yes],[
    AC_MSG_CHECKING([whether to compile using MPI])
    if $1; then
      _ax_prog_cxx_mpi_mpi_wanted=yes
    else
      _ax_prog_cxx_mpi_mpi_wanted=no
    fi
    AC_MSG_RESULT($_ax_prog_cxx_mpi_mpi_wanted)
  ])
  if test x"$_ax_prog_cxx_mpi_mpi_wanted" = xyes; then
    if test -z "$CXX" && test -n "$MPICXX"; then
      CXX="$MPICXX"
    else
      AC_CHECK_TOOLS([CXX], [mpic++ mpicxx mpiCC sxmpic++ hcp mpxlC_r mpxlC mpixlcxx_r mpixlcxx mpg++ mpc++ mpCC cmpic++ mpiFCC CCicpc pgCC pathCC sxc++ xlC_r xlC bgxlC_r bgxlC openCC sunCC crayCC g++ c++ gpp aCC CC cxx cc++ cl.exe FCC KCC RCC])
    fi
  fi
  AC_PROG_CXX
])dnl _AX_PROG_CXX_MPI

# ===========================================================================
#      http://www.gnu.org/software/autoconf-archive/ax_prog_fc_mpi.html
# ===========================================================================
#
# SYNOPSIS
#
#   AX_PROG_FC_MPI([MPI-WANTED-TEST[, ACTION-IF-FOUND[, ACTION-IF-NOT-FOUND]]])
#
# DESCRIPTION
#
#   This macro tries to find out how to compile Fortran77 programs that use
#   MPI (Message Passing Interface), a standard API for parallel process
#   communication (see http://www-unix.mcs.anl.gov/mpi/).  The macro has to
#   be used instead of the standard macro AC_PROG_FC and will replace the
#   standard variable FC with the found compiler.
#
#   MPI-WANTED-TEST is used to test whether MPI is actually wanted by the
#   user. If MPI-WANTED_TEST is omitted or if it succeeds, the macro will
#   try to find out how to use MPI, if it fails, the macro will call
#   AC_PROG_CC to find a standard C compiler instead.
#
#   When MPI is found, ACTION-IF-FOUND will be executed, if MPI is not found
#   (or MPI-WANTED-TEST fails) ACTION-IF-NOT-FOUND is executed. If
#   ACTION-IF-FOUND is not set, the macro will define HAVE_MPI.
#
#   The following example demonstrates usage of the macro:
#
#     # If --with-mpi=auto is used, try to find MPI, but use standard FC compiler if it is not found.
#     # If --with-mpi=yes is used, try to find MPI and fail if it isn't found.
#     # If --with-mpi=no is used, use a standard FC compiler instead.
#     AC_ARG_WITH(mpi, [AS_HELP_STRING([--with-mpi],
#         [compile with MPI (parallelization) support. If none is found,
#         MPI is not used. Default: auto])
#     ],,[with_mpi=auto])
#
#     AX_PROG_FC_MPI([test x"$with_mpi" != xno],[use_mpi=yes],[
#       use_mpi=no
#       if test x"$with_mpi" = xyes; then
#         AC_MSG_FAILURE([MPI compiler requested, but couldn't use MPI.])
#       else
#         AC_MSG_WARN([No MPI compiler found, won't use MPI.])
#       fi
#     ])
#
# LICENSE
#
#   Copyright (c) 2010,2011 Olaf Lenz <olenz@icp.uni-stuttgart.de>
#
#   This program is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by the
#   Free Software Foundation, either version 3 of the License, or (at your
#   option) any later version.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
#   Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program. If not, see <http://www.gnu.org/licenses/>.
#
#   As a special exception, the respective Autoconf Macro's copyright owner
#   gives unlimited permission to copy, distribute and modify the configure
#   scripts that are the output of Autoconf when processing the Macro. You
#   need not follow the terms of the GNU General Public License when using
#   or distributing such scripts, even though portions of the text of the
#   Macro appear in them. The GNU General Public License (GPL) does govern
#   all other use of the material that constitutes the Autoconf Macro.
#
#   This special exception to the GPL applies to versions of the Autoconf
#   Macro released by the Autoconf Archive. When you make and distribute a
#   modified version of the Autoconf Macro, you may extend this special
#   exception to the GPL to apply to your modified version as well.

### serial 2

AC_DEFUN([AX_PROG_FC_MPI], [
AC_PREREQ(2.50)

# Check for compiler
# Needs to be split off into an extra macro to ensure right expansion
# order.
AC_REQUIRE([_AX_PROG_FC_MPI],[_AX_PROG_FC_MPI([$1])])

AS_IF([test x"$_ax_prog_fc_mpi_mpi_wanted" = xno],
  [ _ax_prog_fc_mpi_mpi_found=no ],
  [
    AC_LANG_PUSH([Fortran])

    # test whether MPI_INIT is available
    # We do not use AC_SEARCH_LIBS here, as it caches its outcome and
    # thus disallows corresponding calls in the other AX_PROG_*_MPI
    # macros.
    for lib in NONE mpichf90 fmpi fmpich; do
      save_LIBS=$LIBS
      if test x"$lib" = xNONE; then
        AC_MSG_CHECKING([for function MPI_INIT])
      else
        AC_MSG_CHECKING([for function MPI_INIT in -l$lib])
        LIBS="-l$lib $LIBS"
      fi
      AC_LINK_IFELSE([AC_LANG_CALL([],[MPI_INIT])],
        [ _ax_prog_fc_mpi_mpi_found=yes ],
        [ _ax_prog_fc_mpi_mpi_found=no ])
      AC_MSG_RESULT($_ax_prog_fc_mpi_mpi_found)
      if test "x$_ax_prog_fc_mpi_mpi_found" = "xyes"; then
        break;
      fi
      LIBS=$save_LIBS
    done

    # Check for header
    AS_IF([test x"$_ax_prog_fc_mpi_mpi_found" = xyes], [
      AC_MSG_CHECKING([for mpif.h])
      AC_COMPILE_IFELSE([AC_LANG_PROGRAM(,[[
      include 'mpif.h'
]])],
        [ AC_MSG_RESULT(yes)],
        [ AC_MSG_RESULT(no)
	  _ax_prog_fc_mpi_mpi_found=no
      ])
    ])
    AC_LANG_POP([Fortran])
])

# Finally, execute ACTION-IF-FOUND/ACTION-IF-NOT-FOUND:
AS_IF([test x"$_ax_prog_fc_mpi_mpi_found" = xyes], [
        ifelse([$2],,[AC_DEFINE(HAVE_MPI,1,[Define if you have the MPI library.])],[$2])
        :
],[
        $3
        :
])

])dnl AX_PROG_FC_MPI

dnl _AX_PROG_FC_MPI is an internal macro required by AX_PROG_FC_MPI.
dnl To ensure the right expansion order, the main function AX_PROG_FC_MPI
dnl has to be split into two parts. This part looks for the MPI
dnl compiler, while the other one tests whether an MPI program can be
dnl compiled.
dnl
AC_DEFUN([_AX_PROG_FC_MPI], [
  AC_ARG_VAR(MPIFC,[MPI Fortran compiler command])
  ifelse([$1],,[_ax_prog_fc_mpi_mpi_wanted=yes],[
    AC_MSG_CHECKING([whether to compile using MPI])
    if $1; then
      _ax_prog_fc_mpi_mpi_wanted=yes
    else
      _ax_prog_fc_mpi_mpi_wanted=no
    fi
    AC_MSG_RESULT($_ax_prog_fc_mpi_mpi_wanted)
  ])
  if test x"$_ax_prog_fc_mpi_mpi_wanted" = xyes; then
    if test -z "$FC" && test -n "$MPIFC"; then
      FC="$MPIFC"
    else
      AC_CHECK_TOOLS([FC], [mpif95 mpxlf95_r mpxlf95 ftn mpif90 mpxlf90_r mpxlf90 mpf90 cmpif90c sxmpif90 mpif77 hf77 mpxlf_r mpxlf mpifrt mpf77 cmpifc xlf95 pgf95 pathf95 ifort g95 f95 fort ifc efc openf95 sunf95 crayftn gfortran lf95 ftn xlf90 f90 pgf90 pghpf pathf90 epcf90 sxf90 openf90 sunf90 xlf f77 frt pgf77 pathf77 g77 cf77 fort77 fl32 af77])
    fi
  fi
  AC_PROG_FC
])dnl _AX_PROG_FC_MPI


AC_DEFUN([AY_CHECK_CXXFLAG], 
[dnl 
  AC_MSG_CHECKING([if $CXX supports $1])
  AC_LANG_PUSH([C++])
  ac_saved_cxxflags="$CXXFLAGS"
  CXXFLAGS="$1"
  AC_COMPILE_IFELSE([AC_LANG_PROGRAM([])],
    [AC_MSG_RESULT([yes])]
    [$2],
    [AC_MSG_RESULT([no])]
  )
  CXXFLAGS="$ac_saved_cxxflags"
  AC_LANG_POP([C++])
])


AC_DEFUN([AY_CHECK_FCFLAG], 
[dnl 
  AC_MSG_CHECKING([if $FC supports $1])
  AC_LANG_PUSH([Fortran])
  ac_saved_cxxflags="$FCFLAGS"
  FCFLAGS="$1"
  AC_COMPILE_IFELSE([AC_LANG_PROGRAM([])],
    [AC_MSG_RESULT([yes])]
    [$2],
    [AC_MSG_RESULT([no])]
  )
  FCFLAGS="$ac_saved_cxxflags"
  AC_LANG_POP([Fortran])
])


AC_DEFUN([AY_CHECK_CFLAG], 
[dnl 
  AC_MSG_CHECKING([if $CC supports $1])
  AC_LANG_PUSH([C])
  ac_saved_cxxflags="$CFLAGS"
  CFLAGS="$1"
  AC_COMPILE_IFELSE([AC_LANG_PROGRAM([])],
    [AC_MSG_RESULT([yes])]
    [$2],
    [AC_MSG_RESULT([no])]
  )
  CFLAGS="$ac_saved_cxxflags"
  AC_LANG_POP([C])
])


dnl =====================================================================



AC_DEFUN([AY_OPT_CXXFLAGS],
[
  have_oflag="no"
  OPT_CXXFLAGS=""
  m4_foreach([flag], 
    [
[-Ofast], dnl
[-O3 -ffast-math], [-O3], dnl 
[-O2 -ffast-math], [-O2] dnl
],
    [
      AS_IF([test "x$have_oflag" = "xno"],
        [ AY_CHECK_CXXFLAG([$OPT_CXXFLAGS flag],
            [have_oflag="yes"]
            [OPT_CXXFLAGS+=" flag"]) 
        ])
    ])

  m4_foreach([flag], 
    [dnl
dnl intel flags
[-xhost -static -use-intel-optimized-headers], [-xhost -static],dnl
[-xhost], [-ftz], [-r8], [-align], [-no-prec-div],dnl
[-assume norealloc_lhs,nodummy_aliases,noprotect_parens],dnl
[-std=c++0x], [-wd981,1419],dnl
[-march=native], [-mtune=native], [-ansi], dnl
[-pedantic-errors], [-Wall], [-Wextra] dnl
],
    [
      AY_CHECK_CXXFLAG([$OPT_CXXFLAGS flag],
        [OPT_CXXFLAGS+=" flag"]) 
    ])
  
  AC_SUBST([OPT_CXXFLAGS])
])dnl


AC_DEFUN([AY_OPT_FCFLAGS],
[
  have_oflag="no"
  OPT_FCFLAGS=""
  m4_foreach([flag], 
    [
[-Ofast], dnl
[-O3 -ffast-math], [-O3], dnl 
[-O2 -ffast-math], [-O2] dnl
],
    [
      AS_IF([test "x$have_oflag" = "xno"],
        [ AY_CHECK_CXXFLAG([$OPT_FCFLAGS flag],
            [have_oflag="yes"]
            [OPT_FCFLAGS+=" flag"]) 
        ])
    ])

  m4_foreach([flag], 
    [dnl
dnl intel flags
[-xhost -static],dnl
[-xhost], [-ftz], [-r8], [-align], [-no-prec-div],[-implicitnone],dnl
[-assume norealloc_lhs,nodummy_aliases,noprotect_parens],dnl
[-march=native], [-mtune=native], dnl
[-std=f2003], [-fall-intrinsics], [-Wall], [-Wextra], [-fimplicit-none],dnl
[-Wampersand],[-Wcharacter-truncation], [-ffree-form], [-fno-sign-zero], dnl
],
    [
      AY_CHECK_FCFLAG([$OPT_FCFLAGS flag],
        [OPT_FCFLAGS+=" flag"]) 
    ])
  
  AC_SUBST([OPT_FCFLAGS])
])dnl



AC_DEFUN([AY_OPT_CFLAGS],
[
  have_oflag="no"
  OPT_CFLAGS=""
  m4_foreach([flag], 
    [
[-Ofast], dnl
[-O3 -ffast-math], [-O3], dnl 
[-O2 -ffast-math], [-O2] dnl
],
    [
      AS_IF([test "x$have_oflag" = "xno"],
        [ AY_CHECK_CXXFLAG([$OPT_CFLAGS flag],
            [have_oflag="yes"]
            [OPT_CFLAGS+=" flag"]) 
        ])
    ])

  m4_foreach([flag], 
    [dnl
dnl intel flags
[-xhost -static],dnl
[-xhost], [-ftz], [-r8], [-align], [-no-prec-div],[-implicitnone],dnl
[-assume norealloc_lhs,nodummy_aliases,noprotect_parens],dnl
[-march=native], [-mtune=native], dnl
[-std=c99], [-fall-intrinsics], [-Wall], [-Wextra], [-fno-sign-zero], dnl
],
    [
      AY_CHECK_CFLAG([$OPT_CFLAGS flag],
        [OPT_CFLAGS+=" flag"]) 
    ])
  
  AC_SUBST([OPT_CFLAGS])
])dnl



dnl =====================================================================

AC_DEFUN([AY_DEBUG_CXXFLAGS],
[
  have_oflag="no"
  DEBUG_CXXFLAGS=""
  m4_foreach([flag], 
    [
[-Og], dnl
[-O1], [-O2], dnl 
],
    [
      AS_IF([test "x$have_oflag" = "xno"],
        [ AY_CHECK_CXXFLAG([$DEBUG_CXXFLAGS flag],
            [have_oflag="yes"]
            [DEBUG_CXXFLAGS+=" flag"]) 
        ])
    ])

  m4_foreach([flag], 
    [dnl
dnl intel flags
[-g], [-ansi], [-ansi-alias], [-std=c++0x], [-warn all], [-debug all] [-traceback], [-wd981,1419],dnl
[-pedantic-errors], [-Wall], [-Wextra], dnl
[-ftree-vrp], [-fbounds-check], [-fstack-protector-all],[-Wformat],[-Wnarrowing]
],
    [
      AY_CHECK_CXXFLAG([$DEBUG_CXXFLAGS flag],
        [DEBUG_CXXFLAGS+=" flag"]) 
    ])
  
  AC_SUBST([DEBUG_CXXFLAGS])
])dnl


AC_DEFUN([AY_DEBUG_FCFLAGS],
[
  have_oflag="no"
  DEBUG_FCFLAGS=""
  m4_foreach([flag], 
    [
[-Og], dnl
[-O1], [-O2], dnl 
],
    [
      AS_IF([test "x$have_oflag" = "xno"],
        [ AY_CHECK_CXXFLAG([$DEBUG_FCFLAGS flag],
            [have_oflag="yes"]
            [DEBUG_FCFLAGS+=" flag"]) 
        ])
    ])

  m4_foreach([flag], 
    [dnl
dnl intel flags
[-g],[-implicitnone],dnl
[-check bounds,format,output_conversion,pointers,uninit],dnl
[-warn all], [-debug all], [-traceback],dnl
[-fimplicit-none],[-std=f2003],[-fall-intrinsics],[-fbacktrace],[-fdump-core],[-ggdb],[-Wall],[-Wextra],[-Wampersand],[-Wcharacter-truncation],[-ffree-form],[-fno-sign-zero]dnl
],
    [
      AY_CHECK_FCFLAG([$DEBUG_FCFLAGS flag],
        [DEBUG_FCFLAGS+=" flag"]) 
    ])
  
  AC_SUBST([DEBUG_FCFLAGS])
])dnl



AC_DEFUN([AY_DEBUG_CFLAGS],
[
  have_oflag="no"
  DEBUG_CFLAGS=""
  m4_foreach([flag], 
    [
[-Og], dnl
[-O1], [-O2], dnl 
],
    [
      AS_IF([test "x$have_oflag" = "xno"],
        [ AY_CHECK_CXXFLAG([$DEBUG_CFLAGS flag],
            [have_oflag="yes"]
            [DEBUG_CFLAGS+=" flag"]) 
        ])
    ])

  m4_foreach([flag], 
    [dnl
dnl intel flags
[-g], [-ansi], [-ansi-alias], [-std=c99], [-warn all], [-debug all] [-traceback], [-wd981,1419],dnl
[-pedantic-errors], [-Wall], [-Wextra], dnl
[-ftree-vrp], [-fbounds-check], [-fstack-protector-all],[-Wformat],[-Wnarrowing]
],
    [
      AY_CHECK_CFLAG([$DEBUG_CFLAGS flag],
        [DEBUG_CFLAGS+=" flag"]) 
    ])
  
  AC_SUBST([DEBUG_CFLAGS])
])dnl







dnl ============================================================================

AC_INIT([tdbsc-examples], [0.1],[],[tdbsc-examples])

AC_CONFIG_AUX_DIR(.)
AM_INIT_AUTOMAKE([1.10 -Wall no-define foreign tar-pax subdir-objects])
AM_SILENT_RULES


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

AC_FC_LIBRARY_LDFLAGS
LT_INIT
AM_PATH_PYTHON

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



################################################################################
### BEGIN CHECK FOR python_devel
################################################################################

# ===========================================================================
#      http://www.gnu.org/software/autoconf-archive/ax_python_devel.html
# ===========================================================================
#
# SYNOPSIS
#
#   AX_PYTHON_DEVEL([version])
#
# DESCRIPTION
#
#   Note: Defines as a precious variable "PYTHON_VERSION". Don't override it
#   in your configure.ac.
#
#   This macro checks for Python and tries to get the include path to
#   'Python.h'. It provides the $(PYTHON_CPPFLAGS) and $(PYTHON_LDFLAGS)
#   output variables. It also exports $(PYTHON_EXTRA_LIBS) and
#   $(PYTHON_EXTRA_LDFLAGS) for embedding Python in your code.
#
#   You can search for some particular version of Python by passing a
#   parameter to this macro, for example ">= '2.3.1'", or "== '2.4'". Please
#   note that you *have* to pass also an operator along with the version to
#   match, and pay special attention to the single quotes surrounding the
#   version number. Don't use "PYTHON_VERSION" for this: that environment
#   variable is declared as precious and thus reserved for the end-user.
#
#   This macro should work for all versions of Python >= 2.1.0. As an end
#   user, you can disable the check for the python version by setting the
#   PYTHON_NOVERSIONCHECK environment variable to something else than the
#   empty string.
#
#   If you need to use this macro for an older Python version, please
#   contact the authors. We're always open for feedback.
#
# LICENSE
#
#   Copyright (c) 2009 Sebastian Huber <sebastian-huber@web.de>
#   Copyright (c) 2009 Alan W. Irwin
#   Copyright (c) 2009 Rafael Laboissiere <rafael@laboissiere.net>
#   Copyright (c) 2009 Andrew Collier
#   Copyright (c) 2009 Matteo Settenvini <matteo@member.fsf.org>
#   Copyright (c) 2009 Horst Knorr <hk_classes@knoda.org>
#   Copyright (c) 2013 Daniel Mullner <muellner@math.stanford.edu>
#
#   This program is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by the
#   Free Software Foundation, either version 3 of the License, or (at your
#   option) any later version.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
#   Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program. If not, see <http://www.gnu.org/licenses/>.
#
#   As a special exception, the respective Autoconf Macro's copyright owner
#   gives unlimited permission to copy, distribute and modify the configure
#   scripts that are the output of Autoconf when processing the Macro. You
#   need not follow the terms of the GNU General Public License when using
#   or distributing such scripts, even though portions of the text of the
#   Macro appear in them. The GNU General Public License (GPL) does govern
#   all other use of the material that constitutes the Autoconf Macro.
#
#   This special exception to the GPL applies to versions of the Autoconf
#   Macro released by the Autoconf Archive. When you make and distribute a
#   modified version of the Autoconf Macro, you may extend this special
#   exception to the GPL to apply to your modified version as well.

### serial 16

AU_ALIAS([AC_PYTHON_DEVEL], [AX_PYTHON_DEVEL])
AC_DEFUN([AX_PYTHON_DEVEL],[
	#
	# Allow the use of a (user set) custom python version
	#
	AC_ARG_VAR([PYTHON_VERSION],[The installed Python
		version to use, for example '2.3'. This string
		will be appended to the Python interpreter
		canonical name.])

	AC_PATH_PROG([PYTHON],[python[$PYTHON_VERSION]])
	if test -z "$PYTHON"; then
	   AC_MSG_ERROR([Cannot find python$PYTHON_VERSION in your system path])
	   PYTHON_VERSION=""
	fi

	#
	# Check for a version of Python >= 2.1.0
	#
	AC_MSG_CHECKING([for a version of Python >= '2.1.0'])
	ac_supports_python_ver=`$PYTHON -c "import sys; \
		ver = sys.version.split ()[[0]]; \
		print (ver >= '2.1.0')"`
	if test "$ac_supports_python_ver" != "True"; then
		if test -z "$PYTHON_NOVERSIONCHECK"; then
			AC_MSG_RESULT([no])
			AC_MSG_FAILURE([
This version of the AC@&t@_PYTHON_DEVEL macro
doesn't work properly with versions of Python before
2.1.0. You may need to re-run configure, setting the
variables PYTHON_CPPFLAGS, PYTHON_LDFLAGS, PYTHON_SITE_PKG,
PYTHON_EXTRA_LIBS and PYTHON_EXTRA_LDFLAGS by hand.
Moreover, to disable this check, set PYTHON_NOVERSIONCHECK
to something else than an empty string.
])
		else
			AC_MSG_RESULT([skip at user request])
		fi
	else
		AC_MSG_RESULT([yes])
	fi

	#
	# if the macro parameter ``version'' is set, honour it
	#
	if test -n "$1"; then
		AC_MSG_CHECKING([for a version of Python $1])
		ac_supports_python_ver=`$PYTHON -c "import sys; \
			ver = sys.version.split ()[[0]]; \
			print (ver $1)"`
		if test "$ac_supports_python_ver" = "True"; then
		   AC_MSG_RESULT([yes])
		else
			AC_MSG_RESULT([no])
			AC_MSG_ERROR([this package requires Python $1.
If you have it installed, but it isn't the default Python
interpreter in your system path, please pass the PYTHON_VERSION
variable to configure. See ``configure --help'' for reference.
])
			PYTHON_VERSION=""
		fi
	fi

	#
	# Check if you have distutils, else fail
	#
	AC_MSG_CHECKING([for the distutils Python package])
	ac_distutils_result=`$PYTHON -c "import distutils" 2>&1`
	if test -z "$ac_distutils_result"; then
		AC_MSG_RESULT([yes])
	else
		AC_MSG_RESULT([no])
		AC_MSG_ERROR([cannot import Python module "distutils".
Please check your Python installation. The error was:
$ac_distutils_result])
		PYTHON_VERSION=""
	fi

	#
	# Check for Python include path
	#
	AC_MSG_CHECKING([for Python include path])
	if test -z "$PYTHON_CPPFLAGS"; then
		python_path=`$PYTHON -c "import distutils.sysconfig; \
			print (distutils.sysconfig.get_python_inc ());"`
		plat_python_path=`$PYTHON -c "import distutils.sysconfig; \
			print (distutils.sysconfig.get_python_inc (plat_specific=1));"`
		if test -n "${python_path}"; then
			if test "${plat_python_path}" != "${python_path}"; then
				python_path="-I$python_path -I$plat_python_path"
			else
				python_path="-I$python_path"
			fi
		fi
		PYTHON_CPPFLAGS=$python_path
	fi
	AC_MSG_RESULT([$PYTHON_CPPFLAGS])
	AC_SUBST([PYTHON_CPPFLAGS])

	#
	# Check for Python library path
	#
	AC_MSG_CHECKING([for Python library path])
	if test -z "$PYTHON_LDFLAGS"; then
		# (makes two attempts to ensure we've got a version number
		# from the interpreter)
		ac_python_version=`cat<<EOD | $PYTHON -

# join all versioning strings, on some systems
# major/minor numbers could be in different list elements
from distutils.sysconfig import *
e = get_config_var('VERSION')
if e is not None:
	print(e)
EOD`

		if test -z "$ac_python_version"; then
			if test -n "$PYTHON_VERSION"; then
				ac_python_version=$PYTHON_VERSION
			else
				ac_python_version=`$PYTHON -c "import sys; \
					print (sys.version[[:3]])"`
			fi
		fi

		# Make the versioning information available to the compiler
		AC_DEFINE_UNQUOTED([HAVE_PYTHON], ["$ac_python_version"],
                                   [If available, contains the Python version number currently in use.])

		# First, the library directory:
		ac_python_libdir=`cat<<EOD | $PYTHON -

# There should be only one
import distutils.sysconfig
e = distutils.sysconfig.get_config_var('LIBDIR')
if e is not None:
	print (e)
EOD`

		# Now, for the library:
		ac_python_library=`cat<<EOD | $PYTHON -

import distutils.sysconfig
c = distutils.sysconfig.get_config_vars()
if 'LDVERSION' in c:
	print ('python'+c[['LDVERSION']])
else:
	print ('python'+c[['VERSION']])
EOD`

		# This small piece shamelessly adapted from PostgreSQL python macro;
		# credits goes to momjian, I think. I'd like to put the right name
		# in the credits, if someone can point me in the right direction... ?
		#
		if test -n "$ac_python_libdir" -a -n "$ac_python_library"
		then
			# use the official shared library
			ac_python_library=`echo "$ac_python_library" | sed "s/^lib//"`
			PYTHON_LDFLAGS="-L$ac_python_libdir -l$ac_python_library"
		else
			# old way: use libpython from python_configdir
			ac_python_libdir=`$PYTHON -c \
			  "from distutils.sysconfig import get_python_lib as f; \
			  import os; \
			  print (os.path.join(f(plat_specific=1, standard_lib=1), 'config'));"`
			PYTHON_LDFLAGS="-L$ac_python_libdir -lpython$ac_python_version"
		fi

		if test -z "PYTHON_LDFLAGS"; then
			AC_MSG_ERROR([
  Cannot determine location of your Python DSO. Please check it was installed with
  dynamic libraries enabled, or try setting PYTHON_LDFLAGS by hand.
			])
		fi
	fi
	AC_MSG_RESULT([$PYTHON_LDFLAGS])
	AC_SUBST([PYTHON_LDFLAGS])

	#
	# Check for site packages
	#
	AC_MSG_CHECKING([for Python site-packages path])
	if test -z "$PYTHON_SITE_PKG"; then
		PYTHON_SITE_PKG=`$PYTHON -c "import distutils.sysconfig; \
			print (distutils.sysconfig.get_python_lib(0,0));"`
	fi
	AC_MSG_RESULT([$PYTHON_SITE_PKG])
	AC_SUBST([PYTHON_SITE_PKG])

	#
	# libraries which must be linked in when embedding
	#
	AC_MSG_CHECKING(python extra libraries)
	if test -z "$PYTHON_EXTRA_LIBS"; then
	   PYTHON_EXTRA_LIBS=`$PYTHON -c "import distutils.sysconfig; \
                conf = distutils.sysconfig.get_config_var; \
                print (conf('LIBS'))"`
	fi
	AC_MSG_RESULT([$PYTHON_EXTRA_LIBS])
	AC_SUBST(PYTHON_EXTRA_LIBS)

	#
	# linking flags needed when embedding
	#
	AC_MSG_CHECKING(python extra linking flags)
	if test -z "$PYTHON_EXTRA_LDFLAGS"; then
		PYTHON_EXTRA_LDFLAGS=`$PYTHON -c "import distutils.sysconfig; \
			conf = distutils.sysconfig.get_config_var; \
			print (conf('LINKFORSHARED'))"`
	fi
	AC_MSG_RESULT([$PYTHON_EXTRA_LDFLAGS])
	AC_SUBST(PYTHON_EXTRA_LDFLAGS)

	#
	# final check to see if everything compiles alright
	#
	AC_MSG_CHECKING([consistency of all components of python development environment])
	# save current global flags
	ac_save_LIBS="$LIBS"
	ac_save_CPPFLAGS="$CPPFLAGS"
	LIBS="$ac_save_LIBS $PYTHON_LDFLAGS $PYTHON_EXTRA_LDFLAGS $PYTHON_EXTRA_LIBS"
	CPPFLAGS="$ac_save_CPPFLAGS $PYTHON_CPPFLAGS"
	AC_LANG_PUSH([C])
	AC_LINK_IFELSE([
		AC_LANG_PROGRAM([[#include <Python.h>]],
				[[Py_Initialize();]])
		],[pythonexists=yes],[pythonexists=no])
	AC_LANG_POP([C])
	# turn back to default flags
	CPPFLAGS="$ac_save_CPPFLAGS"
	LIBS="$ac_save_LIBS"

	AC_MSG_RESULT([$pythonexists])

        if test ! "x$pythonexists" = "xyes"; then
	   AC_MSG_FAILURE([
  Could not link test program to Python. Maybe the main Python library has been
  installed in some non-standard library path. If so, pass it to configure,
  via the LDFLAGS environment variable.
  Example: ./configure LDFLAGS="-L/usr/non-standard-path/python/lib"
  ============================================================================
   ERROR!
   You probably have to install the development version of the Python package
   for your distribution.  The exact name of this package varies among them.
  ============================================================================
	   ])
	  PYTHON_VERSION=""
	fi

	#
	# all done!
	#
])

AC_PYTHON_DEVEL([>= '2.6'])

################################################################################
### END CHECK FOR python_devel
################################################################################



################################################################################
### BEGIN CHECK FOR boost
################################################################################

# ===========================================================================
#       http://www.gnu.org/software/autoconf-archive/ax_boost_base.html
# ===========================================================================
#
# SYNOPSIS
#
#   AX_BOOST_BASE([MINIMUM-VERSION], [ACTION-IF-FOUND], [ACTION-IF-NOT-FOUND])
#
# DESCRIPTION
#
#   Test for the Boost C++ libraries of a particular version (or newer)
#
#   If no path to the installed boost library is given the macro searchs
#   under /usr, /usr/local, /opt and /opt/local and evaluates the
#   $BOOST_ROOT environment variable. Further documentation is available at
#   <http://randspringer.de/boost/index.html>.
#
#   This macro calls:
#
#     AC_SUBST(BOOST_CPPFLAGS) / AC_SUBST(BOOST_LDFLAGS)
#
#   And sets:
#
#     HAVE_BOOST
#
# LICENSE
#
#   Copyright (c) 2008 Thomas Porschberg <thomas@randspringer.de>
#   Copyright (c) 2009 Peter Adolphs
#
#   Copying and distribution of this file, with or without modification, are
#   permitted in any medium without royalty provided the copyright notice
#   and this notice are preserved. This file is offered as-is, without any
#   warranty.

### serial 20

AC_DEFUN([AX_BOOST_BASE],
[
AC_ARG_WITH([boost],
  [AS_HELP_STRING([--with-boost@<:@=ARG@:>@],
    [use Boost library from a standard location (ARG=yes),
     from the specified location (ARG=<path>),
     or disable it (ARG=no)
     @<:@ARG=yes@:>@ ])],
    [
    if test "$withval" = "no"; then
        want_boost="no"
    elif test "$withval" = "yes"; then
        want_boost="yes"
        ac_boost_path=""
    else
        want_boost="yes"
        ac_boost_path="$withval"
    fi
    ],
    [want_boost="yes"])


AC_ARG_WITH([boost-libdir],
        AS_HELP_STRING([--with-boost-libdir=LIB_DIR],
        [Force given directory for boost libraries. Note that this will override library path detection, so use this parameter only if default library detection fails and you know exactly where your boost libraries are located.]),
        [
        if test -d "$withval"
        then
                ac_boost_lib_path="$withval"
        else
                AC_MSG_ERROR(--with-boost-libdir expected directory name)
        fi
        ],
        [ac_boost_lib_path=""]
)

if test "x$want_boost" = "xyes"; then
    boost_lib_version_req=ifelse([$1], ,1.20.0,$1)
    boost_lib_version_req_shorten=`expr $boost_lib_version_req : '\([[0-9]]*\.[[0-9]]*\)'`
    boost_lib_version_req_major=`expr $boost_lib_version_req : '\([[0-9]]*\)'`
    boost_lib_version_req_minor=`expr $boost_lib_version_req : '[[0-9]]*\.\([[0-9]]*\)'`
    boost_lib_version_req_sub_minor=`expr $boost_lib_version_req : '[[0-9]]*\.[[0-9]]*\.\([[0-9]]*\)'`
    if test "x$boost_lib_version_req_sub_minor" = "x" ; then
        boost_lib_version_req_sub_minor="0"
        fi
    WANT_BOOST_VERSION=`expr $boost_lib_version_req_major \* 100000 \+  $boost_lib_version_req_minor \* 100 \+ $boost_lib_version_req_sub_minor`
    AC_MSG_CHECKING(for boostlib >= $boost_lib_version_req)
    succeeded=no

    dnl On 64-bit systems check for system libraries in both lib64 and lib.
    dnl The former is specified by FHS, but e.g. Debian does not adhere to
    dnl this (as it rises problems for generic multi-arch support).
    dnl The last entry in the list is chosen by default when no libraries
    dnl are found, e.g. when only header-only libraries are installed!
    libsubdirs="lib"
    ax_arch=`uname -m`
    if test $ax_arch = x86_64 -o $ax_arch = ppc64 -o $ax_arch = s390x -o $ax_arch = sparc64; then
        libsubdirs="lib64 lib lib64"
    fi

    dnl first we check the system location for boost libraries
    dnl this location ist chosen if boost libraries are installed with the --layout=system option
    dnl or if you install boost with RPM
    if test "$ac_boost_path" != ""; then
        BOOST_CPPFLAGS="-I$ac_boost_path/include"
        for ac_boost_path_tmp in $libsubdirs; do
                if test -d "$ac_boost_path"/"$ac_boost_path_tmp" ; then
                        BOOST_LDFLAGS="-L$ac_boost_path/$ac_boost_path_tmp"
                        break
                fi
        done
    elif test "$cross_compiling" != yes; then
        for ac_boost_path_tmp in /usr /usr/local /opt /opt/local ; do
            if test -d "$ac_boost_path_tmp/include/boost" && test -r "$ac_boost_path_tmp/include/boost"; then
                for libsubdir in $libsubdirs ; do
                    if ls "$ac_boost_path_tmp/$libsubdir/libboost_"* >/dev/null 2>&1 ; then break; fi
                done
                BOOST_LDFLAGS="-L$ac_boost_path_tmp/$libsubdir"
                BOOST_CPPFLAGS="-I$ac_boost_path_tmp/include"
                break;
            fi
        done
    fi

    dnl overwrite ld flags if we have required special directory with
    dnl --with-boost-libdir parameter
    if test "$ac_boost_lib_path" != ""; then
       BOOST_LDFLAGS="-L$ac_boost_lib_path"
    fi

    CPPFLAGS_SAVED="$CPPFLAGS"
    CPPFLAGS="$CPPFLAGS $BOOST_CPPFLAGS"
    export CPPFLAGS

    LDFLAGS_SAVED="$LDFLAGS"
    LDFLAGS="$LDFLAGS $BOOST_LDFLAGS"
    export LDFLAGS

    AC_REQUIRE([AC_PROG_CXX])
    AC_LANG_PUSH(C++)
        AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[
    @%:@include <boost/version.hpp>
    ]], [[
    #if BOOST_VERSION >= $WANT_BOOST_VERSION
    // Everything is okay
    #else
    #  error Boost version is too old
    #endif
    ]])],[
        AC_MSG_RESULT(yes)
    succeeded=yes
    found_system=yes
        ],[
        ])
    AC_LANG_POP([C++])



    dnl if we found no boost with system layout we search for boost libraries
    dnl built and installed without the --layout=system option or for a staged(not installed) version
    if test "x$succeeded" != "xyes"; then
        _version=0
        if test "$ac_boost_path" != ""; then
            if test -d "$ac_boost_path" && test -r "$ac_boost_path"; then
                for i in `ls -d $ac_boost_path/include/boost-* 2>/dev/null`; do
                    _version_tmp=`echo $i | sed "s#$ac_boost_path##" | sed 's/\/include\/boost-//' | sed 's/_/./'`
                    V_CHECK=`expr $_version_tmp \> $_version`
                    if test "$V_CHECK" = "1" ; then
                        _version=$_version_tmp
                    fi
                    VERSION_UNDERSCORE=`echo $_version | sed 's/\./_/'`
                    BOOST_CPPFLAGS="-I$ac_boost_path/include/boost-$VERSION_UNDERSCORE"
                done
            fi
        else
            if test "$cross_compiling" != yes; then
                for ac_boost_path in /usr /usr/local /opt /opt/local ; do
                    if test -d "$ac_boost_path" && test -r "$ac_boost_path"; then
                        for i in `ls -d $ac_boost_path/include/boost-* 2>/dev/null`; do
                            _version_tmp=`echo $i | sed "s#$ac_boost_path##" | sed 's/\/include\/boost-//' | sed 's/_/./'`
                            V_CHECK=`expr $_version_tmp \> $_version`
                            if test "$V_CHECK" = "1" ; then
                                _version=$_version_tmp
                                best_path=$ac_boost_path
                            fi
                        done
                    fi
                done

                VERSION_UNDERSCORE=`echo $_version | sed 's/\./_/'`
                BOOST_CPPFLAGS="-I$best_path/include/boost-$VERSION_UNDERSCORE"
                if test "$ac_boost_lib_path" = ""; then
                    for libsubdir in $libsubdirs ; do
                        if ls "$best_path/$libsubdir/libboost_"* >/dev/null 2>&1 ; then break; fi
                    done
                    BOOST_LDFLAGS="-L$best_path/$libsubdir"
                fi
            fi

            if test "x$BOOST_ROOT" != "x"; then
                for libsubdir in $libsubdirs ; do
                    if ls "$BOOST_ROOT/stage/$libsubdir/libboost_"* >/dev/null 2>&1 ; then break; fi
                done
                if test -d "$BOOST_ROOT" && test -r "$BOOST_ROOT" && test -d "$BOOST_ROOT/stage/$libsubdir" && test -r "$BOOST_ROOT/stage/$libsubdir"; then
                    version_dir=`expr //$BOOST_ROOT : '.*/\(.*\)'`
                    stage_version=`echo $version_dir | sed 's/boost_//' | sed 's/_/./g'`
                        stage_version_shorten=`expr $stage_version : '\([[0-9]]*\.[[0-9]]*\)'`
                    V_CHECK=`expr $stage_version_shorten \>\= $_version`
                    if test "$V_CHECK" = "1" -a "$ac_boost_lib_path" = "" ; then
                        AC_MSG_NOTICE(We will use a staged boost library from $BOOST_ROOT)
                        BOOST_CPPFLAGS="-I$BOOST_ROOT"
                        BOOST_LDFLAGS="-L$BOOST_ROOT/stage/$libsubdir"
                    fi
                fi
            fi
        fi

        CPPFLAGS="$CPPFLAGS $BOOST_CPPFLAGS"
        export CPPFLAGS
        LDFLAGS="$LDFLAGS $BOOST_LDFLAGS"
        export LDFLAGS

        AC_LANG_PUSH(C++)
            AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[
        @%:@include <boost/version.hpp>
        ]], [[
        #if BOOST_VERSION >= $WANT_BOOST_VERSION
        // Everything is okay
        #else
        #  error Boost version is too old
        #endif
        ]])],[
            AC_MSG_RESULT(yes)
        succeeded=yes
        found_system=yes
            ],[
            ])
        AC_LANG_POP([C++])
    fi

    if test "$succeeded" != "yes" ; then
        if test "$_version" = "0" ; then
            AC_MSG_NOTICE([[We could not detect the boost libraries (version $boost_lib_version_req_shorten or higher). If you have a staged boost library (still not installed) please specify \$BOOST_ROOT in your environment and do not give a PATH to --with-boost option.  If you are sure you have boost installed, then check your version number looking in <boost/version.hpp>. See http://randspringer.de/boost for more documentation.]])
        else
            AC_MSG_NOTICE([Your boost libraries seems to old (version $_version).])
        fi
        # execute ACTION-IF-NOT-FOUND (if present):
        ifelse([$3], , :, [$3])
    else
        AC_SUBST(BOOST_CPPFLAGS)
        AC_SUBST(BOOST_LDFLAGS)
        AC_DEFINE(HAVE_BOOST,,[define if the Boost library is available])
        # execute ACTION-IF-FOUND (if present):
        ifelse([$2], , :, [$2])
    fi

    CPPFLAGS="$CPPFLAGS_SAVED"
    LDFLAGS="$LDFLAGS_SAVED"
fi

])


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


################################################################################
### END CHECK FOR boost
################################################################################



################################################################################
### BEGIN CHECK FOR boost_python
################################################################################

# ===========================================================================
#      http://www.gnu.org/software/autoconf-archive/ax_boost_python.html
# ===========================================================================
#
# SYNOPSIS
#
#   AX_BOOST_PYTHON
#
# DESCRIPTION
#
#   This macro checks to see if the Boost.Python library is installed. It
#   also attempts to guess the correct library name using several attempts.
#   It tries to build the library name using a user supplied name or suffix
#   and then just the raw library.
#
#   If the library is found, HAVE_BOOST_PYTHON is defined and
#   BOOST_PYTHON_LIB is set to the name of the library.
#
#   This macro calls AC_SUBST(BOOST_PYTHON_LIB).
#
#   In order to ensure that the Python headers and the Boost libraries are
#   specified on the include path, this macro requires AX_PYTHON_DEVEL and
#   AX_BOOST_BASE to be called.
#
# LICENSE
#
#   Copyright (c) 2008 Michael Tindal
#   Copyright (c) 2013 Daniel Mullner <muellner@math.stanford.edu>
#
#   This program is free software; you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by the
#   Free Software Foundation; either version 2 of the License, or (at your
#   option) any later version.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
#   Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program. If not, see <http://www.gnu.org/licenses/>.
#
#   As a special exception, the respective Autoconf Macro's copyright owner
#   gives unlimited permission to copy, distribute and modify the configure
#   scripts that are the output of Autoconf when processing the Macro. You
#   need not follow the terms of the GNU General Public License when using
#   or distributing such scripts, even though portions of the text of the
#   Macro appear in them. The GNU General Public License (GPL) does govern
#   all other use of the material that constitutes the Autoconf Macro.
#
#   This special exception to the GPL applies to versions of the Autoconf
#   Macro released by the Autoconf Archive. When you make and distribute a
#   modified version of the Autoconf Macro, you may extend this special
#   exception to the GPL to apply to your modified version as well.

### serial 18

AC_DEFUN([AX_BOOST_PYTHON],
[AC_REQUIRE([AX_PYTHON_DEVEL])dnl
AC_CACHE_CHECK(whether the Boost::Python library is available,
ac_cv_boost_python,
[AC_LANG_SAVE
 AC_LANG_CPLUSPLUS
 CPPFLAGS_SAVE="$CPPFLAGS"
 if test x$PYTHON_CPPFLAGS != x; then
   CPPFLAGS="$PYTHON_CPPFLAGS $CPPFLAGS"
 fi
 AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[
 #include <boost/python/module.hpp>
 using namespace boost::python;
 BOOST_PYTHON_MODULE(test) { throw "Boost::Python test."; }]],
	[[return 0;]])],
	ac_cv_boost_python=yes, ac_cv_boost_python=no)
 AC_LANG_RESTORE
 CPPFLAGS="$CPPFLAGS_SAVE"
])
if test "$ac_cv_boost_python" = "yes"; then
  AC_DEFINE(HAVE_BOOST_PYTHON,,[define if the Boost::Python library is available])
  ax_python_lib=boost_python
  AC_ARG_WITH([boost-python],AS_HELP_STRING([--with-boost-python],[specify yes/no or the boost python library or suffix to use]),
  [if test "x$with_boost_python" != "xno"; then
     ax_python_lib=$with_boost_python
     ax_boost_python_lib=boost_python-$with_boost_python
   fi])
  BOOSTLIBDIR=`echo $BOOST_LDFLAGS | sed -e 's/@<:@^\/@:>@*//'`
  for ax_lib in `ls $BOOSTLIBDIR/libboost_python*.so* $BOOSTLIBDIR/libboost_python*.dylib* $BOOSTLIBDIR/libboost_python*.a* 2>/dev/null | sed 's,.*/,,' | sed -e 's;^lib\(boost_python.*\)\.so.*$;\1;' -e 's;^lib\(boost_python.*\)\.dylib.*$;\1;' -e 's;^lib\(boost_python.*\)\.a.*$;\1;' ` $ax_python_lib $ax_boost_python_lib boost_python; do
    AC_CHECK_LIB($ax_lib, exit, [BOOST_PYTHON_LIB=-l$ax_lib break], , [$PYTHON_LDFLAGS])
  done
  AC_SUBST(BOOST_PYTHON_LIB)
fi
])dnl


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


################################################################################
### END CHECK FOR boost_python
################################################################################



################################################################################
### BEGIN CHECK FOR fftw3
################################################################################


AC_ARG_VAR(FFTW3_LIBS,-lfftw3 (default); Serial fftw3 libraries)
if test "x$FFTW3_LIBS" = "x"; then
   FFTW3_LIBS="-lfftw3"
   AC_SUBST([FFTW3_LIBS])
fi



################### HEADER TEST fftw3.h

saved_CFLAGS="$CFLAGS"
saved_FCFLAGS="$FCFLAGS"
saved_CXXFLAGS="$CXXFLAGS"
saved_CPPFLAGS="$CPPFLAGS"
saved_LDFLAGS="$LDFLAGS"
saved_LIBS="$LIBS"
CPPFLAGS+=" $AM_CPPFLAGS"
LDFLAGS+=" $AM_LDFLAGS"

AC_LANG_PUSH([C++])

AC_CHECK_HEADER(
  [fftw3.h],
  [

  ], dnl AC_CHECK_HEADER ok
  [
AC_MSG_ERROR([

THE HEADER FILE fftw3.h COULD NOT BE FOUND

This may mean that either:

(*) Library "fftw3" is installed in a nonstandard location

    In this case, locate /path/to/include/fftw3.h on your computer 
    and reconfigure with
    ./configure CPPFLAGS="-I/path/to/include \$CPPFLAGS"

    On some supercomputers, you may have to "module load" a package to make it
    available for use.  If you have the module command, then try typing
    "module list" to see if fftw3 is a loadable module.
    Upon loading, you can use "module show" to help find /path/to/include

    On most machines, you can type "locate 'fftw3.h'" to find a file;
    however, this rarely works to locate files mounted on a network filesystem.
    The printed results of the locate command may be out-of-date as well.
    To update the database that the locate command uses, try "sudo updatedb"

(*) Library "fftw3" is not installed, and you need to install it

])
  ] dnl AC_CHECK_HEADER failed
) dnl AC_CHECK_HEADER
AC_LANG_POP([C++])

CFLAGS=$saved_CFLAGS
FCFLAGS=$saved_FCFLAGS
CXXFLAGS=$saved_CXXFLAGS
CPPFLAGS=$saved_CPPFLAGS
LDFLAGS=$saved_LDFLAGS
LIBS=$saved_LIBS

AC_MSG_CHECKING([serial compilation linked to $(eval echo ${FFTW3_LIBS})])

################### LINK TEST TO ${FFTW3_LIBS}

saved_CFLAGS="$CFLAGS"
saved_FCFLAGS="$FCFLAGS"
saved_CXXFLAGS="$CXXFLAGS"
saved_CPPFLAGS="$CPPFLAGS"
saved_LDFLAGS="$LDFLAGS"
saved_LIBS="$LIBS"
CPPFLAGS+=" $AM_CPPFLAGS"
LDFLAGS+=" $AM_LDFLAGS"

AC_LANG_PUSH([C++])
LIBS+=" ${FFTW3_LIBS}"
AC_LINK_IFELSE(
  [AC_LANG_PROGRAM(
     [

#include <fftw3.h>

     ], dnl preamble
     [

fftw_malloc(3);

     ]  dnl body
     )], dnl AC_LANG_TEST
  [
AC_MSG_RESULT([yes])
atp_test_failed=no
  ], dnl ok
  [
AC_MSG_RESULT([no])
atp_test_failed=yes
  ] dnl failure
) dnl AC_LINK_IFELSE
AC_LANG_POP([C++])

CFLAGS=$saved_CFLAGS
FCFLAGS=$saved_FCFLAGS
CXXFLAGS=$saved_CXXFLAGS
CPPFLAGS=$saved_CPPFLAGS
LDFLAGS=$saved_LDFLAGS
LIBS=$saved_LIBS

AS_IF( [test "x$atp_test_failed" != "xno"],
[
AC_MSG_ERROR([

FAILED TO LINK AGAINST ${FFTW3_LIBS}

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
])
]) dnl failbit was on

################################################################################
### END CHECK FOR fftw3
################################################################################



################################################################################
### BEGIN CHECK FOR fftw3 OPENMP
################################################################################

if test "x$with_openmp" != "xno"; then


AC_ARG_VAR(FFTW3_OPENMP_LIBS,-lfftw3_omp -lfftw3 (default); OpenMP fftw3 libraries)
if test "x$FFTW3_OPENMP_LIBS" = "x"; then
   FFTW3_OPENMP_LIBS="-lfftw3_omp -lfftw3"
   AC_SUBST([FFTW3_OPENMP_LIBS])
fi



################### HEADER TEST fftw3.h

saved_CFLAGS="$CFLAGS"
saved_FCFLAGS="$FCFLAGS"
saved_CXXFLAGS="$CXXFLAGS"
saved_CPPFLAGS="$CPPFLAGS"
saved_LDFLAGS="$LDFLAGS"
saved_LIBS="$LIBS"
CPPFLAGS+=" $AM_CPPFLAGS"
LDFLAGS+=" $AM_LDFLAGS"

AC_LANG_PUSH([C++])

AC_CHECK_HEADER(
  [fftw3.h],
  [

  ], dnl AC_CHECK_HEADER ok
  [
AC_MSG_ERROR([

THE HEADER FILE fftw3.h COULD NOT BE FOUND

This may mean that either:

(*) Library "fftw3" is installed in a nonstandard location

    In this case, locate /path/to/include/fftw3.h on your computer 
    and reconfigure with
    ./configure CPPFLAGS="-I/path/to/include \$CPPFLAGS"

    On some supercomputers, you may have to "module load" a package to make it
    available for use.  If you have the module command, then try typing
    "module list" to see if fftw3 is a loadable module.
    Upon loading, you can use "module show" to help find /path/to/include

    On most machines, you can type "locate 'fftw3.h'" to find a file;
    however, this rarely works to locate files mounted on a network filesystem.
    The printed results of the locate command may be out-of-date as well.
    To update the database that the locate command uses, try "sudo updatedb"

(*) Library "fftw3" is not installed, and you need to install it

])
  ] dnl AC_CHECK_HEADER failed
) dnl AC_CHECK_HEADER
AC_LANG_POP([C++])

CFLAGS=$saved_CFLAGS
FCFLAGS=$saved_FCFLAGS
CXXFLAGS=$saved_CXXFLAGS
CPPFLAGS=$saved_CPPFLAGS
LDFLAGS=$saved_LDFLAGS
LIBS=$saved_LIBS

AC_MSG_CHECKING([OpenMP compilation linked to $(eval echo ${FFTW3_OPENMP_LIBS})])

################### OPENMP LINK TEST TO ${FFTW3_OPENMP_LIBS}

saved_CFLAGS="$CFLAGS"
saved_FCFLAGS="$FCFLAGS"
saved_CXXFLAGS="$CXXFLAGS"
saved_CPPFLAGS="$CPPFLAGS"
saved_LDFLAGS="$LDFLAGS"
saved_LIBS="$LIBS"
CPPFLAGS+=" $AM_CPPFLAGS"
LDFLAGS+=" $AM_LDFLAGS"

CXXFLAGS+=" ${OPENMP_CXXFLAGS}"
AC_LANG_PUSH([C++])
LIBS+=" ${FFTW3_OPENMP_LIBS}"
AC_LINK_IFELSE(
  [AC_LANG_PROGRAM(
     [

#include <omp.h>
#include <fftw3.h>

     ], dnl preamble
     [

fftw_plan_with_nthreads( omp_get_max_threads() );
fftw_malloc(3);

     ]  dnl body
     )], dnl AC_LANG_TEST
  [
AC_MSG_RESULT([yes])
atp_test_failed=no
  ], dnl ok
  [
AC_MSG_RESULT([no])
atp_test_failed=yes
  ] dnl failure
) dnl AC_LINK_IFELSE
AC_LANG_POP([C++])

CFLAGS=$saved_CFLAGS
FCFLAGS=$saved_FCFLAGS
CXXFLAGS=$saved_CXXFLAGS
CPPFLAGS=$saved_CPPFLAGS
LDFLAGS=$saved_LDFLAGS
LIBS=$saved_LIBS

AS_IF( [test "x$atp_test_failed" != "xno"],
[
AC_MSG_ERROR([

FAILED TO LINK AGAINST ${FFTW3_OPENMP_LIBS}

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
])
]) dnl failbit was on

fi

################################################################################
### END CHECK FOR fftw3 OPENMP
################################################################################



################################################################################
### BEGIN CHECK FOR tdbsc
################################################################################


AC_ARG_VAR(TDBSC_LIBS,-ltdbsc (default); Serial tdbsc libraries)
if test "x$TDBSC_LIBS" = "x"; then
   TDBSC_LIBS="-ltdbsc"
   AC_SUBST([TDBSC_LIBS])
fi



################### HEADER TEST tdbsc/tdbsc.hpp

saved_CFLAGS="$CFLAGS"
saved_FCFLAGS="$FCFLAGS"
saved_CXXFLAGS="$CXXFLAGS"
saved_CPPFLAGS="$CPPFLAGS"
saved_LDFLAGS="$LDFLAGS"
saved_LIBS="$LIBS"
CPPFLAGS+=" $AM_CPPFLAGS"
LDFLAGS+=" $AM_LDFLAGS"

AC_LANG_PUSH([C++])

AC_CHECK_HEADER(
  [tdbsc/tdbsc.hpp],
  [

  ], dnl AC_CHECK_HEADER ok
  [
AC_MSG_ERROR([

THE HEADER FILE tdbsc/tdbsc.hpp COULD NOT BE FOUND

This may mean that either:

(*) Library "tdbsc" is installed in a nonstandard location

    In this case, locate /path/to/include/tdbsc/tdbsc.hpp on your computer 
    and reconfigure with
    ./configure CPPFLAGS="-I/path/to/include \$CPPFLAGS"

    On some supercomputers, you may have to "module load" a package to make it
    available for use.  If you have the module command, then try typing
    "module list" to see if tdbsc is a loadable module.
    Upon loading, you can use "module show" to help find /path/to/include

    On most machines, you can type "locate 'tdbsc/tdbsc.hpp'" to find a file;
    however, this rarely works to locate files mounted on a network filesystem.
    The printed results of the locate command may be out-of-date as well.
    To update the database that the locate command uses, try "sudo updatedb"

(*) Library "tdbsc" is not installed, and you need to install it

])
  ] dnl AC_CHECK_HEADER failed
) dnl AC_CHECK_HEADER
AC_LANG_POP([C++])

CFLAGS=$saved_CFLAGS
FCFLAGS=$saved_FCFLAGS
CXXFLAGS=$saved_CXXFLAGS
CPPFLAGS=$saved_CPPFLAGS
LDFLAGS=$saved_LDFLAGS
LIBS=$saved_LIBS

AC_MSG_CHECKING([serial compilation linked to $(eval echo ${TDBSC_LIBS})])

################### LINK TEST TO ${TDBSC_LIBS}

saved_CFLAGS="$CFLAGS"
saved_FCFLAGS="$FCFLAGS"
saved_CXXFLAGS="$CXXFLAGS"
saved_CPPFLAGS="$CPPFLAGS"
saved_LDFLAGS="$LDFLAGS"
saved_LIBS="$LIBS"
CPPFLAGS+=" $AM_CPPFLAGS"
LDFLAGS+=" $AM_LDFLAGS"

AC_LANG_PUSH([C++])
LIBS+=" ${TDBSC_LIBS}"
AC_LINK_IFELSE(
  [AC_LANG_PROGRAM(
     [
#include <tdbsc/tdbsc.hpp>
     ], dnl preamble
     [
int n = tdbsc_readdatasize_("filename");
     ]  dnl body
     )], dnl AC_LANG_TEST
  [
AC_MSG_RESULT([yes])
atp_test_failed=no
  ], dnl ok
  [
AC_MSG_RESULT([no])
atp_test_failed=yes
  ] dnl failure
) dnl AC_LINK_IFELSE
AC_LANG_POP([C++])

CFLAGS=$saved_CFLAGS
FCFLAGS=$saved_FCFLAGS
CXXFLAGS=$saved_CXXFLAGS
CPPFLAGS=$saved_CPPFLAGS
LDFLAGS=$saved_LDFLAGS
LIBS=$saved_LIBS

AS_IF( [test "x$atp_test_failed" != "xno"],
[
AC_MSG_ERROR([

FAILED TO LINK AGAINST ${TDBSC_LIBS}

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
])
]) dnl failbit was on

################################################################################
### END CHECK FOR tdbsc
################################################################################

AC_SUBST([AM_CPPFLAGS],["-I\$(top_builddir) -I\$(top_srcdir) $AM_CPPFLAGS"])
AC_CONFIG_FILES([Makefile])
AC_OUTPUT

