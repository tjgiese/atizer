#ifndef _lalg_ge_tpp_
#define _lalg_ge_tpp_

#include <cassert>
#include <ostream>

inline lalg::ge::ge( int m, int n, double * d ) 
  : nfast(m),nslow(n),data(d) 
{}

    
inline lalg::ge::ge( int m, int n, std::vector<double> & a ) 
  : nfast(m),nslow(n),data(a.data()) 
{ 
  assert( a.size() >= (std::size_t)(m*n) ); 
}


inline double * lalg::ge::begin() { return data; }
inline double * lalg::ge::end() { return data + nfast*nslow; }

inline double const * lalg::ge::begin() const { return data; }
inline double const * lalg::ge::end() const { return data + nfast*nslow; }


inline lalg::v lalg::ge::col( int const i )
{
  return lalg::v(nfast,data+i*nfast);
}


inline void lalg::ge::operator+= ( lalg::ge const a )
{
  assert( nfast == a.nfast );
  assert( nslow == a.nslow );
  int const N = nfast*nslow;
  for ( int i=0; i<N; ++i )
    data[i] += a.data[i];
}


inline void lalg::ge::operator+= ( double const a )
{
  int const N = nfast*nslow;
  for ( int i=0; i<N; ++i )
    data[i] += a;
}


inline void lalg::ge::operator-= ( lalg::ge const a )
{
  assert( nfast == a.nfast );
  assert( nslow == a.nslow );
  int const N = nfast*nslow;
  for ( int i=0; i<N; ++i )
    data[i] -= a.data[i];
}


inline void lalg::ge::operator-= ( double const a )
{
  int const N = nfast*nslow;
  for ( int i=0; i<N; ++i )
    data[i] -= a;
}


inline void lalg::ge::operator*= ( double const a )
{
  int const N = nfast*nslow;
  for ( int i=0; i<N; ++i )
    data[i] *= a;
}


inline lalg::ge & lalg::ge::operator= ( lalg::ge const a )
{
  assert( nfast == a.nfast );
  assert( nslow == a.nslow );
  int const N = nfast*nslow;
  for ( int i=0; i<N; ++i )
    data[i] = a.data[i];
  return *this;
}


inline lalg::ge & lalg::ge::operator= ( double const a )
{
  int const N = nfast*nslow;
  for ( int i=0; i<N; ++i )
    data[i] = a;
  return *this;
}


inline lalg::gt lalg::ge::t()
{
  return lalg::gt(nfast,nslow,data);
}


inline std::ostream & operator<< ( std::ostream & cout, lalg::ge const a )
{
  for ( int i=0; i<a.nfast; ++i )
    {
      for ( int j=0; j<a.nslow; ++j )
	cout << std::setw(11) << std::setprecision(3) << std::scientific 
	     << a.data[i+j*a.nfast];
      if ( i+1 != a.nfast )
	cout << "\n";
    };
  return cout;
}


inline lalg::ge & lalg::ge::graham_schmidt()
{
  double const TOL = 1./1.e-10;
  for ( int i=0; i<nslow; ++i )
    {
      lalg::v vi( col(i) );
      double inorm = 1./std::sqrt( vi.nrm2() );
      vi *= inorm;

      if ( inorm > TOL )
	{
	  vi = 0.;
	  continue;
	};
      
      for ( int j=0; j<i; ++j )
	{
	  lalg::v vj( col(j) );
	  double f = vi.dot(vj);
	  vi.axpy( -f, vj );
	};
     
      double onorm = 1./std::sqrt( vi.nrm2() );
      vi *= onorm;

      if ( onorm > TOL )
	vi = 0.;
    };
  return *this;
}



// inline lalg::ge & lalg::ge::orthogonalize_constraints( lalg::v & cvalues )
// {
//   assert( cvalues.nfast == nslow );
//   double const TOL = 1./1.e-10;
//   for ( int i=0; i<nslow; ++i )
//     {
//       lalg::v vi( col(i) );
//       double inorm = 1./std::sqrt( vi.nrm2() );
//       vi *= inorm;
//       cvalues.data[i] *= inorm;

//       if ( inorm > TOL )
// 	{
// 	  vi = 0.;
// 	  cvalues.data[i] = 0.;
// 	  continue;
// 	};
      
//       for ( int j=0; j<i; ++j )
// 	{
// 	  lalg::v vj( col(j) );
// 	  double f = vi.dot(vj);
// 	  vi.axpy( -f, vj );
// 	  cvalues.data[i] -= f * cvalues.data[j];
// 	};
     
//       double onorm = 1./std::sqrt( vi.nrm2() );
//       vi *= onorm;
//       cvalues.data[i] *= onorm;

//       if ( onorm > TOL )
// 	{
// 	  vi = 0.;
// 	  cvalues.data[i] = 0.;
// 	};      
//     };
//   return *this;
// }



#endif
