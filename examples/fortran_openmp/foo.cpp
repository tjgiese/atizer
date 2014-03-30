#ifdef _OPENMP
#include <omp.h>
#endif
#include <iostream>

extern "C"
{
  void foo_()
  {
    int i = -2;
#ifdef _OPENMP
    i = omp_get_num_threads();
#endif
    std::cout << "i=" << i << "\n";
  }
}
