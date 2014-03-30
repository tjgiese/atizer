!
! Copyright 2013 Timothy John Giese
!
MODULE puckermod

  USE, INTRINSIC :: ISO_C_BINDING
  IMPLICIT NONE

  PUBLIC

  TYPE dihed_pair
     INTEGER(C_INT) :: idx(8)
  END TYPE dihed_pair

  TYPE pucker
     TYPE(dihed_pair),POINTER :: torsions(:) => NULL()
     INTEGER(C_INT) :: order
     INTEGER(C_INT) :: dimsize(2)
     REAL(C_DOUBLE) :: minmax(4)
     LOGICAL(C_BOOL) :: periodic(2)
     REAL(C_DOUBLE),POINTER :: data(:) => NULL()
  END TYPE pucker


  INTERFACE
     INTEGER(C_INT) FUNCTION tdbsc_readdatasize(fname) &
          & BIND(C,NAME="tdbsc_readdatasize_")
       USE, INTRINSIC :: ISO_C_BINDING
       CHARACTER(KIND=C_CHAR,LEN=1),INTENT(IN) :: fname
     END FUNCTION tdbsc_readdatasize
  END INTERFACE
  
  INTERFACE
     SUBROUTINE tdbsc_readdata(fname, &
          & order,dimsize,minmax,periodic,data) &
          & BIND(C,NAME="tdbsc_readdata_")
       USE, INTRINSIC :: ISO_C_BINDING
       CHARACTER(KIND=C_CHAR,LEN=1),INTENT(IN) :: fname
       INTEGER(C_INT),INTENT(OUT) :: order
       INTEGER(C_INT),INTENT(OUT) :: dimsize
       REAL(C_DOUBLE),INTENT(OUT) :: minmax
       LOGICAL(C_BOOL),INTENT(OUT) :: periodic
       REAL(C_DOUBLE),INTENT(OUT) :: data
     END SUBROUTINE tdbsc_readdata
  END INTERFACE

  INTERFACE
     REAL(C_DOUBLE) FUNCTION tdbsc_pucker(c,g,&
          & a1,a2,a3,a4,b1,b2,b3,b4, &
          & order,dimsize,minmax,periodic,data) &
          & BIND(C,NAME="tdbsc_pucker_")
       USE, INTRINSIC :: ISO_C_BINDING
       REAL(C_DOUBLE),INTENT(IN) :: c
       REAL(C_DOUBLE),INTENT(INOUT) :: g
       INTEGER(C_INT),INTENT(IN) :: a1,a2,a3,a4
       INTEGER(C_INT),INTENT(IN) :: b1,b2,b3,b4
       INTEGER(C_INT),INTENT(IN) :: order
       INTEGER(C_INT),INTENT(IN) :: dimsize
       REAL(C_DOUBLE),INTENT(IN) :: minmax
       LOGICAL(C_BOOL),INTENT(IN) :: periodic
       REAL(C_DOUBLE),INTENT(IN) :: data
     END FUNCTION tdbsc_pucker
  END INTERFACE


CONTAINS

  FUNCTION new_pucker( filename ) RESULT( p )
    IMPLICIT NONE

    CHARACTER(LEN=*),INTENT(IN) :: filename
    TYPE(pucker) :: p
    INTEGER(C_INT) :: n
    
    n = tdbsc_readdatasize( TRIM(ADJUSTL(filename))//CHAR(0) )
    ALLOCATE( p%data(n) )
    p%data = 0.d0
    CALL tdbsc_readdata( TRIM(ADJUSTL(filename))//CHAR(0), &
         & p%order, p%dimsize(1), p%minmax(1), p%periodic(1), p%data(1) )

  END FUNCTION new_pucker


  FUNCTION pucker_eval( p, nat, crd, grd ) RESULT(E)
    IMPLICIT NONE

    TYPE(pucker),INTENT(IN) :: p
    INTEGER(C_INT),INTENT(IN) :: nat
    REAL(C_DOUBLE),INTENT(IN) :: crd(3*nat)
    REAL(C_DOUBLE),INTENT(INOUT) :: grd(3*nat)
    REAL(C_DOUBLE) :: E
    INTEGER :: i

    E = 0.d0
    IF ( ASSOCIATED( p%torsions ) ) THEN
       DO i=1,SIZE(p%torsions)
          E = E + tdbsc_pucker( crd(1), grd(1), &
               & p%torsions(i)%idx(1), p%torsions(i)%idx(2), &
               & p%torsions(i)%idx(3), p%torsions(i)%idx(4), &
               & p%torsions(i)%idx(5), p%torsions(i)%idx(6), &
               & p%torsions(i)%idx(7), p%torsions(i)%idx(8), &
               & p%order, p%dimsize(1), p%minmax(1), p%periodic(1), p%data(1) )
       END DO
    END IF

  END FUNCTION pucker_eval


  SUBROUTINE pucker_push_back(p,a1,a2,a3,a4,b1,b2,b3,b4)
    IMPLICIT NONE

    TYPE(pucker),INTENT(INOUT) :: p
    INTEGER(C_INT),INTENT(IN) :: a1,a2,a3,a4,b1,b2,b3,b4

    TYPE(dihed_pair),ALLOCATABLE :: t(:)
    INTEGER :: n

    IF ( ASSOCIATED( p%torsions ) ) THEN
       n = SIZE(p%torsions)
       ALLOCATE( t(n+1) )
       t(1:n) = p%torsions(1:n)
       t(n+1)%idx = (/a1,a2,a3,a4,b1,b2,b3,b4/)
       DEALLOCATE( p%torsions )
       ALLOCATE( p%torsions(n+1) )
       p%torsions = t
    ELSE
       ALLOCATE( p%torsions(1) )
       p%torsions(1)%idx = (/a1,a2,a3,a4,b1,b2,b3,b4/)
    END IF

  END SUBROUTINE pucker_push_back

  
  SUBROUTINE delete_pucker( p )
    IMPLICIT NONE
    TYPE(pucker),INTENT(INOUT) :: p

    IF ( ASSOCIATED( p%torsions ) ) DEALLOCATE( p%torsions )
    IF ( ASSOCIATED( p%data ) ) DEALLOCATE( p%data )

  END SUBROUTINE delete_pucker


END MODULE puckermod ! end
