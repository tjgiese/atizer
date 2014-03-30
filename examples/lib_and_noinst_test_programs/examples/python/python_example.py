#!/usr/bin/env python
#
# Copyright 2013 Timothy John Giese
#

from pytdbsc import *

def read_xyz(filename):
    crd = []
    fh = file(filename,"r")
    liter = iter(fh)
    n = int( liter.next() )
    title = liter.next()
    for i in range(n):
        line = liter.next()
        cols = line.strip().split()
        crd.extend( [ float(c) * 1.88972613373440 for c in cols[1:] ] )
    return crd

crd = read_xyz("ade.xyz")
grd = [0.]*len(crd)
p = pucker("ade.2dbspl")
p.push_back( 0,1,2,3, 2,3,4,5 )

E = p.eval(crd,grd)
print "E = %12.4e"%(E)
for i in range( len(grd)/3 ):
    print "%12.4e%12.4e%12.4e"%(grd[0+i*3],grd[1+i*3],grd[2+i*3])
