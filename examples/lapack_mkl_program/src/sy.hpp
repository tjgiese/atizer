#ifndef _lalg_sy_hpp_
#define _lalg_sy_hpp_

namespace lalg
{
  class ge;
  class di;
}

namespace lalg
{
  class sy
  {
  public:
    sy( int const n, double * d );
    sy( int const n, std::vector<double> & d );

    double * begin();
    double * end();
    lalg::ge ge() const;
    lalg::ge ge();

    void operator+= ( lalg::sy const a );
    void operator-= ( lalg::sy const a );
    lalg::sy & operator= ( lalg::sy const a );

    void operator+= ( double const a );
    void operator-= ( double const a );
    void operator*= ( double const a );
    lalg::sy & operator= ( double const a );

    lalg::sy & dot( double const alpha, lalg::ge const A, lalg::ge const B, double const beta );
    lalg::sy & dot( double const alpha, lalg::gt const A, lalg::ge const B, double const beta );
    lalg::sy & dot( lalg::ge const A, lalg::ge const B );
    lalg::sy & dot( lalg::gt const A, lalg::ge const B );

    lalg::sy & inverse();

    static int query_svd_inverse( int const N );
    lalg::sy & svd_inverse( double const tol, int const nscr, double * scr );
    lalg::sy & svd_inverse( double const tol );

    // static int query_safe_inverse( int const N );
    // lalg::sy & safe_inverse( double const tol, int const nscr, double * scr );
    // lalg::sy & safe_inverse( double const tol );

    static int query_svd( int const N );
    void svd( lalg::ge & U, lalg::di & w, lalg::ge & VT, int const nscr, double * scr ) const;
    void svd( lalg::ge & U, lalg::di & w, lalg::ge & VT ) const;


    static int query_dsyev( int const N );
    static int query_dsyevd( int const N );
    static int query_dsyevr( int const N );
    static int iquery_dsyevd( int const N );
    static int iquery_dsyevr( int const N );

    void dsyev( lalg::di & E, lalg::ge & U, int const nscr, double * scr ) const;
    void dsyevd( lalg::di & E, lalg::ge & U, int const nscr, double * scr ) const;
    void dsyevr( lalg::di & E, lalg::ge & U, int const nscr, double * scr ) const;
    void dsyev( lalg::di & E, lalg::ge & U ) const;
    void dsyevd( lalg::di & E, lalg::ge & U ) const;
    void dsyevr( lalg::di & E, lalg::ge & U ) const;



    static int query_eigen( int const N );
    void eigen( lalg::di & E, lalg::ge & U, int const nscr, double * scr ) const;
    void eigen( lalg::di & E, lalg::ge & U ) const;


    


    int nfast,nslow;
    double * data;
  };
}

#endif
