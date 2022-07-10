#!/bin/bash
sed -i "s;suppr_250_500M;suppr800_bornktmin300_100M;g" improved_launch_Dijets.sh
sed -i "s;suppr_250_500M;suppr800_bornktmin300_100M;g" improved_condor_submit_Dijets.sub

sed -i "s;suppr_250_500M;suppr800_bornktmin300_100M;g" mkfifo_parallel.sh
sed -i "s;suppr_250_500M;suppr800_bornktmin300_100M;g" rivet_condor.sub


