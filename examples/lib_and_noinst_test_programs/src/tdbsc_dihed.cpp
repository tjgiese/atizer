//
// Copyright 2013 Timothy John Giese
//
#include "tdbsc_dihed.hpp"
#include <cmath>

double const PI = 3.141592653589793238462643383279502884197;

template <class DblIn,class DblOut>
void CrossProduct
( DblIn const * a, 
  DblIn const * b,
  DblOut * axb )
{
  // http://en.wikipedia.org/wiki/Cross_product#Coordinate_notation
  axb[0] = a[1]*b[2] - a[2]*b[1];
  axb[1] = b[0]*a[2] - a[0]*b[2];
  axb[2] = a[0]*b[1] - a[1]*b[0];
}

template <class DblIn,class DblOut>
void AccumulateCrossProduct
( DblIn const * a, 
  DblIn const * b,
  DblOut * axb )
{
  // http://en.wikipedia.org/wiki/Cross_product#Coordinate_notation
  axb[0] += a[1]*b[2] - a[2]*b[1];
  axb[1] += b[0]*a[2] - a[0]*b[2];
  axb[2] += a[0]*b[1] - a[1]*b[0];
}


template <class DblIn,class DblOut>
void OrthogonalVector
( DblIn const * a, 
  DblIn const * b, 
  DblIn const * c, 
  DblOut * n )
{
  // http://en.wikipedia.org/wiki/Dihedral_angle#Methods_of_computation
  DblIn ba[] = { b[0]-a[0],b[1]-a[1],b[2]-a[2] };
  DblIn ca[] = { c[0]-a[0],c[1]-a[1],c[2]-a[2] };
  CrossProduct(ba,ca,n);
}


double dihedral_angle
( double const * Ra, double const * Rb, 
  double const * Rc, double const * Rd, 
  bool & linear )
{
  double d = 0.;

  long double const Rba[]={Rb[0]-Ra[0],Rb[1]-Ra[1],Rb[2]-Ra[2]};
  long double const Rcb[]={Rc[0]-Rb[0],Rc[1]-Rb[1],Rc[2]-Rb[2]};
  long double const Rdc[]={Rd[0]-Rc[0],Rd[1]-Rc[1],Rd[2]-Rc[2]};

  long double A[3],B[3];
  CrossProduct(Rba,Rcb,A);
  CrossProduct(Rcb,Rdc,B);
  long double const n2A = A[0]*A[0]+A[1]*A[1]+A[2]*A[2];
  long double const n2B = B[0]*B[0]+B[1]*B[1]+B[2]*B[2];
  long double const den = std::sqrt(n2A*n2B);

  // std::cout << "den = " 
  // 	    << std::scientific << std::setw(12) << std::setprecision(3) 
  // 	    << den << "\n";
  linear = true;
  if ( den > 1.e-30 ) 
    {
      linear = false;
      // std::cout << "acos( " 
      // 		<< std::scientific << std::setw(12) << std::setprecision(3) 
      // 		<< -(A[0]*B[0] + A[1]*B[1] + A[2]*B[2])/den
      // 		<< "\n";
      long double x = -(A[0]*B[0] + A[1]*B[1] + A[2]*B[2])/den;
      if ( x < -1. ) 
	{
	  d = PI;
	}
      else if ( x > 1. )
	{
	  d = 0.;
	}
      else
	{
	  d = std::acos( x );
	};

      long double BxA[3];
      CrossProduct(B,A,BxA);

      long double BondProj = Rcb[0]*BxA[0] + Rcb[1]*BxA[1] + Rcb[2]*BxA[2];
      if ( BondProj > 0.0 ) d = -d;
      d = PI - d;
    }

  return d;
}


double dihedral_angle
( double const * Ra, double const * Rb, 
  double const * Rc, double const * Rd, 
  bool & linear, 
  double * ddda, double * dddb, 
  double * dddc, double * dddd )
{
  double d = 0.;

  long double const Rba[]={Rb[0]-Ra[0],Rb[1]-Ra[1],Rb[2]-Ra[2]};
  long double const Rcb[]={Rc[0]-Rb[0],Rc[1]-Rb[1],Rc[2]-Rb[2]};
  long double const Rdc[]={Rd[0]-Rc[0],Rd[1]-Rc[1],Rd[2]-Rc[2]};
  long double const Rca[]={Rc[0]-Ra[0],Rc[1]-Ra[1],Rc[2]-Ra[2]};
  long double const Rdb[]={Rd[0]-Rb[0],Rd[1]-Rb[1],Rd[2]-Rb[2]};

  long double A[3],B[3];
  CrossProduct(Rba,Rcb,A);
  CrossProduct(Rcb,Rdc,B);
  long double const n2A = A[0]*A[0]+A[1]*A[1]+A[2]*A[2];
  long double const n2B = B[0]*B[0]+B[1]*B[1]+B[2]*B[2];
  long double const den = std::sqrt(n2A*n2B);
  linear = true;
  if ( den > 1.e-30 ) 
    {
      linear = false;
      long double x = -(A[0]*B[0] + A[1]*B[1] + A[2]*B[2])/den;
      if ( x <= -1. ) 
	{
	  d = PI;
	}
      else if ( x >= 1. )
	{
	  d = 0.;
	}
      else
	{
	  d = std::acos( x );
	};


      //d = std::acos( -(A[0]*B[0] + A[1]*B[1] + A[2]*B[2])/den );

      long double BxA[3];
      CrossProduct(B,A,BxA);

      long double BondProj = Rcb[0]*BxA[0] + Rcb[1]*BxA[1] + Rcb[2]*BxA[2];
      if ( BondProj > 0.0 ) d = -d;
      d = PI - d;

      long double const ncb = std::sqrt(Rcb[0]*Rcb[0]+Rcb[1]*Rcb[1]+Rcb[2]*Rcb[2]);

      long double const sclA = 1. / ( n2A*ncb );
      A[0] *= sclA;
      A[1] *= sclA;
      A[2] *= sclA;
      long double AxRcb[3];
      CrossProduct(A,Rcb,AxRcb);

      long double const sclB = 1. / ( n2B*ncb );
      B[0] *= sclB;
      B[1] *= sclB;
      B[2] *= sclB;

      // std::cout << std::scientific << std::setw(12) << std::setprecision(3) 
      // 		<< sclA << " " 
      // 		<< std::scientific << std::setw(12) << std::setprecision(3)
      // 		<< sclB << "\n";

      long double RcbxB[3];
      CrossProduct(Rcb,B,RcbxB);

      CrossProduct(AxRcb,Rcb,ddda);
      CrossProduct(Rca,AxRcb,dddb);
      AccumulateCrossProduct(RcbxB,Rdc,dddb);
      CrossProduct(AxRcb,Rba,dddc);
      AccumulateCrossProduct(Rdb,RcbxB,dddc);
      CrossProduct(RcbxB,Rcb,dddd);
    }

  return d;
}
