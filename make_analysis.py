import argparse
import os
import subprocess as sb
import re

parser=argparse.ArgumentParser(description='temp')
parser.add_argument('--bornsupp', type=int, help='the value of POWHEG born suppression factor')
parser.add_argument('--bornktmin', type=int, help='the value of POWHEG born kt min')
parser.add_argument('--N', type=int, help='the number of events simulated. Default is 1B', default=1000000000)
parser.add_argument('--comment', type=str, help='comment for the run, no whitespaces')
# parser.add_argument('--NAF', type=bool, help='True if running on NAF, else False', required=True,default=False)
args=parser.parse_args()
bornsupp=args.bornsupp
bornktmin=args.bornktmin
N=args.N
comment=args.comment


NAF=True

# os.environ['BASE_DIR_NP']='/home/ali/Desktop/Pulled_Github_Repositories/NPCorrection_InclusiveJets'

if NAF:
    os.environ['BASE_DIR_NP']='/nfs/dust/cms/user/aalkadhi'
else:
    os.environ['BASE_DIR_NP']='/home/ali/Desktop/Pulled_Github_Repositories/NPCorrection_InclusiveJets'
    
if N==1000000000:
    Ns='1B'
    
def make_directory(bornsupp, bornktmin, N):
    BASE_DIR_NP = os.environ['BASE_DIR_NP']
    os.chdir(BASE_DIR_NP)    
    print(BASE_DIR_NP)
    new_dir='suppr%d_bornktmin%d_%s' % (bornsupp, bornktmin, Ns)
    os.system('mkdir  -p %s' % new_dir )
    os.system('cp -r template_run/* %s' % new_dir) 
    
    os.chdir(new_dir)
    os.system('sed -i "s;suppr_250_500M;%s;g" improved_launch_Dijets.sh' % new_dir)
    os.system('sed -i "s;suppr_250_500M;%s;g" improved_condor_submit_Dijets.sub' % new_dir)
    os.system('sed -i "s;suppr_250_500M;%s;g" mkfifo_parallel.sh' % new_dir) 
    os.system('sed -i "s;suppr_250_500M;%s;g" rivet_condor.sub' % new_dir) 
    os.system('sed -i "s;bornktmin 300d0;bornktmin %d;g" powheg.input' % bornktmin) 
    os.system('sed -i "s;bornsuppfact 800d0;bornsuppfact %d;g" powheg.input' % bornsupp)   
    if NAF==True:
        #os.system('condor_submit improved_condor_submit_Dijets.sub')
        os.system(
        '''
        export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
        export DQ2_LOCAL_SITE_ID=DESY-HH_SCRATCHDISK
        source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh
        lsetup asetup
        ''')
        powheg_condor=os.popen('condor_submit improved_condor_submit_Dijets.sub').read()
        #print([l.join('\n') for l in powheg_condor])
        print(powheg_condor)
        powheg_condor=powheg_condor.split()
        njobs=1000#this is the default number of jobs in the condor file above
        #eg 1000 job(s) submitted to cluster 22443072.
        #pattern=r'1000_job.s._submitted_to_cluster_\d+\.'
    	#JOBID=re.findall(pattern, powheg_condor, re.MULTILINE)
        #print('\n JOBID ', JOBID)
        POWHEG_JOBID=powheg_condor[-1][:-1]
        print('POWHEG_JOBID=',POWHEG_JOBID)
        #combine the launch dijets and mkfifo stuff so that everything is done in one batch job (for each run), even the merge and plot parts, because that will be  in the end
        powheg_condor_status=os.popen('condor_q').read()
        for line in powheg_condor_status.split('\n'):
		if POWHEG_JOBID in line:
		# THe condor_q has this structure
		#OWNER    BATCH_NAME      SUBMITTED   DONE   RUN    IDLE   HOLD  TOTAL JOB_IDS
		#aalkadhi ID: 22447158   9/11 02:26    996      _      _      _   1000 22447158.47-828

			print(line,'\n')
	


        #rivet_condor=os.popen('condor_submit rivet_condor.sub').read()
        #print(rivet_condor)
        #RIVET_JOBID=rivet_condor[-1][:-1]
        #print('RIVET JOBID=', RIVET_JOBID)





def main():
    make_directory(bornsupp, bornktmin, N)
    
    
    
    
    
    
if __name__ == '__main__':
    main()
    BASE_DIR_NP = os.environ['BASE_DIR_NP']
    os.chdir(BASE_DIR_NP)
