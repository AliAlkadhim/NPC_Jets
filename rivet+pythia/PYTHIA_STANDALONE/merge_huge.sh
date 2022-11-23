#!/bin/bash
CURRENT_DIR=/nfs/dust/cms/user/aalkadhi/PYTHIA_STANDALONE
cd $CURRENT_DIR
echo $CURRENT_DIR

# DESCRIPTION: go to each of Paris_CUETP8M_100T_{1...6} and merge the outputs 
#of Paris_CUETP8M_100T_{1...6}/PREHADRON into Paris_CUETP8M_100T_COMBINED/PREHADRON/Paris_CUETP8M_100T_{1...6} e.g.
#  Paris_CUETP8M_100T_1/PREHADRON -> Paris_CUETP8M_100T_COMBINED/PREHADRON/Paris_CUETP8M_100T_1_PREHADRON.yoda


Huge_run_merged_dir=/nfs/dust/cms/user/aalkadhi/PYTHIA_STANDALONE/Paris_CUETP8M_100T_COMBINED
Huge_run_merged_dir_PREHADRON=${Huge_run_merged_dir}_PREHADRON
Huge_run_merged_dir_POSTHADRON=${Huge_run_merged_dir}_POSTHADRON

echo $Huge_run_merged_dir_PREHADRON


source /afs/desy.de/user/a/aalkadhi/poweheg/rivet+pythia/installnew.sh

runname=Paris_CUETP8M_100T_
i_start=0
i_end=6
for i in {1..6}
do
    my-dust-quota
    # cd $CURRENT_DIR
    runname_i=$runname$i
    echo $runname_i
    cd $CURRENT_DIR/$runname_i
    cd COMPLETE_YODAS/PREHADRON
    pwd
    ls -lt | head
    rivet-merge -e -o ${Huge_run_merged_dir_PREHADRON}/${runname_i}_PREHADRON.yoda pre*
    rm *.yoda
    cd ../POSTHADRON
    ls -lt | head
    rivet-merge -e -o ${Huge_run_merged_dir_POSTHADRON}/${runname_i}_POSTHADRON.yoda 
    rm *.yoda

    # echo ${Huge_run_merged_dir_PREHADRON}/${runname_i}_PREHADRON.yoda
done
