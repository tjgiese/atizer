#ifndef _lalg_sy_tpp_
#define _lalg_sy_tpp_

inline lalg::sy::sy( int const n, double * d )
  : nfast(n), nslow(n), data(d)
{}

inline lalg::sy::sy( int const n, std::vector<double> & d )
  : nfast(n), nslow(n), data(d.data())
{
  assert( (std::size_t)(n*n) == d.size() );
}


inline lalg::ge lalg::sy::ge()
{
  return lalg::ge(nfast,nslow,data);
}

inline lalg::ge lalg::sy::ge() const
{
  return lalg::ge(nfast,nslow,data);
}

inline double * lalg::sy::begin() 
{ 
  return data + nfast; 
}

inline double * lalg::sy::end() 
{ 
  return data + nfast*nslow; 
}


inline void lalg::sy::operator+= ( lalg::sy const a )
{
  assert( nfast == a.nfast );
  assert( nslow == a.nslow );
  int const N = nfast*nslow;
  for ( int i=0; i<N; ++i )
    data[i] += a.data[i];
}


inline void lalg::sy::operator+= ( double const a )
{
  int const N = nfast*nslow;
  for ( int i=0; i<N; ++i )
    data[i] += a;
}


inline void lalg::sy::operator-= ( lalg::sy const a )
{
  assert( nfast == a.nfast );
  assert( nslow == a.nslow );
  int const N = nfast*nslow;
  for ( int i=0; i<N; ++i )
    data[i] -= a.data[i];
}


inline void lalg::sy::operator-= ( double const a )
{
  int const N = nfast*nslow;
  for ( int i=0; i<N; ++i )
    data[i] -= a;
}


inline void lalg::sy::operator*= ( double const a )
{
  int const N = nfast*nslow;
  for ( int i=0; i<N; ++i )
    data[i] *= a;
}


inline lalg::sy & lalg::sy::operator= ( lalg::sy const a )
{
  assert( nfast == a.nfast );
  assert( nslow == a.nslow );
  int const N = nfast*nslow;
  for ( int i=0; i<N; ++i )
    data[i] = a.data[i];
  return *this;
}


inline lalg::sy & lalg::sy::operator= ( double const a )
{
  int const N = nfast*nslow;
  for ( int i=0; i<N; ++i )
    data[i] = a;
  return *this;
}




inline std::ostream & operator<< ( std::ostream & cout, lalg::sy const a )
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


#endif
