#ifndef _lalg_di_hpp_
#define _lalg_di_hpp_

namespace lalg
{
  class di
  {
  public:

    di( int const nfast, int const nslow, double * data );
    di( int const nfast, int const nslow, std::vector<double> & data );

    double * begin();
    double * end();
    di t();
    di t() const;

    void operator+= ( lalg::di const a );
    void operator-= ( lalg::di const a );
    void operator= ( lalg::di const a );

    void operator+= ( double const a );
    void operator-= ( double const a );
    void operator*= ( double const a );
    void operator= ( double const a );

    di & inverse( double const tol );

    int nfast,nslow,nmin;
    double * data;
  };
}

#endif
