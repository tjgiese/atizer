inline lalg::constraint_enforcer::constraint_enforcer
( lalg::ge const conMat, lalg::v const conVals )
  : nfast(conMat.nfast),
    nslow(conMat.nslow),
    constraint_matrix(conMat.begin(),conMat.end()),
    enforcement_matrix(nfast*nslow),
    constraint_values(conVals.begin(),conVals.end())
{
  assert( nslow < nfast );
  assert( conVals.nfast == conMat.nslow );

  // scratch space
  std::vector<double> scratch(nslow*nslow + lalg::sy::query_svd_inverse(nslow));

  // wrappers
  lalg::ge A(nfast,nslow,constraint_matrix.data());
  lalg::ge A_dot_AtAinv(nfast,nslow,enforcement_matrix.data());
  lalg::sy AtA(nslow,scratch.data());

  // A . (At.A)^{-1}
  AtA.dot(A.t(),A).svd_inverse( 1.e-10, scratch.size()-nslow*nslow, AtA.end() );
  A_dot_AtAinv.dot( A, AtA );
}



inline lalg::v & lalg::constraint_enforcer::enforce_constraints
( lalg::v & x )
{
  assert( x.nfast == nfast );

  // scratch space
  // notice that scratch is initialized to constraint values
  std::vector<double> scratch(constraint_values);

  // wrappers
  lalg::ge A(nfast,nslow,constraint_matrix.data());
  lalg::ge A_dot_AtAinv(nfast,nslow,enforcement_matrix.data());
  lalg::v c_minus_Ax(nslow,scratch.data());

  // c - At.x
  c_minus_Ax.dot(-1.,A.t(),x,1.);

  // x := x + A . (At.A)^{-1} . ( c - At.x )
  return x.dot( 1., A_dot_AtAinv, c_minus_Ax, 1. );
}

