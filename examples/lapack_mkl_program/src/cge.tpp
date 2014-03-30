inline lalg::cge::cge( int const m, int const n, double const * d ) 
  : nfast(m),nslow(n),data(d){}

inline lalg::cge::cge( int const m, int const n, std::vector<double> const & d ) 
  : nfast(m),nslow(n),data(d.data()) { assert(static_cast<std::size_t>(m*n) == d.size()); }

inline lalg::cge::cge( lalg::ge const & a )
  : nfast(a.nfast),nslow(a.nslow),data(a.data){}

inline double const * lalg::cge::begin() const { return data; }
inline double const * lalg::cge::end() const { return data+nfast*nslow; }
inline lalg::cgt lalg::cge::t() const { return lalg::cgt(nfast,nslow,data); }
inline lalg::cv lalg::cge::col( int const i ) const { return lalg::cv(nfast,data+i*nfast); }

