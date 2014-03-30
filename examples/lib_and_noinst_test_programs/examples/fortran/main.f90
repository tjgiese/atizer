!
! Copyright 2013 Timothy John Giese
!
PROGRAM MAIN
  USE puckermod
  IMPLICIT NONE

  INTEGER(C_INT) :: nat
  REAL(C_DOUBLE),POINTER :: crd(:,:) => NULL()
  REAL(C_DOUBLE),POINTER :: grd(:,:) => NULL()
  TYPE(pucker) :: p
  REAL(C_DOUBLE) :: E
  INTEGER :: i

  CALL read_xyz( "ade.xyz", nat, crd )

  ALLOCATE( grd(3,SIZE(crd,2)) )
  grd = 0.d0

  p = new_pucker( "ade.2dbspl" )
  CALL pucker_push_back( p, 0,1,2,3, 2,3,4,5 )

  E = pucker_eval( p, nat, crd, grd )

  WRITE(6,'(A,ES12.4)')"E = ",E
  DO i=1,nat
     WRITE(6,'(3ES12.4)')grd(1:3,i)
  END DO

  CALL delete_pucker( p )
  IF ( ASSOCIATED( crd ) ) DEALLOCATE( crd )
  IF ( ASSOCIATED( grd ) ) DEALLOCATE( grd )

  STOP


CONTAINS

  SUBROUTINE read_xyz( fname, nat, crd )
    IMPLICIT NONE

    CHARACTER(LEN=*),INTENT(IN) :: fname
    INTEGER(C_INT),INTENT(OUT) :: nat
    REAL(C_DOUBLE),POINTER :: crd(:,:)

    CHARACTER(LEN=100) :: title
    INTEGER :: i

    nat = 0
    OPEN(UNIT=20,FILE=fname,STATUS="old")
    READ(20,*)nat
    READ(20,*)title
    ALLOCATE( crd(3,nat) )
    DO i=1,nat
       READ(20,*)title,crd(1:3,i)
    END DO
    CLOSE(UNIT=20)
    crd = crd * 1.88972613373440d0

  END SUBROUTINE read_xyz


END PROGRAM MAIN
