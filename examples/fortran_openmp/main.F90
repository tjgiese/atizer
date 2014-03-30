!
! Copyright 2013 Timothy John Giese
!
PROGRAM MAIN
#ifdef _OPENMP
  USE omp_lib
#endif
  IMPLICIT NONE

  INTEGER :: i

  i = -1
#ifdef _OPENMP
  i = omp_get_num_threads()
#endif
  WRITE(6,*)i
  CALL foo()

  STOP

END PROGRAM MAIN
