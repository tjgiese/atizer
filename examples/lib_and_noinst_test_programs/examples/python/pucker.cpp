//
// Copyright 2013 Timothy John Giese
//
#include "pucker.hpp"
#include "exceptions.hpp"
#include <sstream>
#include <fstream>

pucker::pucker( char const * fname )
{
  int ndata = tdbsc_readdatasize_(fname);
  data.resize(ndata);
  tdbsc_readdata_(fname,&order,
		  dimsize.data(),minmax.data(),
		  periodic.data(),data.data());
}


double pucker::eval( double const * x, double * g )
{
  double E = 0.;
  int const n = torsion.size();
  for ( int i=0; i<n; ++i )
    E += tdbsc_pucker_
      ( x,g,
	&torsion[i][0].a, &torsion[i][0].b, 
	&torsion[i][0].c, &torsion[i][0].d,
	&torsion[i][1].a, &torsion[i][1].b, 
	&torsion[i][1].c, &torsion[i][1].d,
	&order, 
	dimsize.data(), minmax.data(), 
	periodic.data(), data.data() );
  return E;
}


void pucker::push_back( dihed a, dihed b )
{
  std::tr1::array<dihed,2> ab = {{ a,b }};
  torsion.push_back(ab);
}






template <class T>
void v_to_list( std::vector<T> const & x , boost::python::list & l )
{
  int n = x.size();
  int nl = boost::python::len(l);
  for ( int i=nl; i>n; --i ) l.pop();
  nl = boost::python::len(l);
  for ( int i=nl; i<n; ++i ) l.append(T());
  nl = boost::python::len(l);
  for ( int i=0; i<n; ++i )
    l[i] = x[i];
}
    
    
template <class T>
void list_to_v( boost::python::list const & l, std::vector<T> & x )
{
  std::size_t const n = boost::python::len(l);
  x.resize( n );
  for ( std::size_t i=0; i<n; ++i )
    x[i] = boost::python::extract<T>(l[i]);
}






pucker::pucker( boost::python::str pfname )
{
  std::string sname = boost::python::extract< std::string >( pfname );
  char const * fname = sname.c_str();

  { // check if file is ok ////////////////
    std::ifstream fh;
    fh.open( fname );
    if ( ! fh.good() )
      raise_exception(std::string("Could not open ") + sname);
  } ///////////////////////////////////////

  int ndata = tdbsc_readdatasize_(fname);
  data.resize(ndata);
  tdbsc_readdata_(fname,&order,
		  dimsize.data(),minmax.data(),
		  periodic.data(),data.data());
}


double pucker::eval
( boost::python::list const & crd, boost::python::list & grd )
{
  std::vector<double> c,g;
  list_to_v( crd, c );
  list_to_v( grd, g );
  if ( c.size() != g.size() )
    {
      std::stringstream msg;
      msg << "Error detected in "
	  << "pucker::eval( list const & crd, list & grd ) : "
	  << "crd size " << c.size() 
	  << " != grd size " << g.size() << std::endl;
      raise_exception( msg.str() );
    };
  if ( c.size() % 3 != 0 )
    {
      std::stringstream msg;
      msg << "Error detected in "
	  << "pucker::eval( list const & crd, list & grd ) : "
	  << "crd size " << c.size() 
	  << " is not a multiple of 3" << std::endl;
      raise_exception( msg.str() );
    };
  double E = eval(c.data(),g.data());
  v_to_list(g,grd);
  return E;
}


void pucker::push_back
( int const a1, int const b1, 
  int const c1, int const d1, 
  int const a2, int const b2,
  int const c2, int const d2 )
{
  push_back( dihed(a1,b1,c1,d1), dihed(a2,b2,c2,d2) );
}

