#!/bin/bash
last_log=$(ls -lt rivet_log | sed -n 3p | awk '{print $9}')
cat $PWD/rivet_log/$last_log

