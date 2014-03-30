#ifndef _lalg_cv_hpp_
#define _lalg_cv_hpp_

namespace lalg
{
  class v;
  class cv
  {
  public:

    cv( int const n, double const * d );
    cv( std::vector<double> const & d ); 
    cv( lalg::v const & a ); 
    double const * begin() const;
    double const * end() const;

    int nfast;
    double const * data;
  };
}

#endif
