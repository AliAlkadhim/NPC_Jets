#!/bin/bash

mkdir -p MERGED
cd PREHADRON
source /afs/desy.de/user/a/aalkadhi/poweheg/rivet+pythia/installnew.sh
rivet-merge -e -o ../MERGED/Paris_CUETP8M_10B_prehadron_merged.yoda pre*
#rm *.yoda

cd ../POSTHADRON

rivet-merge -e -o ../MERGED/Paris_CUETP8M_10B_posthadron_merged.yoda post*
#rm *.yoda	

cd ../MERGED
rivet-cmphistos Paris_CUETP8M_10B_prehadron_merged.yoda:'Title=PS' Paris_CUETP8M_10B_posthadron_merged.yoda:'Title=PS+HAD+MPI'
make-plots --png *.dat

