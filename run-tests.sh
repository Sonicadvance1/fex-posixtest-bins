#!/bin/bash
shopt -s globstar
echo log start > $2
for i in **/*.test; do # Whitespace-safe and recursive
    echo running "$i"
    ${1}"$i"
    echo "$i" $? >> ${2}
done
