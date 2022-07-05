
Rivet can be run two ways:
1. On `hepmc` files directly, with `rivet -a MC_JETS test.hepmc` (where `test.hepmc` was produced with `./main42.cc main42.cmnd hepmcout.hepmc`). The CMS QCD incl.jet rivet analysis is `CMS_2021_I1972986` For example, 

`rivet -a CMS_2021_I1972986 --ignore-beams retest_pre_hadron.hepmc`

This is inconvenient as the hepmc files are huge and will take forever to run. The second, preferred way is to use a FIFO (first in, first out) pipe



2. use pythia to generate hepmc events going to the fifo. 


`./main42 main42.cmnd tut_fifo.fifo &` 

where I have pwgevents.lhe and main42 files in that directory. Now attach Rivet to the other end of the pipe:

`rivet -a CMS_2021_I1972986 -a MC_JETS tut_fifo.fifo`

This produces a Rivet.yoda file. To produce all the plots as an html file, do

`rivet-mkhtml --mc-errs Rivet.yoda`  




-----------


Do `rivet --help` and `agile-runmc --help` to test that you have ruvet working.
With `pwgevents.lhe` in directory.

### Rivet/pythia for one `.lhe` file.

The starting directory for my `rivet+pythia` workflow is `/afs/desy.de/user/a/aalkadhi/poweheg/rivet+pythia/13TeV_10k_NNPDF`.


The script below, **mkfifo_from_lhe.sh**, makes an output `.yoda` histogram file from an existing `pwgevent.lhe` file that exists in the same directory, by using a fifo pipe, whire hepmc is not saved. You can in principle delete the `.fifo` file if you sure that the `.yoda` output file is what you want. 

```
#!/bin/bash
./main42 main42_prehadron.cmnd prehadron.fifo &
rivet --ignore-beams -o prehadron.yoda -a CMS_2016_I1487277 -a MC_JETS prehadron.fifo
```








Example: currentlt working in /afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets/run_nominal/rivet_pythia , where here I have
`main42  main42.cmnd  minnlo_0001.yoda  out  pwgevents.lhe  rivet_fifo_onefile.sh`

**rivet_fifo_many_lhe_files.sh**

```
#!/bin/bash
echo "shell" $0
rnd=$(($1 + 1))
rnd=$(printf "%04d\n" $rnd)
echo $rnd

#cd out

source /afs/desy.de/user/a/amoroso/cmsarea/powheg/POWHEG-BOX-V2/Zj/ZjMiNNLO/shower/installnew.sh
#export RIVET_ANALYSIS_PATH=/afs/desy.de/user/a/amoroso/cmsarea/powheg/POWHEG-BOX-V2/Zj/ZjMiNNLO/sho$

#lhefile=/afs/desy.de/user/a/amoroso/cmsarea/powheg/POWHEG-BOX-V2/Zj/ZjMiNNLO/testrun/Zmumu13_Q0_unz$
#lhefile=/afs/desy.de/user/a/amoroso/cmsarea/powheg/POWHEG-BOX-V2/hvq/decay-dilep/pwgevents.lhe
#echo $lhefile
#sed  's|pwgevents.lhe|'${lhefile}'|g' /afs/desy.de/user/a/amoroso/cmsarea/powheg/POWHEG-BOX-V2/Zj/Z$


mkfifo myfifo_$rnd
./main42 main42.cmnd myfifo_onefile.fifo &
rivet  --ignore-beams -o minnlo_$rnd.yoda -a MC_JETS,CMS_2016_I1487277  myfifo_onefile.fifo
rm -r myfifo_onefile.fifo
```











Go to `/afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets/run_nominal/rivet_pythia`
 * I made `out_posthadron` and `out_posthadron` directories, copied pwgevents.lhe and main42 to each.
* Then I copied main42_posthadron.cmnd to out_posthadron and the same to prehadron
* I then ran `rivet_fifo_onefile.sh` where once the directories in it are for prehadron, and again where the directories/files in it are those corresponding to post hadron.

