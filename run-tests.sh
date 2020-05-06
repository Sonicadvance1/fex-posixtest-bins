#!/bin/bash

echo "Running native"
rm -rf native
time ./test-runner.sh ./ native

echo
echo "Running fexint ($1)"
rm -rf fexint
time ./test-runner.sh "$1 -U -c irint -n 500 -- " fexint

echo
echo "Running fexjit ($1)"
rm -rf fexjit
time ./test-runner.sh "$1 -U -c irjit -n 500 -- " fexjit
