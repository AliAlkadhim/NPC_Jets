import matplotlib.pyplot as plt
import matplotlib
import argparse


matplotlib.rcParams.update({
    "text.usetex": True})
import numpy as np
import pandas as pd
import mplhep as hep
hep.style.use("CMS") 


# parser=argparse.ArgumentParser(description='directory')
# args = parser.parse_args()

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




def return_bins_pre_post(dir, one_hist):
    if dir == 'suppr250_bornktmin10_100M_ParsiParams':
         begin_post_hist_string ='BEGIN HISTO1D /suppr250_bornktmin10_100M_ParsiParams_posthadron_merged.yoda/CMS_2021_I1972986/'
         begin_pre_hist_string ='BEGIN HISTO1D /suppr250_bornktmin10_100M_ParsiParams_prehadron_merged.yoda/CMS_2021_I1972986/'
         pt_range='low'
    elif dir =='suppr800_bornktmin300_100M_ParisParams':
        begin_post_hist_string ='BEGIN HISTO1D /suppr800_bornktmin300_100M_ParisParams_posthadron_merged.yoda/CMS_2021_I1972986/'
        begin_pre_hist_string ='BEGIN HISTO1D /suppr800_bornktmin300_100M_ParisParams_prehadron_merged.yoda/CMS_2021_I1972986/'
        pt_range='low'

    file_string = dir + '/' + begin_file_string+ one_hist +'.dat'
    n_bins=MAP_DICT[one_hist]['n_bins']
    with open(file_string, 'r') as f:
        bins_list=[]
        pre_entries_list=[]
        post_entries_list = []
        pre_errors_list = []
        post_errors_list=[]
        #Errors are calculated with propagation of errors
        # Delta (post/pre) = |post/pre| sqrt{([Delta post]/post)^2 + ([Delta pre]/pre)^2 }
        #where delta is the uncertainties (errors)
        f_readlines=f.readlines()
        for line_ind, line in enumerate(f_readlines):
            
            #PRE
            if begin_pre_hist_string in line:
                begin_pre_hist_ind = line_ind
                begin_pre_table_ind = line_ind + 7
                
                for i in range(n_bins):
                    bin_val = f_readlines[begin_pre_table_ind].split()[0]
                    bins_list.append(bin_val)
                    pre_entries_val =  f_readlines[begin_pre_table_ind].split()[2]
                    pre_entries_list.append(pre_entries_val)
                    pre_error =  f_readlines[begin_pre_table_ind].split()[3]
                    pre_errors_list.append(pre_error)
                    begin_pre_table_ind +=1 
            #POST
            if begin_post_hist_string in line:
                begin_post_hist_ind = line_ind
                begin_post_table_ind = line_ind + 7
                for i in range(n_bins):
                    #bins already fetcheds
                    post_entries_val =  f_readlines[begin_post_table_ind].split()[2]
                    post_entries_list.append(post_entries_val)
                    post_error =  f_readlines[begin_post_table_ind].split()[3]
                    post_errors_list.append(post_error)
                    begin_post_table_ind +=1 
    bins, pre, post = np.array(bins_list, dtype='float64'),  np.array(pre_entries_list, dtype='float64') + 1.e-20 ,  np.array(post_entries_list, dtype='float64') + 1.e-20
    pre_errors = np.array(pre_errors_list, dtype='float64') + 1.e-20
    post_errors = np.array(post_errors_list, dtype='float64') + 1.e-20 
    # print('BINS', bins)
    # print('PRE', pre)
    # print('POST', post)
    # print('PRE ERRORS', pre_errors)
    return bins, pre, post, pre_errors, post_errors


# dir = 'suppr250_bornktmin10_100M_ParsiParams_MSTP'
# pt_range='low'
# bins, pre, post, pre_errors, post_errors =  return_bins_pre_post(dir, list(MAP_DICT_AK7)[0])

# plt.step(bins, post, label=MAP_DICT_AK7[list(MAP_DICT_AK7)[0]]['ylabel'] + pt_range +'  $p_T$')

# dir = 'suppr800_bornktmin300_100M_ParisParams'
# pt_range='medium'
# bins, pre, post, pre_errors, post_errors =  return_bins_pre_post(dir, list(MAP_DICT_AK7)[0])

# plt.step(bins, post, label=MAP_DICT_AK7[list(MAP_DICT_AK7)[0]]['ylabel'] + pt_range +'  $p_T$')

dir_list=[ 'suppr250_bornktmin10_100M_ParsiParams',  'suppr800_bornktmin300_100M_ParisParams']
# for i in dir_list:
bins, pre, post, pre_errors, post_errors =  return_bins_pre_post(dir_list[0], list(MAP_DICT_AK7)[0])
plt.step(bins, post, label=MAP_DICT_AK7[list(MAP_DICT_AK7)[0]]['ylabel'] +'  $p_T$')

bins, pre, post, pre_errors, post_errors =  return_bins_pre_post(dir_list[1], list(MAP_DICT_AK7)[0])
plt.step(bins, post, label=MAP_DICT_AK7[list(MAP_DICT_AK7)[0]]['ylabel'] +'  $p_T$')


plt.legend()
plt.show()