```
#!/bin/bash
echo "shell" $0
rnd=$(($1 + 1))
rnd=$(printf "%04d\n" $rnd)
echo $rnd

cd out_posthadron

source /afs/desy.de/user/a/amoroso/cmsarea/powheg/POWHEG-BOX-V2/Zj/ZjMiNNLO/shower/installnew.sh
#export RIVET_ANALYSIS_PATH=/afs/desy.de/user/a/amoroso/cmsarea/powheg/POWHEG-BOX-V2/Zj/ZjMiNNLO/sho$

#lhefile=/afs/desy.de/user/a/amoroso/cmsarea/powheg/POWHEG-BOX-V2/Zj/ZjMiNNLO/testrun/Zmumu13_Q0_unz$
#lhefile=/afs/desy.de/user/a/amoroso/cmsarea/powheg/POWHEG-BOX-V2/hvq/decay-dilep/pwgevents.lhe
#echo $lhefile
#sed  's|pwgevents.lhe|'${lhefile}'|g' /afs/desy.de/user/a/amoroso/cmsarea/powheg/POWHEG-BOX-V2/Zj/Z$


mkfifo myfifo_onefile.fifo
./main42 main42_posthadron.cmnd myfifo_onefile.fifo &
rivet  --ignore-beams -o post_hadron.yoda -a MC_JETS,CMS_2016_I1487277  myfifo_onefile.fifo
rm -r myfifo_onefile.fifo
```

* Now how do i use rivet to draw the ratio histogram between them using MC_JETS,CMS_2016_I1487277, and how can I plot both histograms on the same plot




---------

To get an analysis template, which you can fill in with an FS
projection and a particle loop, run e.g. rivet-mkanalysis
MY_TEST_ANALYSIS – this will make the required files.
Once you’ve filled it in, you can either compile directly with g++ ,
using the rivet-config script as a compile flag helper, or run
rivet-buildplugin MY_TEST_ANALYSIS.cc
To run, first export RIVET_ANALYSIS_PATH=$PWD , then run rivet
as before. . . or add the --pwd option to the rivet command line.


---------

compare histos
`rivet-cmphistos pre_hadron.yoda:pre_hadron post_hadron.yoda:post_hadron --errs`


-------


`yodamerge`

`yodamerge_tmp.py run1.yoda run2.yoda run3.yoda`


----------------

# Rivet Analysis with condor for many `.lhe` files

Here the assumption is that you have a directory composed of many sub-directories, each corresponding to a powheg run with a corresponding powheg `pwgevents.lhe` file, such as in `/afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets/suppr_250` (for a tutorial on how this was generated, see the powheg tutorials). We want to write an executable (ending in `.sh`) that implements the following algorithm:
```
for each run in Number_of_runs, do
  cd to run_i
  source rivet+pythia setup
  cp ../main scripts to that directory
  ./main42 main42_prehadron.cmnd prehadron$(i).fifo &
  rivet --ignore-beams -o prehadron$(i).yoda -a CMS_2016_I1487277 -a MC_JETS prehadron$(i).fifo
  ./main42 main42_posthadron.cmnd posthadron$(i).fifo &
  rivet --ignore-beams -o postdron$(i).yoda -a CMS_2016_I1487277 -a MC_JETS posthadron$(i).fifo
  rm posthadron$(i).fifo prehadron$(i).fifo
  cp prehadron$(i).yoda prehadron$(i).yoda ../COMPLETE_YODAS/
  
```

## Implementation in `/nfs/dust/cms/user/aalkadhi/suppr_250_2` 

Use DUST for extra storage. (prevous implementation was in `/afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets/suppr_250`)

**mkfifo_parallel.sh**

