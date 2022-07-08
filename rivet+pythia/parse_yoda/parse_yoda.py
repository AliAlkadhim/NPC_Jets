import matplotlib.pyplot as plt
import matplotlib

import mplhep as hep
hep.style.use("CMS") 

matplotlib.rcParams.update({
    "text.usetex": True})
import numpy as np
import pandas as pd

#MAPPING DICTIONARY BETWEEN The histo name and the rapidity bin ranges


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
                                'n_bins': 15,
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
                                'n_bins': 15,
                                'ylabel': 'AK7 $1.5<|y|<2.0$'}


}

AK4_NAMES=[    
'd01-x01-y01', #0<y < 0.5
 'd02-x01-y01' , 
  'd03-x01-y01', 
   'd04-x01-y01']

begin_hist_string = 'BEGIN YODA_HISTO1D_V2 /CMS_2021_I1972986/' #not the RAW/... because the RAW has no sacaling
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
                begin_table_ind = line_ind+13
                for i in range(n_bins):
                
                    bin_val = f_readlines[begin_table_ind].split()[0]
                    entry_val = f_readlines[begin_table_ind].split()[6]
                    bins_list.append(bin_val)
                    entries_list.append(entry_val)
                    begin_table_ind +=1

                    
    
    return np.array(bins_list, dtype='float64'), np.array( entries_list, dtype='float64') + 1.e-9 









if __name__ == '__main__':
    post_filename = 'merged_posthadron_500M_supp250.yoda'
    # post_filename='../plots/suppr800_bornktmin600_100M/suppr800_bornktmin600_100M_posthadron_merged.yoda'
    pre_filename = 'merged_prehadron_500M_supp250.yoda'
    # pre_filename='../plots/suppr800_bornktmin600_100M/suppr800_bornktmin600_100M_prehadron_merged.yoda'
    # For some reason for loop doesn't work with plt.step()
    #SINGLE TEST
    # pre_bins_list, pre_entries_list= get_bin_entries_list(pre_filename,AK4_NAMES[0], MAP_DICT[AK4_NAMES[0]]['n_bins'])
    # post_bins_list, post_entries_list= get_bin_entries_list(post_filename,AK4_NAMES[0],MAP_DICT[AK4_NAMES[0]]['n_bins'])

    # NPC = post_entries_list/pre_entries_list

    # plt.step(pre_bins_list, NPC, label=AK4_LABELS[0], where='mid')
    # plt.step(pre_bins_list, NPC, label=AK4_LABELS[0], where='mid')


    # plt.legend()
    # plt.title('AK4')
    # plt.show()




    plt.figure() 

    for hist_ind, hist in enumerate(MAP_DICT.keys()):
        pre_bins_list, pre_entries_list= get_bin_entries_list(pre_filename,hist, MAP_DICT[hist]['n_bins'])
        post_bins_list, post_entries_list= get_bin_entries_list(post_filename,hist, MAP_DICT[hist]['n_bins'])

        NPC = post_entries_list/pre_entries_list
        
        plt.step(pre_bins_list, NPC, label=MAP_DICT[hist]['ylabel'], where='mid')
        plt.ylim(-0.5,1.2)
        plt.xlabel('$p_T$')
        plt.ylabel('NP C')
        plt.legend()
        plt.title('bornkt min 10, born suppression factor 800',fontsize=15)
       
    plt.savefig('../plots/500M_supp250/allbins_suppr250_bornktmin10_500M.png')
    plt.show()


