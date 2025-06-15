## Non-perturbative Corrections for the Inclusive jet cross section
A collection of scripts for the derivation and analysis Non-perturbative Corrections for the Inclusive jet cross section, measured at CERN CMS collaboration using Run 2 data.

To see example results, go to `rivet+pythia/plots`. If you want to reproduce or learn more, keep reading


This is meant to be run on `naf`, althought with some modifications it can also be run on `lxplus`. Further, it is highly recommended to be run on `DUST` for higher storage capacity than `afs` (1 TB starting! Do `mydust-quota` to see your available space)

## Complete Automated Analysis for PYTHIA

`cd rive+pythia/PYTHIA_STANDALONE && ls -lt`

`make_pythia_analysis.py` uses the template for one condor run (with `pythia` and `rivet`) in `PYTHIA_STANDALONE/template_run`, with optional argumetents that can be changed in the python script. Use `python make_pythia_analysis --help` for more arguments.

```
cd PYTHIA_STANDALONE
python make_pythia_analysis.py --runname SOME_RUN_NAME
cd SOME_RUN_NAME
condor-submit rivet_condor.sub
```

This too is automated such that you can make many condor runs, each is composed of thousands of jobs. To merge the outputs of this huge meta-run, see `PYTHIA_STANDALONE/merge_huge.sh`  
`merge_huge.sh`



-----------

## POWHEG

Most of my workflow can be replicated from a sample run in the directory `powheg/template_run`.

To make a new run, which is associated with a new directory, do

`mkdir new_example_run`

`cp -r template_run/* new_example_run`

`cd new_example_run`

Then change "suppr800_bornktmin300_100M" with your new run "new_example_run" and do

`bash sed_scripts.sh`

Then change the number of events you want to run in each job in the `powheg.input` (or other powheg parameters). For example, one of the best things to do is 
to run on 100,000 events in each job, and run over 100 jobs with condor, resulting in 100,000,000 events in total.

Then do

`condor_submit improved_condor_submit_Dijets.sub`

Then keep checking your jobs with `condor_q`. This will take a couple of days to produce the 1000 lhe files.

Then do 

`mkdir -p COMPLETE_YODAS/PREHADRON COMPLETE_YODAS/POSTHADRON`

Uncomment the commands for both prehadron and posthadron analyses in the `mkfifo_parallel.sh`, and change the number of events in `main_scripts/main42_prehadron.comnd` and `main_scripts/posthadron.cmnd` to the number of events in each of your `lhe` files.

Then change number of jobes ("Queries") in `rivet_condor.sub` to the number of jobs (directories) that you ran with powheg. Now do

`condor_submit rivet_condor.sub`

After everyhting finishes (this step takes less time than the `lhe` file generation), change the titles of your merged histograms in `merge.sh` and do

`cd COMPLETE_YODAS && bash merge.sh`


Finally, assuming the title of your histograms are `<posthadron_merged.yoda>` and `<prehadron_merged.yoda>`  and do

```
source /afs/desy.de/user/a/aalkadhi/poweheg/rivet+pythia/installnew.sh
cd COMPLETE_YODAS
rivet-cmphistos <posthadron_merged.yoda>:'Title=PS+MPI+HAD' <prehadron_merged.yoda>:'Title=PS`
make-plots --png *.dat
```




### Complete Automated Analysis for POWHEG

It is also possible to use `make_analysys.py` for a completely automated POWHEG+Pythia analysis. This does everythin g necessary for the anlalysis, including the condor submission and checkpointing.
Example usage `python make_anlysis.py --bornsupp 250 --bornktmin 10 --N 1000000000` makes an analysis with $(k_T^{supp},k_T^{min}) = (250,10)$ with $10^9$ events.

Other options such as the pythia tunes and other parameters could be specified and are being automated.


