#!/bin/bash
#
for d in * ; do
    if [ -d "$d" ]; then
        # Your operations on directories here
        echo "Processing directory: $d"
	cp  ../../../Magnetic_data_add_new_feature/INS_SW_MC/$d/sym.txt   $d/
    fi
done
