#ifndef _l1_hpp_
#define _l1_hpp_


///////////////////////////////////////////////////////////////////////
// level 1
///////////////////////////////////////////////////////////////////////

inline double lalg::v::dot( lalg::cv const x ) const
{
  assert( nfast == x.nfast );
  int const inc = 1;
  return FORTRAN_NAME(ddot)(&nfast,data,&inc,x.data,&inc);
}

inline double lalg::v::nrm2() const
{
  //int const inc = 1;
  //return FORTRAN_NAME(dnrm2)(&nfast,data,&inc);
  double d = 0.;
  for ( int i=0; i<nfast; ++i)
    d += data[i]*data[i];
  return d;
}

inline int lalg::v::iabsmax() const
{
  //int const inc = 1;
  //return FORTRAN_NAME(idamax)(&nfast,data,&inc)-1;
  int imax=0;
  double mx = 0.;
  for ( int i=0; i<nfast; ++i )
    {
      double t = std::abs(data[i]);
      if ( t > mx )
	{
	  mx = t;
	  imax = i;
	};
    };
  return imax;
}

inline lalg::v & lalg::v::axpy( double const alpha, lalg::cv const x )
{
  assert( nfast == x.nfast );
  for ( int i=0; i<nfast; ++i )
    data[i] += alpha * x.data[i];
  // int const inc = 1;
  // FORTRAN_NAME(daxpy)(&nfast,&alpha,x.data,&inc,data,&inc);
  return *this;
}

// inline lalg::v & lalg::v::axpby( double const alpha, lalg::v const x, double const beta )
// {
//   //int const N = nfast;
//   for ( int i=0; i<N; ++i )
//     data[i] = alpha * x.data[i] + beta * d.data[i];
//   // assert( nfast == x.nfast );
//   // int const inc=1;
//   // FORTRAN_NAME(dscal)(&nfast,&beta,data,&inc);
//   // FORTRAN_NAME(daxpy)(&nfast,&alpha,x.data,&inc,data,&inc);
//   return *this;
// }
inline lalg::v & lalg::v::axpy( double const alpha, lalg::cv const x, lalg::cv const y )
{
  //int const N = nfast;
  for ( int i=0; i<nfast; ++i )
    data[i] = alpha * x.data[i] + y.data[i];
  // assert( nfast == x.nfast );
  // int const inc=1;
  // FORTRAN_NAME(dscal)(&nfast,&beta,data,&inc);
  // FORTRAN_NAME(daxpy)(&nfast,&alpha,x.data,&inc,data,&inc);
  return *this;
}


#endif

