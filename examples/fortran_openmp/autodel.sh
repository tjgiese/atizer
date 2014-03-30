#!/bin/bash
if [ -f Makefile ]; then
    make distclean
    rm Makefile
fi
rm -f *~ *.o *.la *.lo Doxyfile Doxyfile.bak doxygen-doc
rm -fr autom4te.cache aclocal.m4 config.guess config.sub depcomp install-sh configure ltmain.sh Makefile.in missing AUTHORS COPYING NEWS README ChangeLog config.log config.status libtool
rm -f $(find . -name "*.pyc")
