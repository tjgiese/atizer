#ifndef _lalg_cge_hpp_
#define _lalg_cge_hpp_

namespace lalg
{
  class cgt;
  class ge;
  class cge
  {
  public:

    cge( int const m, int const n, double const * d ); 
    cge( int const m, int const n, std::vector<double> const & d ); 
    cge( lalg::ge const & a );
    double const * begin() const;
    double const * end() const;
    lalg::cgt t() const;
    lalg::cv col( int const i ) const;
    int nfast,nslow;
    double const * data;
  };
}

#endif
