#!/bin/bash
echo "shell" $0
rnd=$(($1 + 1))
rnd=$(printf "%01d\n" $rnd)
echo $rnd

