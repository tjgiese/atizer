#ifndef _lalg_constraint_enforcer_hpp_
#define _lalg_constraint_enforcer_hpp_

namespace lalg
{

  class constraint_enforcer
  {
  public:
    constraint_enforcer( lalg::ge const conMat, lalg::v const conVals );
    lalg::v & enforce_constraints( lalg::v & x );

    int nfast, nslow;
    std::vector<double> constraint_matrix;
    std::vector<double> enforcement_matrix;
    std::vector<double> constraint_values;
  };

}

#endif
