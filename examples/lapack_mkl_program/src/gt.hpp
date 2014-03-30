#ifndef _lalg_gt_hpp_
#define _lalg_gt_hpp_

namespace lalg
{
  class ge;
}

namespace lalg
{
  class gt
  {
  public:
    gt( int m, int n, double * d );
    int nfast,nslow;
    double * data;
  };
}


#endif
