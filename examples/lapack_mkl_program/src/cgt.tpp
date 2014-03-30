inline lalg::cgt::cgt( int const m, int const n, double const * d ) 
  : nfast(m),nslow(n),data(d){}

inline lalg::cgt::cgt( int const m, int const n, std::vector<double> const & d ) 
  : nfast(m),nslow(n),data(d.data()) { assert(static_cast<std::size_t>(m*n) == d.size()); }
    
inline lalg::cgt::cgt( lalg::gt const & a )
  : nfast(a.nfast),nslow(a.nslow),data(a.data){}

inline double const * lalg::cgt::begin() const { return data; }
inline double const * lalg::cgt::end() const { return data+nfast*nslow; }

