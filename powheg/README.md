The base working directory for parallel powheg is `/afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets`, go there.

There you will see **improved_launch_Dijets.sh**. This file's contents are written bellow. The idea is that each time this script is run (by condor, in parallel), the counter `rnd` is appended by 1. Therefore, each run is associated with the value of `rnd`. Each time this is run, the script makes a new directory associated with `rnd`, it copies the `powheg.input` to that run's directory, it goes to that run's directory, it sources the powheg setup script, it changes the `iseed` value in the powheg input in that run's directory, it then executes `Dijets` script, and it exists the directory.

```
#!/bin/bash
echo "starting"
echo "shell" $0


rnd=$(($1 + 1))
current_dir=$(pwd)
mkdir -p ${current_dir}/run_nominal${rnd}
#cp -p ${current_dir}/powheg.input ${current_dir}/run_rominal${rnd}/powheg.input
cp /afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets/suppr_250/powheg.input /afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets/suppr_250/run_nominal${rnd}
#cd ${current_dir}/run_nominal${rnd}
cd /afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets/suppr_250/run_nominal${rnd}

source /afs/desy.de/user/a/aalkadhi/simone_setup.sh

alias Dijets=/afs/desy.de/user/a/aalkadhi/poweheg/2-POWHEG-BOX/POWHEG-BOX/Dijet/pwhg_main


sed -i "s;iseed    5421;iseed    ${rnd};g" ${current_dir}/run_nominal${rnd}/powheg.input

echo $1,$rnd
#echo $rnd | Dijets > powheglog${rnd}_p2.txt
Dijets
cd ${current_dir}
```
The script that allows this to run in parallel is **improved_condor_submit_Dijets.sub**, where Queue is the number of jobs, and the rest are self-explanatory.

```
Executable  = /afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets/suppr_250/improved_launch_Dijets.sh
Arguments  = $(Process)
Log = logs/log_$(Process).txt

Output = out/out_$(Process).txt

Error = error/err_$(Process).txt
#+RequestRunTime=500000
Queue 500
```
