#ifndef _lalg_H_
#define _lalg_H_

#include "LAPACK_FortranInterface.hpp"

#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>

#include "exceptions.hpp"

// class definitions
#include "cv.hpp"
#include "cge.hpp"
#include "cgt.hpp"
#include "csy.hpp"

#include "v.hpp"
#include "gt.hpp"
#include "ge.hpp"
#include "sy.hpp"
#include "di.hpp"

#include "constraint_enforcer.hpp"

// method implementations

#include "cv.tpp"
#include "cge.tpp"
#include "cgt.tpp"
#include "csy.tpp"

#include "v.tpp"
#include "ge.tpp"
#include "gt.tpp"
#include "sy.tpp"
#include "di.tpp"
#include "constraint_enforcer.tpp"


#include "l1.hpp"
#include "l2.hpp"
#include "l3.hpp"
#include "svd.hpp"
#include "eigen.hpp"
#include "solve.hpp"
#include "cg.hpp"

#endif
