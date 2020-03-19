
#-------------------------------------------------------------------
#
# AY_LAPACK
#    Sets LAPACK_LIBS and LAPACK_OPENMP_LIBS or DIES
#

AC_DEFUN([AY_LAPACK],[

   AC_ARG_VAR(MKL_HOME,Location of mkl libraries, if not already in your LD_LIBRARY_PATH, e.g. -L/opt/intel/mkl/lib)
   AS_IF([test "x$MKL_HOME" != "x"],[AM_LDFLAGS="$AM_LDFLAGS -L$MKL_HOME"])
   AC_ARG_VAR(LAPACK_LIBS,-llapack -lblas (default if MKL_HOME is unset); Serial lapack/blas libs)



  GNU_MKL_FLAGS="-m64 -Wl,--start-group  -lmkl_gf_lp64 -lmkl_sequential -lmkl_core -Wl,--end-group -lpthread -lm -ldl"
#-lm -lm $FC_RUNTIME_LIB"
  GNU_OMPMKL_FLAGS="-m64 -Wl,--start-group -lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -Wl,--end-group -liomp5 -lpthread -lm -ldl"
#-lm -lm $FC_RUNTIME_LIB"
  INTEL_MKL_FLAGS="-m64 -Wl,--start-group -lmkl_intel_lp64 -lmkl_sequential -lmkl_core -Wl,--end-group -lpthread -lm -ldl"
#-lm -lm $FC_RUNTIME_LIB"
  INTEL_OMPMKL_FLAGS="-m64 -Wl,--start-group -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core -Wl,--end-group -liomp5 -lpthread -lm -ldl"
#-lm -lm $FC_RUNTIME_LIB"

   HAVE_LAPACK="no"

   AC_LANG_PUSH([C])

   AS_IF([test "x$LAPACK_LIBS" != "x"],
         [AC_MSG_CHECKING(LAPACK_LIBS)]
         [saved_libs="$LIBS"]
	 [LIBS="$LIBS $LAPACK_LIBS $FCLIBS"]
	 [
            AC_LINK_IFELSE(
               [AC_LANG_PROGRAM(  
[
void dgesdd_(const char *jobz, const int *m, const int *n,double *a, const int *lda, double *s,double *u, const int *ldu,double *vt, const int *ldvt, double *work, const int *lwork, int *iwork, int *info);
],
[
  double * p = 0;
  double work = 0.;
  int lwork = -1;
  int iwork = 0;
  int info = 0;
  int M,N;
  dgesdd_("A",&M,&N,p,&M,p,p,&M,p,&N,&work,&lwork,&iwork,&info);
] 
                               )],
               [HAVE_LAPACK=yes]
	       [AC_MSG_RESULT([yes])],
               [HAVE_LAPACK=no]
	       [AC_MSG_RESULT([no])]
               [AC_MSG_WARN(User-supplied LAPACK_LIBS "$LAPACK_LIBS" did not compile)]
            )
         ]
         [LIBS="$saved_libs"]
	)

   AS_IF([test "x$HAVE_LAPACK" = "xno"],
         [AC_MSG_CHECKING(mkl/gnu LIBS)]
         [saved_libs="$LIBS"]
	 [LIBS="$LIBS $GNU_MKL_FLAGS $FCLIBS"]
	 [
            AC_LINK_IFELSE(
               [AC_LANG_PROGRAM(  
[
void dgesdd_(const char *jobz, const int *m, const int *n,double *a, const int *lda, double *s,double *u, const int *ldu,double *vt, const int *ldvt, double *work, const int *lwork, int *iwork, int *info);
],
[
  double * p = 0;
  double work = 0.;
  int lwork = -1;
  int iwork = 0;
  int info = 0;
  int M,N;
  dgesdd_("A",&M,&N,p,&M,p,p,&M,p,&N,&work,&lwork,&iwork,&info);
] 
                               )],
               [LAPACK_LIBS="$GNU_MKL_FLAGS"] 
               [HAVE_LAPACK=yes]
               [AC_SUBST([AM_CPPFLAGS],["$AM_CPPFLAGS -DMKL"])]
	       [AC_MSG_RESULT([yes])],
               [HAVE_LAPACK=no]
               [AC_MSG_RESULT([no])]
            )
         ]
         [LIBS="$saved_libs"]
	)

   AS_IF([test "x$HAVE_LAPACK" = "xno"],
         [AC_MSG_CHECKING(openblas LIBS)]
         [saved_libs="$LIBS"]
         [LIBS="$LIBS -lopenblas $FCLIBS"]
         [
            AC_LINK_IFELSE(
               [AC_LANG_PROGRAM(  
[
void dgesdd_(const char *jobz, const int *m, const int *n,double *a, const int *lda, double *s,double *u, const int *ldu,double *vt, const int *ldvt, double *work, const int *lwork, int *iwork, int *info);
],
[
  double * p = 0;
  double work = 0.;
  int lwork = -1;
  int iwork = 0;
  int info = 0;
  int M,N;
  dgesdd_("A",&M,&N,p,&M,p,p,&M,p,&N,&work,&lwork,&iwork,&info);
] 
                               )],
               [LAPACK_LIBS="-lopenblas"] 
               [HAVE_LAPACK=yes]
               [AC_MSG_RESULT([yes])],
               [HAVE_LAPACK=no]
               [AC_MSG_RESULT([no])]
            )
         ]
         [LIBS="$saved_libs"]
        )



   AS_IF([test "x$HAVE_LAPACK" = "xno"],
         [AC_MSG_CHECKING(-llapack -lblas LIBS)]
         [saved_libs="$LIBS"]
	 [LIBS="$LIBS -llapack -lblas $FCLIBS"]
	 [
            AC_LINK_IFELSE(
               [AC_LANG_PROGRAM(  
[
void dgesdd_(const char *jobz, const int *m, const int *n,double *a, const int *lda, double *s,double *u, const int *ldu,double *vt, const int *ldvt, double *work, const int *lwork, int *iwork, int *info);
],
[
  double * p = 0;
  double work = 0.;
  int lwork = -1;
  int iwork = 0;
  int info = 0;
  int M,N;
  dgesdd_("A",&M,&N,p,&M,p,p,&M,p,&N,&work,&lwork,&iwork,&info);
] 
                               )],
               [LAPACK_LIBS="-llapack -lblas"] 
               [HAVE_LAPACK=yes]
	       [AC_MSG_RESULT([yes])],
               [HAVE_LAPACK=no]
               [AC_MSG_RESULT([no])]
            )
         ]
	)

   AC_SUBST(LAPACK_LIBS,["$LAPACK_LIBS"])

   if test "x$HAVE_LAPACK" != "xyes"; then
      AC_MSG_ERROR([

The lapack/blas librares are required, but could not be found.

Locate the liblapack.a and libblas.a files on your operating system and rerun configure with 
   LDFLAGS="-L/path/to/lib"
As an automated example, try: 
   LDFLAGS="-L\$(dirname \$(locate liblapack.a | head -n 1))"
If you cannot find liblapack.a on your system, then you need to install it.
On fedora: 
   sudo yum install lapack-devel blas-devel
On Ubuntu: 
   sudo apt-get install liblapack-dev libblas-dev
Alternatively, you can install Intel's MKL libraries
   http://software.intel.com/en-us/non-commercial-software-development
Some supercomputers make it available by loading modules, e.g.,
   module load intel/mkl
or some other similar name. You may be able run 
   module avail
to list the available modules.
If you want to use the MKL libraries, then it's probably best to
include the paths to their libraries in your LD_LIBRARY_PATH.
To do this, add something like (your installation path may vary)
   source /opt/intel/mkl/bin/mklvars.sh intel64
to your ~/.bashrc or ~/.profile and then
   source ~/.bashrc
If you know the location of your MKL libraries, but are unable
to include that path to your LD_LIBRARY_PATH (for whatever reason),
then set
   export MKLHOME=/path/to/mkl/lib
and re-run configure.

This configure script will only attempt to link to the mkl libraries
using the gcc bindings, e.g.,

Serial:
     -m64 -Wl,--start-group  -lmkl_gf_lp64 -lmkl_sequential -lmkl_core -Wl,--end-group -lpthread -lm -lm -ldl $FC_RUNTIME_LIB

OpenMP:
    -m64 -Wl,--start-group -lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -Wl,--end-group -liomp5 -lpthread -lm -lm -ldl $FC_RUNTIME_LIB

If you are linking with an Intel compiler (ifort, icc, icpc), then you'll want to link with the native Intel bindings

Serial:
    -m64 -Wl,--start-group -lmkl_intel_lp64 -lmkl_sequential -lmkl_core -Wl,--end-group -lpthread -lm -lm -lsvml

OpenMP:
    -m64 -Wl,--start-group -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core -Wl,--end-group -liomp5 -lpthread -lm -lm -lsvml

which you can set using the enviromental variables LAPACK_LIBS and LAPACK_OPENMP_LIBS

      ])
   fi

   AC_LANG_POP([C])

])
