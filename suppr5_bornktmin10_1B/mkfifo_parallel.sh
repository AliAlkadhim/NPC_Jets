#!/bin/bash
echo "shell" $0
rnd=$(($1 + 1))
rnd=$(printf "%01d\n" $rnd)

#current_dir=$(pwd)
# ON AFS
#current_dir=/afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets/suppr_250_2/
# ON DUST
current_dir=/nfs/dust/cms/user/aalkadhi/suppr5_bornktmin10_1B/
#go to the run directory
cd /nfs/dust/cms/user/aalkadhi/suppr5_bornktmin10_1B/run_${rnd}

#remove everything but the pwgevents.lhe files
rm powheg.input
rm *.dat
rm *.top
rm pwhg_checklimits
rm FlavRegList
#source env
source /afs/desy.de/user/a/aalkadhi/poweheg/rivet+pythia/installnew.sh
#copy main pythia script to this directory
cp /nfs/dust/cms/user/aalkadhi/suppr5_bornktmin10_1B/main_scripts/* .

#PREHADRON
#make a fifo associated with that run in that run directory. First generate the hepmc events into fifo
#./main42 main42_prehadron.cmnd prehadron${rnd}.fifo &
#then attach the analysis at the opposite end
#rivet --ignore-beams -o prehadron${rnd}.yoda -a CMS_2021_I1972986 prehadron${rnd}.fifo
#rivet --ignore-beams -o prehadron${rnd}.yoda -a CMS_2016_I1487277 prehadron${rnd}.fifo
#remove the fifo file
#rm prehadron${rnd}.fifo
#copy the yoda hist file into COMPLETE_YODAS dir
#mv prehadron${rnd}.yoda /nfs/dust/cms/user/aalkadhi/suppr5_bornktmin10_1B/COMPLETE_YODAS/PREHADRON/






#POSTHADRON
#make a fifo associated with that run in that run directory. First generate the hepmc events into fifo
./main42 main42_posthadron.cmnd posthadron${rnd}.fifo &
#then attach the analysis at the opposite end
rivet --ignore-beams -o posthadron${rnd}.yoda -a CMS_2021_I1972986 posthadron${rnd}.fifo
#rivet --ignore-beams -o prehadron${rnd}.yoda -a CMS_2016_I1487277 posthadron${rnd}.fifo
#remove the fifo file
rm posthadron${rnd}.fifo
#copy the yoda hist file into COMPLETE_YODAS dir
mv posthadron${rnd}.yoda /nfs/dust/cms/user/aalkadhi/suppr5_bornktmin10_1B/COMPLETE_YODAS/POSTHADRON/


#BOTH
#rm posthadron${rnd}.fifo prehadron${rnd}.fifo
#cp prehadron${rnd}.yoda posthadron${rnd}.yoda /afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets/suppr_250/COMPLETE_YODAS/
#rm prehadron${rnd}.fifo
#cp prehadron${rnd}.yoda /afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets/suppr_250/COMPLETE_YODAS/

#Finally, go back to current_dir
cd /nfs/dust/cms/user/aalkadhi/suppr5_bornktmin10_1B/


