import matplotlib.pyplot as plt
import matplotlib
import argparse

import mplhep as hep
hep.style.use("CMS") 

matplotlib.rcParams.update({
    "text.usetex": True})
import numpy as np
import pandas as pd

#MAPPING DICTIONARY BETWEEN The histo name and the rapidity bin ranges

parser=argparse.ArgumentParser(description='directory')
parser.add_argument('--D', required=True)
args = parser.parse_args()

#ASSUMING EVERYTHING is in /RAW/CMS_2021_I1972986/  , for example /RAW/CMS_2021_I1972986/d23-x01-y01

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
# 300 AND 600 BORNKTMIN WITH 800 SUPPR
# begin_post_hist_string ='BEGIN HISTO1D /suppr800_bornktmin600_100M_posthadron_merged.yoda/CMS_2021_I1972986/'
# begin_pre_hist_string ='BEGIN HISTO1D /suppr800_bornktmin600_100M_prehadron_merged.yoda/CMS_2021_I1972986/'

# LOW PT
# begin_post_hist_string ='BEGIN HISTO1D /merged_posthadron_500M_supp250.yoda/CMS_2021_I1972986/'
# begin_pre_hist_string ='BEGIN HISTO1D /merged_prehadron_500M_supp250.yoda/CMS_2021_I1972986/'


# 0 SUPP FACT
begin_post_hist_string ='BEGIN HISTO1D /suppr_0_500M_posthadron_merged.yoda/CMS_2021_I1972986/'
begin_pre_hist_string ='BEGIN HISTO1D /suppr_0_500M_prehadron_merged.yoda/CMS_2021_I1972986/'



def return_bins_pre_post(one_hist):
    file_string = args.D + '/' + begin_file_string+ one_hist +'.dat'
    n_bins=MAP_DICT[one_hist]['n_bins']
    with open(file_string, 'r') as f:
        bins_list=[]
        pre_entries_list=[]
        post_entries_list = []
        f_readlines=f.readlines()
        for line_ind, line in enumerate(f_readlines):
            
            if begin_pre_hist_string in line:
                begin_pre_hist_ind = line_ind
                begin_pre_table_ind = line_ind + 8
                
                for i in range(n_bins):
                    bin_val = f_readlines[begin_pre_table_ind].split()[0]
                    bins_list.append(bin_val)
                    pre_entries_val =  f_readlines[begin_pre_table_ind].split()[2]
                    pre_entries_list.append(pre_entries_val)
                    begin_pre_table_ind +=1 

            if begin_post_hist_string in line:
                begin_post_hist_ind = line_ind
                begin_post_table_ind = line_ind + 8
                for i in range(n_bins):
                    post_entries_val =  f_readlines[begin_post_table_ind].split()[2]
                    post_entries_list.append(post_entries_val)
                    begin_post_table_ind +=1 
            
    return np.array(bins_list, dtype='float64'),  np.array(pre_entries_list, dtype='float64') + 1.e-9 ,  np.array(post_entries_list, dtype='float64')



for hist_ind, hist in enumerate(MAP_DICT.keys()):

    bins, pre, post = return_bins_pre_post(hist)
    NPC = post/pre
    plt.step(bins, NPC, label=MAP_DICT[hist]['ylabel'], where='mid')
    plt.xlabel('$p_T$ [GeV]')
    plt.ylabel(r'$\frac{\sigma^{PS+MPI+HAD}}{\sigma^{PS}}$')
    plt.title('bornktmin 10, bornsuppfact 0',font='MonoSpace')
    plt.ylim(-0.5,3)
    plt.legend()
    plt.savefig(args.D+'/ALLBINS_'+args.D+'.png')

plt.show()