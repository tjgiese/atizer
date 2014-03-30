#ifndef _lalg_ge_hpp_
#define _lalg_ge_hpp_

#include <vector>

namespace lalg
{
  class v;
  class gt;
  class sy;
  class di;
}

namespace lalg
{

  class ge
  {
  public:
    
    ge( int m, int n, double * d );
    ge( int m, int n, std::vector<double> & a );

    double * begin();
    double * end();
    double const * begin() const;
    double const * end() const;
    lalg::gt t();
    lalg::gt t() const;
    lalg::v  col( int const i );

    void operator+= ( lalg::ge const a );
    void operator-= ( lalg::ge const a );
    lalg::ge & operator= ( lalg::ge const a );

    void operator+= ( double const a );
    void operator-= ( double const a );
    void operator*= ( double const a );
    lalg::ge & operator= ( double const a );
    
    //////////////////////////////////////////////////////////////////////////
    // overload these for custom matrix-like object
    template <class MA,class MB>
    lalg::ge & dot( double const alpha, MA & A, MB & B, double const beta );
    
    template <class MA,class MB>
    lalg::ge & dot( MA & A, MB & B );
    //////////////////////////////////////////////////////////////////////////


    lalg::ge & dot( double const alpha, lalg::ge const A, lalg::ge const B, double const beta );
    lalg::ge & dot( double const alpha, lalg::gt const A, lalg::ge const B, double const beta );
    lalg::ge & dot( double const alpha, lalg::ge const A, lalg::gt const B, double const beta );
    lalg::ge & dot( double const alpha, lalg::gt const A, lalg::gt const B, double const beta );
    lalg::ge & dot( double const alpha, lalg::sy const A, lalg::ge const B, double const beta );
    lalg::ge & dot( double const alpha, lalg::ge const A, lalg::sy const B, double const beta );

    lalg::ge & dot( lalg::ge const A, lalg::ge const B );
    lalg::ge & dot( lalg::gt const A, lalg::ge const B );
    lalg::ge & dot( lalg::ge const A, lalg::gt const B );
    lalg::ge & dot( lalg::gt const A, lalg::gt const B );
    lalg::ge & dot( lalg::sy const A, lalg::ge const B );
    lalg::ge & dot( lalg::ge const A, lalg::sy const B );

    lalg::ge & dot( lalg::di const A, lalg::ge const B );
    lalg::ge & dot( lalg::gt const A, lalg::di const B );



    lalg::ge & graham_schmidt();
    //lalg::ge & orthogonalize_constraints( lalg::v & constraint_values );



    static int query_svd_inverse( int const M, int const N );
    lalg::ge & svd_inverse( double const tol, int const nscr, double * scr );
    lalg::ge & svd_inverse( double const tol );



    static int query_svd( int const M, int const N );
    void svd( lalg::ge & U, lalg::di & w, lalg::ge & VT, int const nscr, double * scr ) const;
    void svd( lalg::ge & U, lalg::di & w, lalg::ge & VT ) const;


    /*
    //
    // On entry, the matrix A has dimensions M x Nconstraints
    // On exit, the matrix is
    //  P = A.(At.A)^{-1}
    // which is still M x Nconstraints
    //
    // The resulting matrix projects out constraints via
    // x += P.(c - At.x)
    // where c is the vector of Nconstraint constraint values
    //
    static int query_constraint_projector( int const M, int const Nconstraints );
    lalg::ge & constraint_projector( int const nscr, double * scr );
    lalg::ge & constraint_projector();
    */


    int nfast,nslow;
    double * data;
  };
  
}

#endif
