
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
[-std=c99], [-Wall], [-Wextra], dnl
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




