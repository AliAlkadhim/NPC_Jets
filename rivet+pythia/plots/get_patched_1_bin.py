'''The purpose of this file
'''
import matplotlib.pyplot as plt
import matplotlib
import argparse



# matplotlib.rcParams.update({
#     "text.usetex": True})
import numpy as np
import pandas as pd
import mplhep as hep
hep.style.use("CMS") 

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

'''For the weughted average method to work, the uncertainties or standard deviations on the ratios
have to be reasonable.
bornsuppfactor bornktmin
160 5 : NR
250 10: R (R in some, NR in some of the range)
400 15: NR
800 30: R (R in some, NR in some) MOSTLY NR
800 300: R
800 600: R
1,800 75: R
3,200 150: R
5,300 250: NR
9,000 750: NR
11,000 1,250: R
'''

#Reasonable pt slices composed of pairs of (bornsuppfactor, bornktmin)
slices=[(250, 10), (800,300),(800,600),(1800,75),(3200,150),(11000,1250)]
 #FIRST RAPIDITY BIN IS 'd01-x01-y01'
SLICES = {
    1:{'pairs':(250, 10),
                        'dir':'suppr250_bornktmin10_1B_ParsiParams',
                        'begin_pre_hist_string' :'BEGIN HISTO1D /suppr250_bornktmin10_1B_ParsiParams_prehadron_merged.yoda/CMS_2021_I1972986',
                        'begin_post_hist_string' :'BEGIN HISTO1D /suppr250_bornktmin10_1B_ParsiParams_posthadron_merged.yoda/CMS_2021_I1972986'

},
#WITH PARIS PARAMS, WITH MSTP
# 2:{'pairs':(800,600),
#                         'dir':'suppr800_bornktmin600_1B_ParisParams_MSTP',
#                         'begin_pre_hist_string' :'BEGIN HISTO1D /suppr800_bornktmin600_1B_ParisParams_MSTP_prehadron_merged.yoda/CMS_2021_I1972986/',
#                         'begin_post_hist_string' :'BEGIN HISTO1D /suppr800_bornktmin600_1B_ParisParams_MSTP_posthadron_merged.yoda/CMS_2021_I1972986/'
# },

#NO PARIS PARAMS AND NO MSTP
# 2:{'pairs':(800,600),
#                         'dir':'suppr800_bornktmin600_100M',
#                         'begin_pre_hist_string' :'BEGIN HISTO1D /suppr800_bornktmin600_100M_prehadron_merged.yoda/CMS_2021_I1972986/',
#                         'begin_post_hist_string' :'BEGIN HISTO1D /suppr800_bornktmin600_100M_posthadron_merged.yoda/CMS_2021_I1972986'

# },

#PARIS PARAMS WITHOUT MSTP
2:{'pairs':(800,600),
                        'dir':'suppr800_bornktmin600_100M_ParisParams',
                        'begin_pre_hist_string' :'BEGIN HISTO1D /suppr800_bornktmin600_100M_ParisParams_prehadron_merged.yoda/CMS_2021_I1972986/',
                        'begin_post_hist_string' :'BEGIN HISTO1D /suppr800_bornktmin600_100M_ParisParams_posthadron_merged.yoda/CMS_2021_I1972986'

},

3:{'pairs':(1800,75),
                        'dir':'suppr11000_bornktmin1250_1B_ParsiParams_MSTP',
                        'begin_pre_hist_string' :'BEGIN HISTO1D /suppr11000_bornktmin1250_1B_ParsiParams_MSTP_prehadron_merged.yoda/CMS_2021_I1972986',
                        'begin_post_hist_string' :'BEGIN HISTO1D /suppr11000_bornktmin1250_1B_ParsiParams_MSTP_posthadron_merged.yoda/CMS_2021_I1972986'


# 3:{'pairs':(1800,75),
#                         'dir':'suppr1800_bornktmin75_1B_ParsiParams_MSTP',
#                         'begin_pre_hist_string' :'BEGIN HISTO1D /suppr1800_bornktmin75_1B_ParsiParams_MSTP_prehadron_merged.yoda/CMS_2021_I1972986',
#                         'begin_post_hist_string' :'BEGIN HISTO1D /suppr1800_bornktmin75_1B_ParsiParams_MSTP_posthadron_merged.yoda/CMS_2021_I1972986'

},
4:{'pairs':(11000,1250),
                        'dir':'suppr11000_bornktmin1250_1B_ParsiParams_MSTP',
                        'begin_pre_hist_string' :'BEGIN HISTO1D /suppr11000_bornktmin1250_1B_ParsiParams_MSTP_prehadron_merged.yoda/CMS_2021_I1972986',
                        'begin_post_hist_string' :'BEGIN HISTO1D /suppr11000_bornktmin1250_1B_ParsiParams_MSTP_posthadron_merged.yoda/CMS_2021_I1972986'

},

5:{'pairs':(800,300),
                        'dir':'suppr800_bornktmin300_100M_ParisParams',
                        'begin_pre_hist_string' :'BEGIN HISTO1D /suppr800_bornktmin300_100M_ParisParams_prehadron_merged.yoda/CMS_2021_I1972986',
                        'begin_post_hist_string' :'BEGIN HISTO1D /suppr800_bornktmin300_100M_ParisParams_posthadron_merged.yoda/CMS_2021_I1972986'

}

}
AK='4'
IMG_TITLE='2_4_AK'+AK+'_100M_Monash2013_WitharisParams_WithoutMSTP'
FIG_TITLE='Pythia Monash 2013 (Default), 100M Events in Slice (800,600), 1B Events in Slice (11000,1250); With ParisParams, Without MSTP'

