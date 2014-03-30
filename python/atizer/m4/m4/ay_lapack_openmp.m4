
#-------------------------------------------------------------------
#
# AY_LAPACK
#    Sets LAPACK_LIBS and LAPACK_OPENMP_LIBS or DIES
#

AC_DEFUN([AY_LAPACK_OPENMP],[
AC_REQUIRE([AY_LAPACK])dnl

   AC_ARG_VAR(LAPACK_OPENMP_LIBS,-llapack -lblas (default if MKL_HOME is unset); OpenMP lapack/blas libs)


  GNU_MKL_FLAGS="-m64 -Wl,--no-as-needed -Wl,--start-group  -lmkl_gf_lp64 -lmkl_sequential -lmkl_core -Wl,--end-group -lpthread -lm -ldl"
#-lm -lm $FC_RUNTIME_LIB"
  GNU_OMPMKL_FLAGS="-m64 -Wl,--no-as-needed -Wl,--start-group -lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -Wl,--end-group -liomp5 -lpthread -lm -ldl"
#-lm -lm $FC_RUNTIME_LIB"
  INTEL_MKL_FLAGS="-m64 -Wl,--start-group -lmkl_intel_lp64 -lmkl_sequential -lmkl_core -Wl,--end-group -lpthread -lm -ldl"
#-lm -lm $FC_RUNTIME_LIB"
  INTEL_OMPMKL_FLAGS="-m64 -Wl,--start-group -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core -Wl,--end-group -liomp5 -lpthread -lm -ldl"
#-lm -lm $FC_RUNTIME_LIB"

   HAVE_LAPACK="no"

############
   AC_LANG_PUSH([C])

   HAVE_OPENMP_LAPACK="no"
   AS_IF([test "x$LAPACK_OPENMP_LIBS" != "x"],
         [AC_MSG_CHECKING(LAPACK_OPENMP_LIBS)]
         [saved_libs="$LIBS"]
   	 [LIBS="$LIBS $LAPACK_LIBS $FCLIBS"]
   	 [
            AC_LINK_IFELSE(
               [AC_LANG_PROGRAM(  
                                  [extern "C" { char dgemm_(); }],
                                  [dgemm_()] 
                               )],
               [HAVE_OPENMP_LAPACK=yes]
   	       [AC_MSG_RESULT([yes])],
               [HAVE_OPENMP_LAPACK=no]
   	       [AC_MSG_RESULT([no])]
               [AC_MSG_WARN(User-supplied LAPACK_OPENMP_LIBS "$LAPACK_OPENMP_LIBS" did not compile)]
            )
         ]
         [LIBS="$saved_libs"]
   	)




   AS_IF([test "x$HAVE_OPENMP_LAPACK" = "xno"],
         [AC_MSG_CHECKING(mkl/gnu openmp LIBS)]
         [saved_libs="$LIBS"]
         [LIBS="$LIBS $GNU_OMPMKL_FLAGS $FCLIBS"]
         [
            AC_LINK_IFELSE(
               [AC_LANG_PROGRAM(  
                  [char dgemm_();],
                  [dgemm_()] 
               )],
               [LAPACK_OPENMP_LIBS="$GNU_OMPMKL_FLAGS"]
               [AC_SUBST([AM_CPPFLAGS],["$AM_CPPFLAGS -DMKL"])]
               [AC_MSG_RESULT([yes])],
               [LAPACK_OPENMP_LIBS="$LAPACK_LIBS"] 
               [AC_MSG_RESULT([no])]
	       [AC_MSG_WARN(Using serial lapack libraries for openmp compilation)]
            )
         ]
         [LIBS="$saved_libs"]
      )

   AC_SUBST(LAPACK_OPENMP_LIBS,["$LAPACK_OPENMP_LIBS"])
   AC_LANG_POP([C])
])
