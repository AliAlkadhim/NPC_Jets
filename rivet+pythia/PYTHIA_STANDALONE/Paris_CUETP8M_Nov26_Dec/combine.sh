#!/bin/bash
source /afs/desy.de/user/a/aalkadhi/poweheg/rivet+pythia/installnew.sh
combined_dir=/nfs/dust/cms/user/aalkadhi/PYTHIA_STANDALONE/COMBINE_ALL_NOV26_SOFAR
base_dir=/nfs/dust/cms/user/aalkadhi/PYTHIA_STANDALONE

rivet-merge -e -o COMBINED_PREHADRON.yoda $base_dir/Paris_CUETP8M_Nov26_45_to_51/PREHADRON_45_to51.yoda $base_dir/Paris_CUETP8M_Nov26_37_to_45/Paris_CUETP8M_Nov26_37_to_45_PREHADRON.yoda $base_dir/Paris_CUETP8M_Nov26_16_to_33/Paris_CUETP8M_Nov26_16_to_37_PREHADRON.yoda $base_dir/Paris_CUETP8M_Nov26_2_to_15/Nov_26_all_merged_prehadron.yoda $base_dir/Paris_CUETP8M_100T_COMBINED/MERGED/Paris_CUETP8M_100T_PREHADRON_1_to_30.yoda $base_dir/Paris_CUETP8M_10T_1_2_COMBINED/Paris_CUETP8M_10T_1_2_COMBINED_prehadron.yoda \
$base_dir/Paris_CUETP8M_10T_4.5T_COMBINED/Paris_CUETP8M_10T_4.5T_MERGED_PREHADRON.yoda

















rivet-merge -e -o COMBINED_POSTHADRON.yoda $base_dir/Paris_CUETP8M_Nov26_45_to_51/POSTHADRON_45_to51.yoda $base_dir/Paris_CUETP8M_Nov26_37_to_45/Paris_CUETP8M_Nov26_37_to_45_PREHADRON.yoda $base_dir/Paris_CUETP8M_Nov26_16_to_33/Paris_CUETP8M_Nov26_16_to_37_POSTHADRON.yoda $base_dir/Paris_CUETP8M_Nov26_2_to_15/Nov_26_all_merged_posthadron.yoda $base_dir/Paris_CUETP8M_100T_COMBINED/MERGED/Paris_CUETP8M_100T_POSTHADRON_1_to_30.yoda $base_dir/Paris_CUETP8M_10T_1_2_COMBINED/Paris_CUETP8M_10T_1_2_COMBINED_posthadron.yoda \
$base_dir/Paris_CUETP8M_10T_4.5T_COMBINED/Paris_CUETP8M_10T_4.5T_MERGED_POSTHADRON.yoda
