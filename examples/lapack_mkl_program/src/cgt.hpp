#ifndef _lalg_cgt_hpp_
#define _lalg_cgt_hpp_

namespace lalg
{
  class gt;
  class cgt
  {
  public:

    cgt( int const m, int const n, double const * d ); 
    cgt( int const m, int const n, std::vector<double> const & d );
    cgt( lalg::gt const & a );
    double const * begin() const;
    double const * end() const;
    int nfast,nslow;
    double const * data;
  };
}

#endif
