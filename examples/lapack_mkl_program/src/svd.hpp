#ifndef _lalg_svd_hpp_
#define _lalg_svd_hpp_


// queries

inline int lalg::ge::query_svd( int const M, int const N )
{
  double * p = NULL;
  double work = 0.;
  int lwork = -1;
  int iwork = 0;
  int info = 0;
  FORTRAN_NAME(dgesdd)("A",&M,&N,p,&M,p,p,&M,p,&N,&work,&lwork,&iwork,&info);
  if ( info < 0 )
    {
      throw lalg::illegal_argument("query_svd_inverse; dgesdd",-info);
    }
  else if ( info > 0 )
    {
      throw lalg::exception("query_svd_inverse; dgesdd; DBDSDC did not converge, updating process failed.");
    };
  return ((int)work) + M*N;
}


inline int lalg::ge::query_svd_inverse( int const M, int const N )
{
  return M*M + std::min(M,N) + N*N + lalg::ge::query_svd(M,N);
}


inline int lalg::sy::query_svd( int const N )
{
  return lalg::ge::query_svd(N,N);
}

inline int lalg::sy::query_svd_inverse( int const N )
{
  return lalg::ge::query_svd_inverse(N,N);
}







// driver


namespace lalg
{

  template <class M>
  inline void svd_driver( M const & ain, lalg::ge & U, lalg::di & w, lalg::ge & VT, int const nscr, double * scr )
  {
    assert( U.nfast == ain.nfast );
    assert( U.nslow == ain.nfast );
    assert( w.nfast == ain.nfast );
    assert( w.nslow == ain.nslow );
    assert( VT.nfast == ain.nslow );
    assert( VT.nslow == ain.nslow );
    
    std::vector<int> iwork( 8*std::min(ain.nfast,ain.nslow) );
    int info = 0;

    lalg::ge A(ain.nfast,ain.nslow,scr);
    int const N = ain.nfast*ain.nslow;
    for ( int i=0; i<N; ++i )
      A.data[i] = ain.data[i];
    int const lwork = nscr - N;

    FORTRAN_NAME(dgesdd)("A",&(ain.nfast),&(ain.nslow),A.data,
			 &(ain.nfast),w.data,U.data,
			 &(ain.nfast),VT.data,
			 &(ain.nslow),A.end(),
			 &lwork,iwork.data(),&info);
  if ( info < 0 )
    {
      throw lalg::illegal_argument("svd; dgesdd",-info);
    }
  else if ( info > 0 )
    {
      throw lalg::exception("svd; dgesdd; DBDSDC did not converge, updating process failed.");
    };
  }

}












// interfaces


inline void lalg::ge::svd( lalg::ge & U, lalg::di & w, lalg::ge & VT, int const nscr, double * scr ) const
{
  lalg::svd_driver(*this,U,w,VT,nscr,scr);
}

inline void lalg::ge::svd( lalg::ge & U, lalg::di & w, lalg::ge & VT ) const
{
  std::vector<double> scr(lalg::ge::query_svd(nfast,nslow));
  lalg::svd_driver(*this,U,w,VT,scr.size(),scr.data());
}



inline void lalg::sy::svd( lalg::ge & U, lalg::di & w, lalg::ge & VT, int const nscr, double * scr ) const
{
  lalg::svd_driver(*this,U,w,VT,nscr,scr);
}

inline void lalg::sy::svd( lalg::ge & U, lalg::di & w, lalg::ge & VT ) const
{
  std::vector<double> scr(lalg::sy::query_svd(nfast));
  lalg::svd_driver(*this,U,w,VT,scr.size(),scr.data());
}




inline lalg::ge & lalg::ge::svd_inverse( double const tol, int const nscr, double * scr )
{
  lalg::ge U(nfast,nfast,scr);
  lalg::di w(nfast,nslow,U.end());
  lalg::ge VT(nslow,nslow,w.end());
  //lalg::ge t(nslow,nfast,VT.end());
  lalg::ge t(nfast,nslow,VT.end());
  assert( nscr > std::distance(scr,VT.end()) );
  svd(U,w,VT,nscr-std::distance(scr,VT.end()),VT.end());
  std::swap(nfast,nslow);
  //return dot( t.dot( VT.t(),w.inverse(tol) ), U.t() );
  return dot( t.dot( w.inverse(tol).t(), VT ).t(), U.t() );
}

inline lalg::ge & lalg::ge::svd_inverse( double const tol )
{
  std::vector<double> scr( lalg::ge::query_svd_inverse(nfast,nslow) );
  return svd_inverse(tol,scr.size(),scr.data());
}

inline lalg::sy & lalg::sy::svd_inverse( double const tol, int const nscr, double * scr )
{
  ge().svd_inverse(tol,nscr,scr);
  return *this;
}

inline lalg::sy & lalg::sy::svd_inverse( double const tol )
{
  std::vector<double> scr( lalg::sy::query_svd_inverse(nfast) );
  return svd_inverse(tol,scr.size(),scr.data());
}


inline lalg::sy & lalg::sy::inverse()
{
  int info;

  FORTRAN_NAME(dpotrf)( "U", &nfast, data, &nfast, &info );

  if ( info != 0 )
    {
      if ( info < 0 )
	throw lalg::illegal_argument("lalg::sy::inverse dpotrf",-info);
      if ( info > 0 )
	throw lalg::exception("lalg::sy::inverse dpotrf says matrix is not positive definite");
    };

  FORTRAN_NAME(dpotri)( "U", &nfast, data, &nfast, &info );

  if ( info != 0 )
    {
      if ( info < 0 )
	throw lalg::illegal_argument("lalg::sy::inverse dpotri",-info);
      if ( info > 0 )
	throw lalg::exception("lalg::sy::inverse dpotri says the inverse could not be computed");
    };

  for ( int j=1; j < nfast; ++j )
    for ( int i=0; i < j; ++i )
      data[j+i*nfast] = data[i+j*nfast];

  return *this;
}


#endif

