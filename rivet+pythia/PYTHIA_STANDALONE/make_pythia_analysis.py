import os
import argparse


parser=argparse.ArgumentParser(description='temp')
parser.add_argument('--runname', type=str, help='name of the run',required=True)
parser.add_argument('--condor', type=bool, help='boolean whether to run condor')
args=parser.parse_args()
runname=args.runname
condor=args.condor
NAF=True

#Remember that tune CUETP8M1-NNPDF2.3LO is the important CMS one, which has tune:pp=
#Tune:pp=18 #15 for CMS UE Tune CUETP8S1-CTEQ6L1, the default is Monash2013, 18 for CUETP8M1-NNPDF2.3LO

if NAF:
    os.environ['BASE_DIR_PYTHIA']='/nfs/dust/cms/user/aalkadhi/PYTHIA_STANDALONE'
# else:
#     os.environ['BASE_DIR_PYTHIA']='/home/ali/Desktop/Pulled_Github_Repositories/NPCorrection_InclusiveJets'
    
# if N==1000000000:
#     Ns='1B'
    
def make_directory():
    BASE_DIR_PYTHIA = os.environ['BASE_DIR_PYTHIA']
    os.chdir(BASE_DIR_PYTHIA)    
    print(BASE_DIR_PYTHIA)
    new_dir=runname
    os.system('mkdir  -p %s' % new_dir )
    os.system('cp -r template_run/* %s' % new_dir) 
    os.chdir(new_dir)

    os.system('sed -i "s;some_run;%s;g" pythia_parallel.sh' % new_dir) 
    os.system('sed -i "s;some_run;%s;g" rivet_condor.sub' % new_dir) 
    os.system('sed -i "s;some_run;%s;g" COMPLETE_YODAS/merg.sh' % new_dir)
#    if condor:
#        os.system(
#            '''
#            export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
#            export DQ2_LOCAL_SITE_ID=DESY-HH_SCRATCHDISK
#            source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh
#            lsetup asetup
#            ''')
#
#        rivet_condor = os.popen('condor_submit rivet_condor.sub').read()
#        print(rivet_condor)
#        rivet_condor=rivet_condor.split()
#        RIVET_JOBID=rivet_condor[-1][:-1]
#        print('RIVET JOBID = ', RIVET_JOBID)

def main():
    make_directory()

if __name__=="__main__":
    main()
    BASE_DIR_PYTHIA = os.environ['BASE_DIR_PYTHIA']
    os.chdir(BASE_DIR_PYTHIA)
	
