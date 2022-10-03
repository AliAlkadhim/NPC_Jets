#!/bin/bash

source /afs/desy.de/user/a/aalkadhi/poweheg/rivet+pythia/installnew.sh

rivet-merge -e -o Paris_CUETP8M_10T_1_2_COMBINED_prehadron.yoda /nfs/dust/cms/user/aalkadhi/PYTHIA_STANDALONE/Paris_CUETP8M_10T_2/COMPLETE_YODAS/MERGED/Paris_CUETP8M_10T_2_prehadron_merged.yoda \
/nfs/dust/cms/user/aalkadhi/PYTHIA_STANDALONE/Paris_CUETP8M_10T/COMPLETE_YODAS/MERGED/Paris_CUETP8M_10T_prehadron_merged.yoda
#rm *.yoda


rivet-merge -e -o Paris_CUETP8M_10T_1_2_COMBINED_posthadron.yoda /nfs/dust/cms/user/aalkadhi/PYTHIA_STANDALONE/Paris_CUETP8M_10T_2/COMPLETE_YODAS/MERGED/Paris_CUETP8M_10T_2_posthadron_merged.yoda \
/nfs/dust/cms/user/aalkadhi/PYTHIA_STANDALONE/Paris_CUETP8M_10T/COMPLETE_YODAS/MERGED/Paris_CUETP8M_10T_posthadron_merged.yoda
#rm *.yoda	

