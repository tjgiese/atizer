#!/bin/bash
set -e
set -u

PREFIX=$HOME/devel/local
OPENMP=--with-openmp

function numcores {
    awk -F: '/^physical/ && !ID[$2] { P++; ID[$2]=1 }; /^cpu cores/ { CORES=$2 };  END { print CORES*P }' /proc/cpuinfo
}

if [ $# -gt 1 ]; then
    echo "Error: You should specify at most one argument to avoid race-conditions"
    echo "./make"
    echo "./make debug"
    echo "./make clean"
    echo "./make doxygen-doc"
    echo "./make dist-gzip"
    echo "./make rm  (note: this delete's everything)"
    exit 1
fi

if [ $# -gt 0 ]; then
    if [ "$1" == "rm" ]; then
	if [ -e Makefile ]; then
	    make uninstall
	fi
	if [ -e autodel.sh ]; then
	    ./autodel.sh
	fi
	rm -fr autodel.sh autogen.sh configure.ac Makefile.am local
        exit
    fi
fi

if [ ! -e configure ]; then
    if [ ! -e configure.ac ]; then
	if [ -e __init__.py ]; then
	    ./__init__.py --prefix=$PREFIX $OPENMP
	fi
    fi
fi

if [ ! -e configure ]; then
    autoreconf -fvi
fi

if [ ! -e Makefile ]; then
    ./configure --prefix=$PREFIX $OPENMP
fi

if [ $# -gt 0 ]; then
    if [ "$1" == "opt" ] || [ "$1" == "debug" ]; then
	make $@ -j $(numcores)
	make install
    elif [ "$1" == "clean" ] || [ "$1" == "distclean" ]; then
	make uninstall
	make $@
    else
	make $@ -j $(numcores)
    fi
else
    make opt -j $(numcores)
    make install
fi

