#!/bin/bash
echo "starting"
echo "shell" $0


rnd=$(($1 + 1))
current_dir=$(pwd)
mkdir -p ${current_dir}/run_${rnd}
#cp -p ${current_dir}/powheg.input ${current_dir}/run_rominal${rnd}/powheg.input
cp /afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets/suppr_250/powheg.input /afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets/suppr_250/run_${rnd}
#cd ${current_dir}/run_nominal${rnd}
cd /afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets/suppr_250/run_${rnd}

source /afs/desy.de/user/a/aalkadhi/simone_setup.sh

alias Dijets=/afs/desy.de/user/a/aalkadhi/poweheg/2-POWHEG-BOX/POWHEG-BOX/Dijet/pwhg_main


sed -i "s;iseed    5421;iseed    ${rnd};g" ${current_dir}/run_${rnd}/powheg.input

echo $1,$rnd
#echo $rnd | Dijets > powheglog${rnd}_p2.txt
Dijets
cd ${current_dir}