```
#!/bin/bash
echo "shell" $0
rnd=$(($1 + 1))
rnd=$(printf "%01d\n" $rnd)

#current_dir=$(pwd)
# ON AFS
#current_dir=/afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets/suppr_250_2/
# ON DUST
current_dir=/nfs/dust/cms/user/aalkadhi/suppr_250_2/
#go to the run directory
cd /nfs/dust/cms/user/aalkadhi/suppr_250_2/run_${rnd}

#remove everything but the pwgevents.lhe files
rm powheg.input
#source env
source /afs/desy.de/user/a/aalkadhi/poweheg/rivet+pythia/installnew.sh
#copy main pythia script to this directory
cp /nfs/dust/cms/user/aalkadhi/suppr_250_2/main_scripts/* .

#PREHADRON
#make a fifo associated with that run in that run directory. First generate the hepmc events into fi$
#./main42 main42_prehadron.cmnd prehadron${rnd}.fifo &
#then attach the analysis at the opposite end
#rivet --ignore-beams -o prehadron${rnd}.yoda -a CMS_2021_I1972986 prehadron${rnd}.fifo
#rivet --ignore-beams -o prehadron${rnd}.yoda -a CMS_2016_I1487277 prehadron${rnd}.fifo
#remove the fifo file
#rm prehadron${rnd}.fifo
#copy the yoda hist file into COMPLETE_YODAS dir
#mv prehadron${rnd}.yoda /nfs/dust/cms/user/aalkadhi/suppr_250_2/COMPLETE_YODAS/PREHADRON/

#POSTHADRON
#make a fifo associated with that run in that run directory. First generate the hepmc events into fi$
./main42 main42_posthadron.cmnd posthadron${rnd}.fifo &
#then attach the analysis at the opposite end
rivet --ignore-beams -o posthadron${rnd}.yoda -a CMS_2021_I1972986 posthadron${rnd}.fifo
#rivet --ignore-beams -o prehadron${rnd}.yoda -a CMS_2016_I1487277 posthadron${rnd}.fifo
#remove the fifo file
rm posthadron${rnd}.fifo
#copy the yoda hist file into COMPLETE_YODAS dir
mv posthadron${rnd}.yoda /nfs/dust/cms/user/aalkadhi/suppr_250_2/COMPLETE_YODAS/POSTHADRON/


#BOTH (Don't do)
#rm posthadron${rnd}.fifo prehadron${rnd}.fifo
#cp prehadron${rnd}.yoda posthadron${rnd}.yoda #/afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets/suppr_250/COMPLETE_YODAS/
#rm prehadron${rnd}.fifo
#cp prehadron${rnd}.yoda #/afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets/suppr_250/COMPLETE_YODAS/

#Finally, go back to current_dir
cd /nfs/dust/cms/user/aalkadhi/suppr_250_2/

```

`mkdir -p rivet_logs rivet_error rivet_out`

**rivet_condor.sub**
```
Executable  = /nfs/dust/cms/user/aalkadhi/suppr_250_2/mkfifo_parallel.sh
Arguments  = $(Process)
Log = rivet_log/log_$(Process).txt

Output = rivet_out/out_$(Process).txt

Error = rivet_error/err_$(Process).txt
#+RequestRunTime=500000
Queue 1000
```

------


`yodamerge`

`yodamerge_tmp.py -o merged_prehadron.yoda run1.yoda run2.yoda run3.yoda`

### Make a merged yoda for the post hadron yoda files
`cd COMPLETE_YODAS/PREHADRON`
`yodamerge_tmp.py -o posthadron_merged.yoda post*`

### Make a merged yoda for the pre hadron yoda files
`cd COMPLETE_YODAS/POSTHADRON`
`yodamerge_tmp.py -o prehadron_merged.yoda pre*`
---------

compare histos
`rivet-cmphistos posthadron_merged.yoda:'Title=PS+MPI+HAD' prehadron_merged.yoda:'Title=PS'`
-------
`make-plots --png *.dat`
