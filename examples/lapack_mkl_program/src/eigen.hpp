#ifndef _lalg_eigen_hpp_
#define _lalg_eigen_hpp_

inline int lalg::sy::query_dsyev( int const N )
{
  double p = 0.;
  int info = 0;
  int lwork=-1;
  double work = 0.;
  FORTRAN_NAME(dsyev)("V","U", &N, &p,
		      &N, &p,
		      &work, &lwork, &info );
  assert( info == 0 );
  return (int)work;
}

inline int lalg::sy::query_dsyevd( int const N )
{
  int info = 0;
  int lwork=-1;
  double work = 0.;
  int liwork=-1;
  int iwork = 0;
  double p = 0.;
  FORTRAN_NAME(dsyevd)("V","U",
		       &N,&p,
		       &N,&p,
		       &work, &lwork,
		       &iwork, &liwork,
		       &info );
  assert( info == 0 );
  return work;
  //liwork = (int)iwork;
  // liwork = 5 * ( 3 + 5*N )
}

inline int lalg::sy::iquery_dsyevd( int const N )
{
  int info = 0;
  int lwork=-1;
  double work = 0.;
  int liwork=-1;
  int iwork = 0;
  double p = 0.;
  FORTRAN_NAME(dsyevd)("V","U",
		       &N,&p,
		       &N,&p,
		       &work, &lwork,
		       &iwork, &liwork,
		       &info );
  assert( info == 0 );
  return iwork;
}



inline int lalg::sy::query_dsyevr( int const N )
{
  int info  =  0, ISUPPZ = 0, IL = 1, IU = N, M = N;
  double work = 0., p = 0., VL = 0., VU = 0.;
  int lwork = -1, liwork=-1, iwork = 0;
  double ABSTOL = FORTRAN_NAME(dlamch)("Safe minimum");
 
  FORTRAN_NAME(dsyevr)("V","A","U",
		       &N,&p,&N,
		       &VL,&VU,
		       &IL,&IU,
		       &ABSTOL,
		       &M,&p,&p,&N,
		       &ISUPPZ,
		       &work,&lwork,
		       &iwork,&liwork,
		       &info );
  assert( info == 0 );
  return ((int)work) + N*N;
}


inline int lalg::sy::iquery_dsyevr( int const N )
{
  int info  =  0, ISUPPZ = 0, IL = 1, IU = N, M = N;
  double work = 0., p = 0., VL = 0., VU = 0.;
  int lwork = -1, liwork=-1, iwork = 0;
  double ABSTOL = 0.;

  FORTRAN_NAME(dsyevr)("V","A","U",
		       &N,&p,&N,
		       &VL,&VU,
		       &IL,&IU,
		       &ABSTOL,
		       &M,&p,&p,&N,
		       &ISUPPZ,
		       &work,&lwork,
		       &iwork,&liwork,
		       &info );
  assert( info == 0 );
  return iwork+2*N; 
}



inline void lalg::sy::dsyev( lalg::di & E, lalg::ge & U, int const nscr, double * scr ) const
{
  for ( int i=0; i<nfast*nfast; ++i )
    U.data[i] = data[i];
  int info = 0;
  FORTRAN_NAME(dsyev)("V","U", &nfast, U.data,
		      &nfast, E.data,
		      scr, &nscr, &info );
  assert( info == 0 );
}



inline void lalg::sy::dsyevd( lalg::di & E, lalg::ge & U, int const nscr, double * scr ) const
{
  for ( int i=0; i<nfast*nfast; ++i )
    U.data[i] = data[i];
  int info = 0;
  int liwork= lalg::sy::iquery_dsyevd(nfast);
  std::vector<int> iwork(liwork);
  FORTRAN_NAME(dsyevd)("V","U",
		       &nfast,U.data,
		       &nfast,E.data,
		       scr, &nscr,
		       iwork.data(), &liwork,
		       &info );
  assert( info == 0 );
}


inline void lalg::sy::dsyevr( lalg::di & E, lalg::ge & U, int const nscr, double * scr ) const
{
  int const N2 = nfast*nfast;
  double * T = scr;
  int const lwork = nscr-N2;
  double * work = scr + N2;
  for ( int i=0; i<N2; ++i )
    T[i] = data[i];

  int info,M;
  int const liwork = lalg::sy::iquery_dsyevr(nfast);
  std::vector<int> isuppz(liwork);
  int * iwork = isuppz.data() + 2*nfast;
  const double VL = 0., VU = 0.;
  const int IL = 1, IU = nfast;
  const double ABSTOL = FORTRAN_NAME(dlamch)("Safe minimum");
  
  FORTRAN_NAME(dsyevr)("V","A","U",
		       &nfast,T,&nfast,
		       &VL,&VU,
		       &IL,&IU,
		       &ABSTOL,
		       &M,E.data,U.data,&nfast,
		       isuppz.data(),
		       work,&lwork,
		       iwork,&liwork,
		       &info );
  assert( info == 0 );
}



inline void lalg::sy::dsyev( lalg::di & E, lalg::ge & U) const
{
  std::vector<double> scr( lalg::sy::query_dsyev(nfast) );
  dsyev(E,U,scr.size(),scr.data());
}

inline void lalg::sy::dsyevd( lalg::di & E, lalg::ge & U ) const
{
  std::vector<double> scr( lalg::sy::query_dsyevd(nfast) );
  dsyevd(E,U,scr.size(),scr.data());
}

inline void lalg::sy::dsyevr( lalg::di & E, lalg::ge & U ) const
{
  std::vector<double> scr( lalg::sy::query_dsyevr(nfast) );
  dsyevr(E,U,scr.size(),scr.data());
}


#define EVMAX 70
#define EVRMAX 440

inline int lalg::sy::query_eigen( int const N )
{
  int n;
  if ( N < EVMAX )
    {
      n = lalg::sy::query_dsyev(N);
    }
  else if ( N < EVRMAX )
    {
      n = lalg::sy::query_dsyevr(N);
    }
  else
    {
      n = lalg::sy::query_dsyevd(N);
    };
  return n;
}

inline void lalg::sy::eigen( lalg::di & E, lalg::ge & U, int const nscr, double * scr ) const
{
  if ( nfast < EVMAX )
    {
      dsyev(E,U,nscr,scr);
    }
  else if ( nfast < EVRMAX )
    {
      dsyevr(E,U,nscr,scr);
    }
  else
    {
      dsyevd(E,U,nscr,scr);
    };
}

inline void lalg::sy::eigen( lalg::di & E, lalg::ge & U ) const
{
  if ( nfast < EVMAX )
    {
      dsyev(E,U);
    }
  else if ( nfast < EVRMAX )
    {
      dsyevr(E,U);
    }
  else
    {
      dsyevd(E,U);
    };
}

#endif

