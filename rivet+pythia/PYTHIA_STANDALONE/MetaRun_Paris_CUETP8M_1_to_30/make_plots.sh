#!/bin/bash
source /afs/desy.de/user/a/aalkadhi/poweheg/rivet+pythia/installnew.sh

rivet-cmphistos Paris_CUETP8M_100T_PREHADRON_1_to_30.yoda:'Title=PS' Paris_CUETP8M_100T_POSTHADRON_1_to_30.yoda:'Title=PS+HAD+MPI'

make-plots --png *.dat