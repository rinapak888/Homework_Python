#!/bin/bash
a=""
while IFS= read -r line 
    do
    if [[ $line == '@'* ]]
    then
    # a+= "$line"
    # a+= " "
    echo "$line" >> abobahex.txt
    else
    echo "$line" | sha256sum  >> abobahex.txt
    fi
    done < aboba.txt