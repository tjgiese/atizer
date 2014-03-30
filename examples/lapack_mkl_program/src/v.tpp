#ifndef _lalg_v_tpp_
#define _lalg_v_tpp_


inline lalg::v::v( int const n, double * d ) : nfast(n),data(d) {}


inline lalg::v::v( std::vector<double> & a ) : nfast(a.size()),data(a.data()) {}

    
inline double * lalg::v::begin() { return data; }
inline double * lalg::v::end() { return data + nfast; }
inline double const * lalg::v::begin() const { return data; }
inline double const * lalg::v::end() const { return data + nfast; }


template <class MAT>
lalg::v & lalg::v::dot( MAT & A, lalg::cv const x ) 
{ 
  return dot(1.,A,x,0.); 
}


inline lalg::v & lalg::v::operator+= ( lalg::v const a )
{
  assert( nfast == a.nfast );
  for ( int i=0; i<nfast; ++i ) data[i] += a.data[i];
  return *this;
}

inline lalg::v & lalg::v::operator-= ( lalg::v const a )
{
  assert( nfast == a.nfast );
  for ( int i=0; i<nfast; ++i ) data[i] -= a.data[i];
  return *this;
}

inline lalg::v & lalg::v::operator*= ( lalg::v const a )
{
  assert( nfast == a.nfast );
  for ( int i=0; i<nfast; ++i ) data[i] *= a.data[i];
  return *this;
}


inline lalg::v & lalg::v::operator= ( lalg::v const a )
{ 
  for ( int i=0; i<nfast; ++i ) data[i] = a.data[i]; 
  return *this; 
}



inline lalg::v & lalg::v::operator+= ( lalg::cv const a )
{
  assert( nfast == a.nfast );
  for ( int i=0; i<nfast; ++i ) data[i] += a.data[i];
  return *this;
}

inline lalg::v & lalg::v::operator-= ( lalg::cv const a )
{
  assert( nfast == a.nfast );
  for ( int i=0; i<nfast; ++i ) data[i] -= a.data[i];
  return *this;
}

inline lalg::v & lalg::v::operator*= ( lalg::cv const a )
{
  assert( nfast == a.nfast );
  for ( int i=0; i<nfast; ++i ) data[i] *= a.data[i];
  return *this;
}

inline lalg::v & lalg::v::operator= ( lalg::cv const a )
{
  assert( nfast == a.nfast );
  for ( int i=0; i<nfast; ++i ) data[i] = a.data[i];
  return *this;
}




inline lalg::v & lalg::v::operator+= ( double const a )
{
  for ( int i=0; i<nfast; ++i )
    data[i] += a;
  return *this;
}




inline lalg::v & lalg::v::operator-= ( double const a )
{
  for ( int i=0; i<nfast; ++i )
    data[i] -= a;
  return *this;
}


inline lalg::v & lalg::v::operator*= ( double const a )
{
  for ( int i=0; i<nfast; ++i )
    data[i] *= a;
  return *this;
}



inline lalg::v & lalg::v::operator= ( double const a )
{
  for ( int i=0; i<nfast; ++i )
    data[i] = a;
  return *this;
}


inline std::ostream & operator<< ( std::ostream & cout, lalg::cv const a )
{
  for ( int i=0; i<a.nfast; ++i )
    cout << std::setw(11) << std::setprecision(3) << std::scientific
	 << a.data[i];
  return cout;
}

// inline lalg::v & lalg::v::apply_orthogonal_constraints( lalg::ge & D, lalg::v & v )
// {
//   assert( D.nslow == v.nfast );
//   assert( D.nfast == nfast );
//   std::vector<double> scr(D.nslow);
//   lalg::v t(scr);
//   t.dot( D.t(), *this );
//   for ( int i=0; i<D.nslow; ++i )
//     axpy( v.data[i]-t.data[i], D.col(i) );
//   return *this;
// }


#endif
