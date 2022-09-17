import matplotlib.pyplot as plt
import matplotlib
import argparse
import pprint

# see https://stackoverflow.com/questions/45154291/numpy-histogram-retrieve-sum-of-weights-squared-in-each-bin
#SEE https://ipnp.cz/scheirich/?page_id=292
#SEE https://www.desy.de/~flucke/rootdoc/src/GFHistManip.cxx.html
#SEE https://cholmcc.gitlab.io/nbi-python/statistics/Statistik_en.pdf

matplotlib.rcParams.update({
    "text.usetex": True,
    "font.size":15})
import numpy as np
import pandas as pd
import mplhep as hep
hep.style.use("CMS") 

#MAPPING DICTIONARY BETWEEN The histo name and the rapidity bin ranges

parser=argparse.ArgumentParser(description='directory')
parser.add_argument('--D', required=True)

args = parser.parse_args()
# SLICE=args.slice

RANGE=(0.9,1.15)
#ASSUMING EVERYTHING is in /RAW/CMS_2021_I1972986/  , for example /RAW/CMS_2021_I1972986/d23-x01-y01
# TUNE='CUETP8M1-NNPDF2.3LO'
TUNE='Monash2013'



MAP_DICT_AK4 = { 
    #AK4 JETS
    'd01-x01-y01' : {'y_range':(0,0.5), 
                                'n_bins': 22,
                                'ylabel':'AK4 $0<|y|<0.5$',
                                'color':'tab:orange'},

 'd02-x01-y01' :  {'y_range':(0.5,1), 
                                'n_bins': 21,
                                'ylabel':'AK4 $0.5<|y|<1.0$',
                                'color':'navy'},

  'd03-x01-y01':  {'y_range':(1,1.5), 
                                'n_bins': 19,
                                'ylabel': 'AK4 $1.0<|y|<1.5$',
                                'color':'tab:green'},

   'd04-x01-y01': {'y_range':(1.5,2), 
                                'n_bins': 16, #15 for ordinary, 16 for RAW
                                'ylabel': 'AK4 $1.5<|y|<2.0$',
                                'color':'tab:red'}
}



MAP_DICT_AK7 = {

   #AK 7
    'd21-x01-y01': {'y_range':(0,0.5), 
                                'n_bins': 22,
                                'ylabel':'AK7 $0<|y|<0.5$',
                                'color':'tab:orange'},
    
    'd22-x01-y01': {'y_range':(0.5,1), 
                                'n_bins': 21,
                                'ylabel':'AK7 $0.5<|y|<1.0$',
                                'color':'navy'},

    'd23-x01-y01': {'y_range':(1,1.5), 
                                'n_bins': 19,
                                'ylabel': 'AK7 $1.0<|y|<1.5$',
                                'color':'tab:green'},

    'd24-x01-y01': {'y_range':(1.5,2), 
                                'n_bins': 16, #15 for ordinary, 16 for RAW
                                'ylabel': 'AK7 $1.5<|y|<2.0$',
                                'color':'tab:red'}


}

MAP_DICT = { 
    #AK4 JETS
    'd01-x01-y01' : {'y_range':(0,0.5), 
                                'n_bins': 22,
                                'ylabel':'AK4 $0<|y|<0.5$'},

 'd02-x01-y01' :  {'y_range':(0.5,1), 
                                'n_bins': 21,
                                'ylabel':'AK4 $0.5<|y|<1.0$'},

  'd03-x01-y01':  {'y_range':(1,1.5), 
                                'n_bins': 19,
                                'ylabel': 'AK4 $1.0<|y|<1.5$'},

   'd04-x01-y01': {'y_range':(1.5,2), 
                                'n_bins': 16, #15 for ordinary, 16 for RAW
                                'ylabel': 'AK4 $1.5<|y|<2.0$'},
   #AK 7
    'd21-x01-y01': {'y_range':(0,0.5), 
                                'n_bins': 22,
                                'ylabel':'AK7 $0<|y|<0.5$'},
    
    'd22-x01-y01': {'y_range':(0.5,1), 
                                'n_bins': 21,
                                'ylabel':'AK7 $0.5<|y|<1.0$'},

    'd23-x01-y01': {'y_range':(1,1.5), 
                                'n_bins': 19,
                                'ylabel': 'AK7 $1.0<|y|<1.5$'},

    'd24-x01-y01': {'y_range':(1.5,2), 
                                'n_bins': 16, #15 for ordinary, 16 for RAW
                                'ylabel': 'AK7 $1.5<|y|<2.0$'}
}
begin_file_string = 'CMS_2021_I1972986_'


if args.D=="suppr800_bornktmin300_100M":
    post_filename='/home/ali/Desktop/Pulled_Github_Repositories/NPCorrection_InclusiveJets/rivet+pythia/plots/suppr800_bornktmin300_100M/suppr800_bornktmin300_100M_posthadron_merged.yoda'
    pre_filename='/home/ali/Desktop/Pulled_Github_Repositories/NPCorrection_InclusiveJets/rivet+pythia/plots/suppr800_bornktmin300_100M/suppr800_bornktmin300_100M_prehadron_merged.yoda'
    
def get_bin_entries_list(filename, hist_name, n_bins):
    # line_counter=0
    with open(filename, 'r') as f:
        bins_list = []
        entries_list = []
        f_readlines=f.readlines()
        for line_ind, line in enumerate(f_readlines):
            # line_counter +=1 
            if begin_hist_string+ hist_name in line:
                begin_hist_ind = line_ind
                begin_table_ind = line_ind+13 #+13 for ordinary, +12 for RAW
                # begin_table_ind = line_ind+12
                for i in range(n_bins):
                
                    bin_val = f_readlines[begin_table_ind].split()[0]
                    entry_val = f_readlines[begin_table_ind].split()[4]
                    bins_list.append(bin_val)
                    entries_list.append(entry_val)
                    begin_table_ind +=1
        return np.array(bins_list, dtype='float64'), np.array( entries_list, dtype='float64') + 1.e-9 
