#ifndef _lalg_csy_hpp_
#define _lalg_csy_hpp_

namespace lalg
{
  class sy;
  class csy
  {
  public:

    csy( int const n, double const * d ); 
    csy( int const n, std::vector<double> const & d ); 
    csy( lalg::sy const & a );
    double const * begin() const;
    double const * end() const;
    lalg::cge ge() const;

    int nfast,nslow;
    double const * data;
  };
}

#endif
