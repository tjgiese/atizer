inline lalg::cv::cv( int const n, double const * d ) 
  : nfast(n), data(d) {}

inline lalg::cv::cv( std::vector<double> const & d ) 
  : nfast(d.size()), data(d.data()) {}

inline lalg::cv::cv( lalg::v const & a ) 
  : nfast(a.nfast), data(a.data) {}

inline double const * lalg::cv::begin() const { return data; }
inline double const * lalg::cv::end() const { return data+nfast; }

