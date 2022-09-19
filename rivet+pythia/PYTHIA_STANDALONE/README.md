To start a new pythia standalone analysis, simply do

`python makeanalysis.py --runname <runname> --condor False`

and a new <runname> is generated with all the necessary files and configurations for your run. You can go into the directory for more detailed configurations (and run condor from there), or you can use `--condor True` to have a condor job for this run be submitted automatically.


