FIFO - first in, first out

Do `rivet --help` and `agile-runmc --help` to test that you have ruvet working.
With `pwgevents.lhe` in directory.

```
#!/bin/bash
./main42 main42_prehadron.cmnd prehadron.fifo &
rivet --ignore-beams -o prehadron.yoda -a CMS_2016_I1487277 -a MC_JETS prehadron.fifo
```




------

use pythia to generate hepmc events going to the fifo

`./main42 main42.cmnd tut_fifo.fifo &` where I have pwgevents.lhe and main42 files in that directory

Now attach Rivet to the other end of the pipe:

`rivet -a MC_GENERIC -a MC_JETS tut_fifo.fifo`


The CMS QCD incl.jet rivet analysis is `CMS_2016_I1487277` For example, `rivet -a MC_JETS,CMS_2016_I1487277 --ignore-beams retest_pre_hadron.hepmc`



-----------

### Rivet/pythia for one `.lhe` file.

Example: currentlt working in /afs/desy.de/user/a/aalkadhi/poweheg/parallel_Dijets/run_nominal/rivet_pythia , where here I have
`main42  main42.cmnd  minnlo_0001.yoda  out  pwgevents.lhe  rivet_fifo_onefile.sh`

**rivet_fifo_onefile.sh**

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










## Questions for Valentina: So what is the workflow like for one file?

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
