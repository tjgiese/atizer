#!/bin/sh -e
maketar() {
    echo ""
    echo "make dist-gzip"
    make dist-gzip
    echo ""
    mkdir -p distrib
    if [ ! -f $1 ]; then
        echo "$1 does not exist; not copying to distrib/"
        rm $1
    else
        if [ ! -f distrib/$1 ]; then
            echo "mv -f  $1 distrib/"
            mv -f $1 distrib/
        else
            echo "tar -xzOf $1 | md5sum" "=" "$(tar -xzOf $1 | md5sum)"
            echo "tar -xzOf distrib/$1 " "=" "$(tar -xzOf distrib/$1 | md5sum)"
            if [ "$(tar -xzOf $1 | md5sum)" = "$(tar -xzOf distrib/$1 | md5sum)" ]; then
                echo "Not copying $1 to distrib/ because they are the same"
                rm $1
            else
                echo "cp -f  $1 distrib/"
                mv -f $1 distrib/
            fi
        fi
    fi
    echo ""
}

touch NEWS README AUTHORS ChangeLog
echo "For private use only; do not redistribute" > COPYING
autoreconf -fvi #--force --install --verbose "$srcdir"
./configure $@
maketar fortran_example-0.1.tar.gz
