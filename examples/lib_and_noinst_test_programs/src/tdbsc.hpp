//
// Copyright 2013 Timothy John Giese
//
#ifndef _tdbsc_hpp_
#define _tdbsc_hpp_


/**
 * \file tdbsc.hpp
 *
 * \brief two-dimensional b-spline correction
 *
 * \author Timothy J. Giese
 *
 * \version 0.1
 *
 * \date 2013/01/01
 * 
 */


extern "C"
{

  /** \brief Read the data array size within the 2d b-spline parameter file
    @param[in] fname = filename
    @return size of array to be allocated
   */
  int tdbsc_readdatasize_
  ( char const * fname );

  /** \brief Read a 2d b-spline parameter file
      @param[in] fname = filename
      @param[out] order = b-spline order
      @param[out] dimsize_2 = the number of grid pts in each direction
      @param[out] minmax_2x2 = the min,max values defining the length of the grid.  They are stored in the order (minx,maxx,miny,maxy).
      @param[out] periodicity_2 = flag indicating whether the dimension is periodic
      @param[out] data = the parameters at each grid point.  Use tdbsc_readdatasize_ to determine the size of this array
  */
  void tdbsc_readdata_
  ( char const * fname,
    int * order, 
    int * dimsize_2,
    double * minmax_2x2,
    bool * periodicity_2,
    double * data );


  /** \brief Evaluate a 2d b-spline 
      @param[in] q = an array of length 2 holding the coordinates
      @param[in] dvaluedq = an array of length 2 holding the derivative of the interpolated value with respect to q
      @param[in] order = b-spline order
      @param[in] dimsize_2 = the number of grid pts in each direction
      @param[in] minmax_2x2 = the min,max values defining the length of the grid.  They are stored in the order (minx,maxx,miny,maxy).
      @param[in] periodicity_2 = flag indicating whether the dimension is periodic
      @param[in] data = the parameters at each grid point.  Use tdbsc_readdatasize_ to determine the size of this array
      @return the interpolated value
  */
  double tdbsc_cptvalue_
  ( double const * q,
    double * dvaluedq,
    int const * order, 
    int const * dimsize_2, 
    double const * minmax_2x2,
    bool const * periodicity_2,
    double const * data );

  /** \brief Evaluate a b-spline pucker correction 
      @param[in] x3n = an array of length 3N holding the atom coordinates.  No unit conversions are performed.
      @param[in,out] g3n = an array of length 3N holding atom gradients (not forces).  The pucker correction gradients are ADDED to these values.
      @param[in] a1 = zero-based index of atom 1 in torsion a
      @param[in] a2 = zero-based index of atom 2 in torsion a
      @param[in] a3 = zero-based index of atom 3 in torsion a
      @param[in] a4 = zero-based index of atom 4 in torsion a
      @param[in] b1 = zero-based index of atom 1 in torsion b
      @param[in] b2 = zero-based index of atom 2 in torsion b
      @param[in] b3 = zero-based index of atom 3 in torsion b
      @param[in] b4 = zero-based index of atom 4 in torsion b
      @param[in] order = b-spline order
      @param[in] dimsize_2 = the number of grid pts in each direction
      @param[in] minmax_2x2 = the min,max values defining the length of the grid.  They are stored in the order (minx,maxx,miny,maxy).
      @param[in] periodicity_2 = flag indicating whether the dimension is periodic
      @param[in] data = the parameters at each grid point.  Use tdbsc_readdatasize_ to determine the size of this array
      @return the interpolated value
  */
  double tdbsc_pucker_
  ( double const * x3n,
    double * g3n,
    int const * a1, int const * a2, int const * a3, int const * a4,
    int const * b1, int const * b2, int const * b3, int const * b4,
    int const * order, 
    int const * dimsize_2, 
    double const * minmax_2x2,
    bool const * periodicity_2,
    double const * data );

}

#endif
