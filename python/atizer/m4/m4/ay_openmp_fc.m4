
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