begin_file_string = 'CMS_2021_I1972986_'


def return_bins_pre_post(rapidity_bin, slice):
    file_string = SLICES[slice]['dir'] + '/' + begin_file_string+ rapidity_bin +'.dat'
    print('FILE ', file_string)
    n_bins=MAP_DICT[rapidity_bin]['n_bins']
    with open(file_string, 'r') as f:
        # print(f.read())
        file_content = f.read()
        s='ErrorBars=1'#count the number of times this string is in the file, which is written when you do --mc-errs in rivet

        number_of_s = file_content.count(s)
        # print(number_of_s)
        if number_of_s==3:
            line_add_num=8
        else:
            line_add_num=7
        f.seek(0)
        f_readlines=f.readlines()
        bins_list=[]
        bins_high_list=[]
        pre_entries_list=[]
        post_entries_list = []
        pre_errors_list = []
        post_errors_list=[]
        



        #Errors are calculated with propagation of errors
        # Delta (post/pre) = |post/pre| sqrt{([Delta post]/post)^2 + ([Delta pre]/pre)^2 }
        #where delta is the uncertainties (errors)
        # print('SLICES', SLICES[1]['begin_pre_hist_string'])
        for line_ind, line in enumerate(f_readlines):
            if str(SLICES[slice]['begin_pre_hist_string']) in line:
                begin_pre_hist_ind = line_ind
                # +8 if --mc-errs, +7 if no -mc-errs
                begin_pre_table_ind = line_ind + line_add_num
                
                for i in range(n_bins):
                    # print( f_readlines[begin_pre_table_ind])
                    bin_val = f_readlines[begin_pre_table_ind].split()[0]
                    bins_list.append(bin_val)
                    bins_high_list.append(f_readlines[begin_pre_table_ind].split()[1])
                    pre_entries_val =  f_readlines[begin_pre_table_ind].split()[2]
                    pre_entries_list.append(pre_entries_val)
                    pre_error =  f_readlines[begin_pre_table_ind].split()[3]
                    pre_errors_list.append(float(pre_error))
                    begin_pre_table_ind +=1 
            #POST
            if str(SLICES[slice]['begin_post_hist_string']) in line:
                begin_post_hist_ind = line_ind
                begin_post_table_ind = line_ind + line_add_num
                for i in range(n_bins):
                    #bins already fetcheds
                    post_entries_val =  f_readlines[begin_post_table_ind].split()[2]
                    post_entries_list.append(post_entries_val)
                    post_error =  f_readlines[begin_post_table_ind].split()[3]
                
                    post_errors_list.append(float(post_error))
                    begin_post_table_ind +=1 
    bins, bins_high, pre, post = np.array(bins_list, dtype=float),   np.array(bins_high_list, dtype=float), np.array(pre_entries_list, dtype=float) ,  np.array(post_entries_list, dtype=float) 
    pre_errors = np.array(pre_errors_list,dtype=float)+ 1.e-20
    post_errors = np.array(post_errors_list,dtype=float)+ 1.e-20
    ratio = np.array(post/pre, dtype=float)
    factor_4 = np.abs(np.divide(post,pre))
    error_ratio = factor_4 * np.sqrt((post_errors/post)**2 + (pre_errors/pre)**2)

    # print('ratio = ', ratio)
    # print('error on ratio = ', error_ratio)
    print('BINS LOW', bins)
    print()
    print('PRE', pre)
    print('POST', post)
    
    return bins, bins_high, pre, post

return_bins_pre_post('d01-x01-y01', 2)