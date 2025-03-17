#!/bin/bash
rm -f T.dat
echo "Material   T_exp     T_MC    T_MC*    S    Error" > T.dat
for d in * ; do
    if [ -d "$d" ]; then
	data=`tail -1  $d/T.txt` 
        echo "$d" $data >> T.dat
    fi

done
