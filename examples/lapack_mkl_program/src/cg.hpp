template < class Matrix, class PreconditionerInverse >
bool 
CG( int const N, 
    Matrix & A, 
    lalg::v & x, lalg::v const & b,
    PreconditionerInverse const & Minv, 
    int & max_iter, 
    double & tol )
{
  double resid;
  
  std::vector<double> SCR( 4*N );
  lalg::v p( N, SCR.data() );
  lalg::v z( N, p.end() );
  lalg::v q( N, z.end() );
  lalg::v r( N, q.end() );
  
  /*
  std::vector<double> sp(N),sz(N),sq(N),sr(N);
  lalg::v p( sp );
  lalg::v z( sz );
  lalg::v q( sq );
  lalg::v r( sr );
  */

  double alpha, beta, rho, rho_1 = 1.;

  double normb = b.nrm2();
  r.axpy( -1., q.dot(A,x), b );

  if ( normb == 0.0 ) 
    normb = 1.;
  
  if ( (resid = r.nrm2() / normb) <= tol ) 
    {
      tol = resid;
      max_iter = 0;
      return true;
    }

  for ( int i = 1; i <= max_iter; i++ ) 
    {

      z.dot(Minv,r);
      rho = r.dot(z);
      if ( i == 1 )
	{
	  p = z;
	}
      else 
	{
	  beta = rho / rho_1;
	  ( p *= beta ) += z;
	}
      q.dot(A,p);
      alpha = rho / p.dot(q);
      x.axpy( alpha,p);
      r.axpy(-alpha,q);

      std::cout << std::scientific << r.nrm2() / normb << "\n";
      if ( (resid = r.nrm2() / normb ) <= tol) 
	{
	  tol = resid;
	  max_iter = i;
	  return true;     
	}

      rho_1 = rho;
    }
  tol = resid;
  return false;
}


