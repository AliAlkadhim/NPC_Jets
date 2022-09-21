import matplotlib.pyplot as plt
import matplotlib
import argparse
import parse_dat as parse


matplotlib.rcParams.update({
    "text.usetex": True})
import numpy as np
# import pandas as pd
import mplhep as hep
hep.style.use("CMS") 

#MAPPING DICTIONARY BETWEEN The histo name and the rapidity bin ranges

parser=argparse.ArgumentParser(description='directory')
parser.add_argument('--D', required=True)
# parser.add_argument('--slice', required=True)

parser.add_argument('--Matrix', type=bool, required=False, default=False, help='if True, generate a matrix of the NPC in the (x,y)=(hadron,parton) space')
args = parser.parse_args()
# SLICE=args.slice

RANGE=(0.9,1.15)
XMAX=967 + 10
#ASSUMING EVERYTHING is in /RAW/CMS_2021_I1972986/  , for example /RAW/CMS_2021_I1972986/d23-x01-y01
# TUNE='CUETP8M1-NNPDF2.3LO'
# TUNE='Monash2013'
TUNE="CUETP8M1-NNPDF2.3LO"



MAP_DICT_AK4 = { 
    #AK4 JETS
    'd01-x01-y01' : {'y_range':(0,0.5), 
                                'n_bins': 22,
                                'ylabel':'AK4 $0<|y|<0.5$',
                                'color':'tab:orange',
                                'xfitter_file':'NP_y0.dat'},

 'd02-x01-y01' :  {'y_range':(0.5,1), 
                                'n_bins': 21,
                                'ylabel':'AK4 $0.5<|y|<1.0$',
                                'color':'navy',
                                'xfitter_file':'NP_y1.dat'},

  'd03-x01-y01':  {'y_range':(1,1.5), 
                                'n_bins': 19,
                                'ylabel': 'AK4 $1.0<|y|<1.5$',
                                'color':'tab:green',
                                'xfitter_file':'NP_y2.dat'},

   'd04-x01-y01': {'y_range':(1.5,2), 
                                'n_bins': 16, #15 for ordinary, 16 for RAW
                                'ylabel': 'AK4 $1.5<|y|<2.0$',
                                'color':'tab:red',
                                'xfitter_file':'NP_y3.dat'}
}


MAP_DICT_AK7 = {

   #AK 7
    'd21-x01-y01': {'y_range':(0,0.5), 
                                'n_bins': 22,
                                'ylabel':'AK7 $0<|y|<0.5$',
                                'color':'tab:orange',
                                'xfitter_file':'NP_y0.dat'},
    
    'd22-x01-y01': {'y_range':(0.5,1), 
                                'n_bins': 21,
                                'ylabel':'AK7 $0.5<|y|<1.0$',
                                'color':'navy',
                                'xfitter_file':'NP_y1.dat'
                                },

    'd23-x01-y01': {'y_range':(1,1.5), 
                                'n_bins': 19,
                                'ylabel': 'AK7 $1.0<|y|<1.5$',
                                'color':'tab:green',
                                 'xfitter_file':'NP_y2.dat'},

    'd24-x01-y01': {'y_range':(1.5,2), 
                                'n_bins': 16, #15 for ordinary, 16 for RAW
                                'ylabel': 'AK7 $1.5<|y|<2.0$',
                                'color':'tab:red',
                                'xfitter_file':'NP_y3.dat'}


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

if args.D=="CUETP8M1-NNPDF2.3LO_HardQCD_1T":
    begin_post_hist_string = 'BEGIN HISTO1D /CUETP8M1-NNPDF2.3LO_HardQCD_1T_posthadron_merged.yoda/CMS_2021_I1972986'
    begin_pre_hist_string = 'BEGIN HISTO1D /CUETP8M1-NNPDF2.3LO_HardQCD_1T_prehadron_merged.yoda/CMS_2021_I1972986'
    
for hist_ind, hist in enumerate(MAP_DICT.keys()):
                bins_4, pre_4, post_4, pre_error_4 , post_error_4 = parse.return_bins_pre_post(hist)
                err_file = np.load(args.D + '/' + hist + '_errors.npy')
                plt.scatter(bins_4, err_file*100, label=MAP_DICT[hist]['ylabel'],linewidth=2,marker='X')
                
                plt.xlabel('$p_T$ [GeV]', fontsize=21)
                plt.ylabel('\% Uncertainty')
                plt.legend(fontsize=13)

plt.savefig(args.D+ '/'+'errs_allbins.png')
plt.show()
