inline lalg::csy::csy( int const n, double const * d ) 
  : nfast(n),nslow(n),data(d){}

inline lalg::csy::csy( int const n, std::vector<double> const & d ) 
  : nfast(n),nslow(n),data(d.data()) { assert(static_cast<std::size_t>(n*n) == d.size()); }
    
inline lalg::csy::csy( lalg::sy const & a )
  : nfast(a.nfast),nslow(a.nslow),data(a.data){}

inline double const * lalg::csy::begin() const { return data; }
inline double const * lalg::csy::end() const { return data+nfast*nslow; }
inline lalg::cge lalg::csy::ge() const { return lalg::cge(nfast,nslow,data); }

