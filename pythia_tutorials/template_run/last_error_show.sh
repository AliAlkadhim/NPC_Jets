#!/bin/bash
last_error=$(ls -lt rivet_error | sed -n 3p | awk '{print $9}')
cat $PWD/rivet_error/$last_error

