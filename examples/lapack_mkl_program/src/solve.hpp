
// inline int lalg::v::query_solve( int const N )
// {
//   int nrhs=1;
//   int ipiv=1;
//   double p=0.;
//   double work=0.;
//   int lwork=-1;
//   int info=0;
//   FORTRAN_NAME(dsysv)("U",&N,&nrhs,&p,&N,&ipiv,&p,&N,&work,&lwork,&info);
//   return (int)work + N*N;
// }

// inline lalg::v & lalg::v::solve( lalg::sy const & A, lalg::v const & b, int const nscr, double * scr )
// {
//   lalg::sy T(nfast,scr);
//   T = A;
//   int const lwork = nscr-nfast*nfast;
//   *this = b;
//   int info=0;
//   int one=1;
//   std::vector<int> ipiv(nfast);
//   FORTRAN_NAME(dsysv)("U",&nfast,&one,T.data,&nfast,
// 		      ipiv.data(),data,&nfast,T.end(),&lwork,&info);
//   if ( info != 0 )
//     {
//       if ( info < 0 )
// 	throw lalg::illegal_argument("lalg::v::solve dsysv",-info);
//       if ( info > 0 )
// 	throw lalg::exception("lalg::v::solve dsysv says the matrix is singular");
//     };
//   return *this;
// }
// inline lalg::v & lalg::v::solve( lalg::sy const & A, lalg::v const & b )
// {
//   std::vector<double> scr( lalg::v::query_solve(nfast) );
//   return solve(A,b,scr.size(),scr.data());
// }



inline int lalg::v::query_solve( int const N ) { return N*N; }


inline lalg::v & lalg::v::solve( lalg::sy const & A, lalg::v const & b, int const nscr, double * scr )
{
  if ( nscr < nfast*nfast )
    throw lalg::exception("lalg::v::solve scratch space too small");
  return dot( (  lalg::sy(nfast,scr)=A  ).inverse() , b );
}


inline lalg::v & lalg::v::solve( lalg::sy const & A, lalg::v const & b )
{
  std::vector<double> scr(nfast*nfast);  
  return dot( (  lalg::sy(nfast,scr)=A  ).inverse() , b );
}


inline lalg::v & lalg::v::constrained_solve( lalg::sy const & A, lalg::v const & b, lalg::v const & d, double const N )
{
  assert( d.nrm2() > 1.e-10 );
  std::vector<double> scr(nfast*nfast+nfast);
  lalg::sy Ainv(nfast,scr.data());
  lalg::v t(nfast,Ainv.end());
  t.dot( (Ainv=A).inverse() , d );
  double const mu = ( N - t.dot(b) ) / t.dot(d);
  return dot( Ainv, t.axpy(mu,d,b) );
}


