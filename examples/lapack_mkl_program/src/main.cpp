#include "lalg.hpp"

#ifdef _OPENMP
#include <omp.h>
#else
#include <sys/time.h>
#endif

class timer
{
    
public:
    
  timer() : niter(1) {}
  timer( unsigned int nit ) : niter(nit) {}

  /** \brief Start timer */
  inline void start() 
  {
#ifdef _OPENMP
    mStartTime = omp_get_wtime();
#else
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &mStartTime); 
#endif
  }
  /** \brief Stop timer */
  inline void stop() 
  { 
#ifdef _OPENMP
    mStopTime = omp_get_wtime();
#else
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &mStopTime);
#endif 
  }
  /** \brief Return time in seconds (double); assumes start and stop have been used */
  inline double value() const 
  { 
#ifdef _OPENMP
    return (mStopTime-mStartTime)/niter;
#else
    return TimeInSec( DeltaTime() )/niter; 
#endif
  };
  

private:
  unsigned int niter;
#ifdef _OPENMP
  double mStartTime,mStopTime;
#else
  timespec mStartTime;
  timespec mStopTime;
  /** \private */
  timespec DeltaTime() const;
  /** \private */
  inline double TimeInSec( timespec const t ) const { return static_cast<double>(t.tv_sec) + static_cast<double>(t.tv_nsec) * 1.e-9; }
#endif
};
  

#ifndef _OPENMP
inline timespec timer::DeltaTime() const
{
  timespec temp;
  if ( (mStopTime.tv_nsec - mStartTime.tv_nsec) < 0 )
    {
      temp.tv_sec = mStopTime.tv_sec-mStartTime.tv_sec-1;
      temp.tv_nsec = 1000000000+mStopTime.tv_nsec-mStartTime.tv_nsec;
    } 
  else 
    {
      temp.tv_sec = mStopTime.tv_sec-mStartTime.tv_sec;
      temp.tv_nsec = mStopTime.tv_nsec-mStartTime.tv_nsec;
    };
  return temp;
}
#endif




inline std::ostream & operator<< ( std::ostream & cout, timer const & t )
{
  return cout << std::setw(9) << std::setprecision(4) << std::fixed << t.value();
}




double const TOL = 1.e-13;

double fRand(double fMin, double fMax)
{
  double f = (double)rand() / RAND_MAX;
  return fMin + f * (fMax - fMin);
}

double fRand()
{
  return fRand(-1.,1.);
}

class check
{
public:
  check( std::vector<double> const & a, std::vector<double> const & b )
    : a(a),b(b) {};
  check( int const n, double const * pa, double const * pb )
    : a(pa,pa+n),b(pb,pb+n) {};
  std::vector<double> a,b;
};

std::ostream & operator<<( std::ostream & cout, check c )
{
  bool err = false;
  int m = c.a.size();
  if ( c.a.size() != c.b.size() ) err = true;
  for ( int i=0; i<m; ++i )
    if ( std::abs( c.a[i]-c.b[i] ) > TOL )
      err = true;
  if ( err )
    {
      cout << " FAIL\n";
    }
  else
    {
      cout << " pass\n";
    };
  return cout;
}



std::vector<double> rvec(int n);
std::vector<double> rvec(int n,int m);

void time_eigen( int m );
void time_solve( int m );

int main()
{
  srand(0);

  // time_eigen(25);
  // time_eigen(50);
  // time_eigen(75);
   time_eigen(100);
  // time_eigen(150);
   time_eigen(200);
  // time_eigen(300);
  // time_eigen(400);
  // time_eigen(450);
   time_eigen(500);
  // time_eigen(600);
  // time_eigen(700);

   time_solve(100);
   time_solve(200);
   time_solve(500);
  // time_solve(700);

  return 0;
}


std::vector<double> rvec(int n)
{
  std::vector<double> a(n);
  for ( int i=0; i<n; ++i )
    a[i] = fRand();
  return a;
}

std::vector<double> rvec(int m, int n)
{
  std::vector<double> a( rvec(m*n) );
  if ( m == n )
    {
      for ( int i=0; i<n; ++i )
	{
	  for ( int j=0; j<i; ++j )
	    {
	      a[j+i*n] *= 1. / std::abs(i-j);
	      a[i+j*n] = a[j+i*n];
	    };
	  a[i+i*n] += 5.;
	};
    };
  return a;
}






void time_eigen( int n )
{
  std::stringstream sheader;
  sheader << "time_eigen(" << n << ") ";
  std::string header( sheader.str() );

  std::vector<double> a1( rvec(n,n) ),b1(n),c1(n*n);
  lalg::ge c(n,n,c1);
  lalg::sy a(n,a1);
  lalg::di b(n,n,b1);

  int NITER = 100;
  if ( n > 350 ) NITER = 50;
  if ( n > 550 ) NITER = 25;

  timer t1(NITER),t2(NITER),t3(NITER),t4(NITER);
  t1.start();
  for ( int i=0; i<NITER; ++i ) a.dsyev( b, c );
  t1.stop();

  t2.start();
  for ( int i=0; i<NITER; ++i ) a.dsyevd( b, c );
  t2.stop();

  t3.start();
  for ( int i=0; i<NITER; ++i ) a.dsyevr( b, c );
  t3.stop();

  t4.start();
  for ( int i=0; i<NITER; ++i ) a.eigen( b, c );
  t4.stop();

  std::cout << std::setw(5) << n << t1 << t2 << t3 << t4 << "\n";

}




void time_solve( int n )
{
  std::stringstream sheader;
  sheader << "time_solve(" << n << ") ";
  std::string header( sheader.str() );

  std::vector<double> a1( rvec(n,n) ),b1( rvec(n) ),c1(n);
  lalg::sy a(n,a1);
  lalg::v  b(b1);
  lalg::v  c(c1);

  int NITER=100;
  timer t1(NITER);

  t1.start();
  for ( int i=0; i<NITER; ++i ) c.solve( a, b );
  t1.stop();

  std::cout << header << "solve   : " << t1 << "\n";

}

