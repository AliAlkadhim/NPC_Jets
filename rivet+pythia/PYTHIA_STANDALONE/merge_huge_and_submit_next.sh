#!/bin/bash
CURRENT_DIR=/nfs/dust/cms/user/aalkadhi/PYTHIA_STANDALONE
cd $CURRENT_DIR
echo $CURRENT_DIR

SLEEP_TIME="1200"

# DESCRIPTION: go to each of Paris_CUETP8M_100T_{1...6} and merge the outputs 
#of Paris_CUETP8M_100T_{1...6}/PREHADRON into Paris_CUETP8M_100T_COMBINED/PREHADRON/Paris_CUETP8M_100T_{1...6} e.g.
#  Paris_CUETP8M_100T_1/PREHADRON -> Paris_CUETP8M_100T_COMBINED/PREHADRON/Paris_CUETP8M_100T_1_PREHADRON.yoda


export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
export DQ2_LOCAL_SITE_ID=DESY-HH_SCRATCHDISK
source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh
lsetup asetup


Huge_run_merged_dir=/nfs/dust/cms/user/aalkadhi/PYTHIA_STANDALONE/Paris_CUETP8M_100T_COMBINED
Huge_run_merged_dir_PREHADRON=${Huge_run_merged_dir}_PREHADRON
Huge_run_merged_dir_POSTHADRON=${Huge_run_merged_dir}_POSTHADRON

echo $Huge_run_merged_dir_PREHADRON


source /afs/desy.de/user/a/aalkadhi/poweheg/rivet+pythia/installnew.sh

runname=Paris_CUETP8M_100T_
i_start=0
i_end=6
for i in {1..20}
do
    #check if my quota is still big enough
    my-dust-quota
    #check if I how many jobs I have running
    condor_q
    #Potentially do condor_rm -all here?

    #Go to the next run
    # cd $CURRENT_DIR
    runname_i=$runname$i
    echo $runname_i
    cd $CURRENT_DIR/$runname_i
    
    #RUN IT WITH CONDOR
    condor_submit rivet_condor.sub
    sleep $SLEEP_TIME

    #go to the PREHADRON dir of this run
    cd COMPLETE_YODAS/PREHADRON
    pwd
    ls -lt | head
    Number_of_pre_files=`ls -l | wc -l`
    echo "MERGING $vNumber_of_pre_files$ PREHADRON FILES"
    #merge all the jobs of this run into the meta_analysis/prehadron directory
    rivet-merge -e -o ${Huge_run_merged_dir_PREHADRON}/${runname_i}_PREHADRON.yoda pre*
    #remove the PREHADRON yodas
    rm *.yoda

    cd ../POSTHADRON
    ls -lt | head
    Number_of_post_files=`ls -l | wc -l`
    echo "MERGING $Number_of_post_files$ PREHADRON FILES"
    rivet-merge -e -o ${Huge_run_merged_dir_POSTHADRON}/${runname_i}_POSTHADRON.yoda 
    rm *.yoda
    echo "CONDOR JOBS STILL RUNNING:\n"
    condor_q
    echo "REMOVING THEM:\n"
    condor_rm -all


    #condor_rm jobid of this run
done
