#ifndef _lalg_l3_hpp_
#define _lalg_l3_hpp_


inline lalg::ge & lalg::ge::dot( double const alpha, lalg::ge const A, lalg::ge const B, double const beta )
{
  assert( nfast == A.nfast );
  assert( nslow == B.nslow );
  assert( A.nslow == B.nfast );
  FORTRAN_NAME(dgemm)("N","N",&nfast,&nslow,&(A.nslow),
		      &alpha,
		      A.data,&(A.nfast),
		      B.data,&(B.nfast),
		      &beta,
		      data,&nfast);
  return *this;
}
inline lalg::ge & lalg::ge::dot( lalg::ge const A, lalg::ge const B )
{ return dot(1.,A,B,0.); }



inline lalg::ge & lalg::ge::dot( double const alpha, lalg::gt const A, lalg::ge const B, double const beta )
{
  assert( nfast == A.nslow );
  assert( nslow == B.nslow );
  assert( A.nfast == B.nfast );
  FORTRAN_NAME(dgemm)("T","N",&nfast,&nslow,&(A.nfast),
		      &alpha,
		      A.data,&(A.nfast),
		      B.data,&(B.nfast),
		      &beta,
		      data,&nfast);
  return *this;
}
inline lalg::ge & lalg::ge::dot( lalg::gt const A, lalg::ge const B )
{ return dot(1.,A,B,0.); }



inline lalg::ge & lalg::ge::dot( double const alpha, lalg::ge const A, lalg::gt const B, double const beta )
{
  assert( nfast == A.nfast );
  assert( nslow == B.nfast );
  assert( A.nslow == B.nslow );
  FORTRAN_NAME(dgemm)("N","T",&nfast,&nslow,&(A.nslow),
		      &alpha,
		      A.data,&(A.nfast),
		      B.data,&(B.nfast),
		      &beta,
		      data,&nfast);
  return *this;
}
inline lalg::ge & lalg::ge::dot( lalg::ge const A, lalg::gt const B )
{ return dot(1.,A,B,0.); }



inline lalg::ge & lalg::ge::dot( double const alpha, lalg::gt const A, lalg::gt const B, double const beta )
{
  assert( nfast == A.nslow );
  assert( nslow == B.nfast );
  assert( A.nfast == B.nslow );
  FORTRAN_NAME(dgemm)("T","T",&nfast,&nslow,&(A.nfast),
		      &alpha,
		      A.data,&(A.nfast),
		      B.data,&(B.nfast),
		      &beta,
		      data,&nfast);
  return *this;
}
inline lalg::ge & lalg::ge::dot( lalg::gt const A, lalg::gt const B )
{ return dot(1.,A,B,0.); }



inline lalg::ge & lalg::ge::dot( double const alpha, lalg::sy const A, lalg::ge const B, double const beta )
{
  assert( nfast == A.nfast );
  assert( nslow == B.nslow );
  assert( A.nslow == B.nfast );
  FORTRAN_NAME(dsymm)("L","U",&nfast,&nslow,
		      &alpha,
		      A.data,&(A.nfast),
		      B.data,&(B.nfast),
		      &beta,
		      data,&nfast);
  return *this;
}
inline lalg::ge & lalg::ge::dot( lalg::sy const A, lalg::ge const B )
{ return dot(1.,A,B,0.); }



inline lalg::ge & lalg::ge::dot( double const alpha, lalg::ge const A, lalg::sy const B, double const beta )
{
  assert( nfast == A.nfast );
  assert( nslow == B.nslow );
  assert( A.nslow == B.nfast );
  FORTRAN_NAME(dsymm)("R","U",&nfast,&nslow,
		      &alpha,
		      B.data,&(B.nfast),
		      A.data,&(A.nfast),
		      &beta,
		      data,&nfast);
  return *this;
}
inline lalg::ge & lalg::ge::dot( lalg::ge const A, lalg::sy const B )
{ return dot(1.,A,B,0.); }



inline lalg::ge & lalg::ge::dot( lalg::di const A, lalg::ge const B )
{
  assert( nfast == A.nfast );
  assert( nslow == A.nslow );
  assert( nslow == B.nslow );
  assert( A.nslow == B.nfast );
  for ( int j=0; j<nslow; ++j )
    for ( int i=0; i<nfast; ++i )
      data[i+j*nfast] = A.data[i] * B.data[i+j*B.nfast];
  return *this;
}


inline lalg::ge & lalg::ge::dot( lalg::gt const A, lalg::di const B )
{
  assert( nfast == A.nslow );
  assert( nslow == B.nslow );
  assert( A.nfast == B.nfast );
  if ( nslow < 1000 )
    {
      for ( int j=0; j<nslow; ++j )
	for ( int i=0; i<nfast; ++i )
	  data[i+j*nfast] = A.data[j+i*A.nslow] * B.data[j];
    }
  else
    {
      int const BLK = 8;
      for ( int jb=0; jb<nslow; jb+=BLK )
	{
	  int const ju = std::min(nslow,jb+BLK);
	  for ( int ib=0; ib<nfast; ib+=BLK )
	    {
	      int const iu = std::min(nfast,ib+BLK);
	      for ( int j=jb; j<ju; ++j )
		for ( int i=ib; i<iu; ++i )
		  data[i+j*nfast] = A.data[j+i*A.nslow] * B.data[j];
	    };
	};
    };
  return *this;
}




inline lalg::sy & lalg::sy::dot( double const alpha, lalg::ge const A, lalg::ge const B, double const beta )
{
  ge().dot(alpha,A,B,beta);
  return *this;
}


inline lalg::sy & lalg::sy::dot( lalg::ge const A, lalg::ge const B )
{
  ge().dot(1.,A,B,0.);
  return *this;
}

inline lalg::sy & lalg::sy::dot( double const alpha, lalg::gt const A, lalg::ge const B, double const beta )
{
  ge().dot(alpha,A,B,beta);
  return *this;
}

inline lalg::sy & lalg::sy::dot( lalg::gt const A, lalg::ge const B )
{
  ge().dot(1.,A,B,0.);
  return *this;
}



#endif

