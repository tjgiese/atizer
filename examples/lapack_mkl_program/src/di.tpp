#ifndef _lalg_di_tpp_
#define _lalg_di_tpp_

#include <cmath>

inline lalg::di::di( int const nfast, int const nslow, double * d )
  : nfast(nfast),nslow(nslow),nmin(std::min(nfast,nslow)),data(d)
{ }

inline lalg::di::di( int const nf, int const ns, std::vector<double> & d )
  : nfast(nf),nslow(ns),nmin(std::min(nf,ns)),data(d.data())
{ 
  assert( d.size() >= (std::size_t)(nmin) ); 
}


inline double * lalg::di::begin()
{
  return data;
}

inline double * lalg::di::end()
{
  return data+nmin;
}


inline lalg::di lalg::di::t()
{
  return lalg::di(nslow,nfast,data);
}

inline lalg::di lalg::di::t() const
{
  return lalg::di(nslow,nfast,data);
}


inline void lalg::di::operator+= ( lalg::di const a )
{
  assert( nfast == a.nfast );
  assert( nslow == a.nslow );
  for ( int i=0; i<nmin; ++i )
    data[i] += a.data[i];
}


inline void lalg::di::operator+= ( double const a )
{
  for ( int i=0; i<nmin; ++i )
    data[i] += a;
}


inline void lalg::di::operator-= ( lalg::di const a )
{
  assert( nfast == a.nfast );
  assert( nslow == a.nslow );
  for ( int i=0; i<nmin; ++i )
    data[i] -= a.data[i];
}

inline void lalg::di::operator-= ( double const a )
{
  for ( int i=0; i<nmin; ++i )
    data[i] -= a;
}


inline void lalg::di::operator*= ( double const a )
{
  for ( int i=0; i<nmin; ++i )
    data[i] *= a;
}


inline void lalg::di::operator= ( lalg::di const a )
{
  assert( nfast == a.nfast );
  assert( nslow == a.nslow );
  for ( int i=0; i<nmin; ++i )
    data[i] = a.data[i];
}


inline void lalg::di::operator= ( double const a )
{
  for ( int i=0; i<nmin; ++i )
    data[i] = a;
}


inline lalg::di & lalg::di::inverse( double const tol )
{
  int const nlow = std::min(4,nmin);
  for ( int i=0; i<nlow; ++i )
    {
      if ( std::abs(data[i]) > tol )
	{ data[i] = 1./data[i]; }
      else
	{ data[i] = 0.; };
    };
  for ( int i=nlow; i<nmin; ++i )
    data[i] = 1./data[i];
  std::swap(nfast,nslow);
  return *this;
}




#endif
