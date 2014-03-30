#ifndef _lalg_l2_hpp_
#define _lalg_l2_hpp_



///////////////////////////////////////////////////////////////////////
// level 2
///////////////////////////////////////////////////////////////////////

inline lalg::v & lalg::v::dot( double const alpha, lalg::ge const A, lalg::cv const x, double const beta )
{
  assert( nfast == A.nfast );
  assert( A.nslow == x.nfast );
  int const inc = 1;
  FORTRAN_NAME(dgemv)("N",&(A.nfast),&(A.nslow),&alpha,
		      A.data,&(A.nfast),
		      x.data,&inc,&beta,
		      data,&inc);
  return *this;
}

inline lalg::v & lalg::v::dot( double const alpha, lalg::gt const A, lalg::cv const x, double const beta )
{
  assert( nfast == A.nslow );
  assert( A.nfast == x.nfast );
  int const inc = 1;
  FORTRAN_NAME(dgemv)("T",&(A.nfast),&(A.nslow),&alpha,
		      A.data,&(A.nfast),
		      x.data,&inc,&beta,
		      data,&inc);
  return *this;
}


inline lalg::v & lalg::v::dot( double const alpha, lalg::sy const A, lalg::cv const x, double const beta )
{
  assert( nfast == A.nfast );
  assert( A.nslow == x.nfast );
  int const inc = 1;
  FORTRAN_NAME(dsymv)("U",&(A.nfast),&alpha,
		      A.data,&(A.nfast),
		      x.data,&inc,&beta,
		      data,&inc);
  return *this;
}



inline lalg::v & lalg::v::dot( lalg::ge const A, lalg::cv const x )
{
  return dot(1.,A,x,0.);
}


inline lalg::v & lalg::v::dot( lalg::gt const A, lalg::cv const x )
{
  return dot(1.,A,x,0.);
}


inline lalg::v & lalg::v::dot( lalg::sy const A, lalg::cv const x )
{
  return dot(1.,A,x,0.);
}


#endif
