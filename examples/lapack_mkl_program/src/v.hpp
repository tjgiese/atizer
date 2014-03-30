#ifndef _lalg_v_hpp_
#define _lalg_v_hpp_

#include <vector>

namespace lalg
{
  class sy;
  class ge;
  class gt;
  class gd;
}

namespace lalg
{

  class v
  {
  public:
    
    v( int const n, double * d );
    v( std::vector<double> & a );
    
    double * begin();
    double * end();
    double const * begin() const;
    double const * end() const;

    v & operator+= ( lalg::v const a );
    v & operator-= ( lalg::v const a );
    v & operator*= ( lalg::v const a );
    v & operator= ( lalg::v const a );
    v & operator+= ( lalg::cv const a );
    v & operator-= ( lalg::cv const a );
    v & operator*= ( lalg::cv const a );
    v & operator= ( lalg::cv const a );

    v & operator+= ( double const a );
    v & operator-= ( double const a );
    v & operator*= ( double const a );
    v & operator= ( double const a );
    
    double dot( lalg::cv const x ) const;
    
    double nrm2() const;
    
    int iabsmax() const;
    
    lalg::v & axpy( double const alpha, lalg::cv const x );
    lalg::v & axpy( double const alpha, lalg::cv const x, lalg::cv const y );

    //lalg::v & axpby( double const alpha, lalg::v const x, double const beta );

    //////////////////////////////////////////////////////////////////////////
    // overload these for custom matrix-like object
    template <class MAT>
    lalg::v & dot( double const alpha, MAT & A, lalg::cv const x, double const beta );

    template <class MAT>
    lalg::v & dot( MAT & A, lalg::cv const x );
    //////////////////////////////////////////////////////////////////////////


    lalg::v & dot( double const alpha, lalg::ge const A, lalg::cv const x, double const beta );
    lalg::v & dot( double const alpha, lalg::gt const A, lalg::cv const x, double const beta );
    lalg::v & dot( double const alpha, lalg::sy const A, lalg::cv const x, double const beta );

    lalg::v & dot( lalg::ge const A, lalg::cv const x );
    lalg::v & dot( lalg::gt const A, lalg::cv const x );
    lalg::v & dot( lalg::sy const A, lalg::cv const x );
    

    // static int query_solve( int const N );
    // lalg::v & solve( lalg::sy const & A, lalg::v const & b, int const nscr, double * scr );
    // lalg::v & solve( lalg::sy const & A, lalg::v const & b );


    //
    // solves A.x = b
    // min { xt.b - 0.5 xt.A.x }
    //
    static int query_solve( int const N );
    lalg::v & solve( lalg::sy const & A, lalg::v const & b, int const nscr, double * scr  );
    lalg::v & solve( lalg::sy const & A, lalg::v const & b );

    //
    // solves A.x = b ; st dt.x = N
    // min { xt.b - 0.5 xt.A.x + mu ( xt.d - N ) }
    //
    lalg::v & constrained_solve( lalg::sy const & A, lalg::v const & b, lalg::v const & d, double const N );


    /*
    //lalg::v & apply_orthogonal_constraints( lalg::ge & D, lalg::v & v );
    //
    // On input, the vector does not necessarily satisfy
    // the constraints
    // At.x = constraint_values
    // On output, it does.
    // x += constraint_projector_of_A . ( constraint_values - At.x )
    // where constraint_projector_of_A is
    // ( constraint_projector_of_A = A ).constraint_projector()
    //
    int query_enforce_constraints( int const nconstraints );
    v & enforce_constraints( lalg::ge & A, lalg::ge const & constraint_projector_of_A, lalg::v const & constraint_values, int const nscr, double * scr );
    v & enforce_constraints( lalg::ge & A, lalg::ge const & constraint_projector_of_A, lalg::v const & constraint_values );
    v & enforce_constraints( lalg::ge & A, lalg::v const & constraint_values );
    */


    int nfast;
    double * data;
  };


}


#endif
