with open('merge_all_Nov_25.sh','w') as f:
    f.write('#!/bin/bash\n')
    f.write('source /afs/desy.de/user/a/aalkadhi/poweheg/rivet+pythia/installnew.sh\n')
    f.write('rivet-merge -e -o Nov_26_all_merged_prehadron.yoda ')
    for i in range(2,16):
        f.write(' /nfs/dust/cms/user/aalkadhi/PYTHIA_STANDALONE/Paris_CUETP8M_Nov26_%s/COMPLETE_YODAS/MERGED/Paris_CUETP8M_Nov26_%s_prehadron_merged.yoda' % (str(int(i)), str(int(i))) )
    f.write('\n')
    f.write('rivet-merge -e -o Nov_26_all_merged_posthadron.yoda ')
    for i in range(2,16):
        f.write(' /nfs/dust/cms/user/aalkadhi/PYTHIA_STANDALONE/Paris_CUETP8M_Nov26_%s/COMPLETE_YODAS/MERGED/Paris_CUETP8M_Nov26_%s_posthadron_merged.yoda' % (str(int(i)), str(int(i)) ))

