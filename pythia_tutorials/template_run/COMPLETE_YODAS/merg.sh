#!/bin/bash

mkdir -p MERGED
cd PREHADRON
source /afs/desy.de/user/a/aalkadhi/poweheg/rivet+pythia/installnew.sh
rivet-merge -e -o ../MERGED/some_run_prehadron_merged.yoda pre*
#rm *.yoda

cd ../POSTHADRON

rivet-merge -e -o ../MERGED/some_run_posthadron_merged.yoda post*
#rm *.yoda	

