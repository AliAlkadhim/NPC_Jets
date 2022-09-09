import argparse
import os
import subprocess as sb

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


NAF=False

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
        os.system('condor_submit improved_condor_submit_Dijets.sub')
    
    
def main():
    make_directory(bornsupp, bornktmin, N)
    
    
    
    
    
    
if __name__ == '__main__':
    main()
    BASE_DIR_NP = os.environ['BASE_DIR_NP']
    os.chdir(BASE_DIR_NP)