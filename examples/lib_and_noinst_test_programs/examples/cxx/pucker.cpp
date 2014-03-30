//
// Copyright 2013 Timothy John Giese
//
#include "pucker.hpp"

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
