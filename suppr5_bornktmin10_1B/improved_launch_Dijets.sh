#!/bin/bash
echo "starting"
echo "shell" $0


rnd=$(($1 + 1))
#current_dir=$(pwd)
# ON AFS
#current_dir=/afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets/suppr_250_2
# ON DUST
current_dir=/nfs/dust/cms/user/aalkadhi/suppr5_bornktmin10_1B
mkdir -p ${current_dir}/run_${rnd}
#cp -p ${current_dir}/powheg.input ${current_dir}/run_rominal${rnd}/powheg.input
cp /nfs/dust/cms/user/aalkadhi/suppr5_bornktmin10_1B/powheg.input /nfs/dust/cms/user/aalkadhi/suppr5_bornktmin10_1B/run_${rnd}
#cd ${current_dir}/run_nominal${rnd}
cd /nfs/dust/cms/user/aalkadhi/suppr5_bornktmin10_1B/run_${rnd}

source /afs/desy.de/user/a/aalkadhi/simone_setup.sh

alias Dijets=/afs/desy.de/user/a/aalkadhi/poweheg/2-POWHEG-BOX/POWHEG-BOX/Dijet/pwhg_main


sed -i "s;iseed    5421;iseed    ${rnd};g" powheg.input

echo $1,$rnd
#echo $rnd | Dijets > powheglog${rnd}_p2.txt
Dijets
rm *.dat *.top
### zip pwgevents.zip pwgevent.lhe
cd ${current_dir}
