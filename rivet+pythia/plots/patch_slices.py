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

def divide_lists(l1,l2):
    ratio=[]
    for i,j in zip(l1,l2):
        d = (float(i)+1.e-20)/(float(j)+1.e-20)
        ratio.append(d)
    return np.array(ratio)


begin_file_string = 'CMS_2021_I1972986_'

# file = begin_file_string + rapidity_bin

def return_bins_pre_post(rapidity_bin, slice):
    file_string = SLICES[slice]['dir'] + '/' + begin_file_string+ rapidity_bin +'.dat'
    print('FILE ', file_string)
    n_bins=MAP_DICT[rapidity_bin]['n_bins']
    with open(file_string, 'r') as f:
        # print(f.read())
        file_content = f.read()
        s='ErrorBars=1'#count the number of times this string is in the file, which is written when you do --mc-errs in rivet

        number_of_s = file_content.count(s)
        print(number_of_s)
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
                    print( f_readlines[begin_pre_table_ind])
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
    bins, bins_high, pre, post = np.array(bins_list, dtype=float),   np.array(bins_high_list, dtype=float), np.array(pre_entries_list, dtype=float) + 1.e-20 ,  np.array(post_entries_list, dtype=float) + 1.e-20
    pre_errors = np.array(pre_errors_list,dtype=float)+ 1.e-20
    post_errors = np.array(post_errors_list,dtype=float)+ 1.e-20
    ratio = np.array(post/pre, dtype=float)
    factor_4 = np.abs(np.divide(post,pre))
    error_ratio = factor_4 * np.sqrt((post_errors/post)**2 + (pre_errors/pre)**2)

    print('ratio = ', ratio)
    print('error on ratio = ', error_ratio)
    return bins, bins_high, ratio, error_ratio









#WORKFLOW FOR 1 BIN

# jet_pt=[  97, 133,  174,  220,  272,  330,  395,  468,  548,  638,  737,  846, 967, 1101, 1248, 1410, 1588, 1784, 2000, 2238, 2500, 2787, 3103] # is the same as bins_1=bins_2=.... but with xhigh too
# jet_pt_centers=(np.array(jet_pt)[1:]+np.array(jet_pt)[:-1])/2
# jet_pt_centers = [ 115,   153.5,  197,   246,   301,   362.5,  431.5,  508,   593,   687.5, 791.5,  906.5, 1034,  1174.5, 1329,  1499,  1686,  1892,  2119,  2369, 2643.5, 2945 ]
# print(len(jet_pt_centers))
# print('jet pt centers', jet_pt_centers)

cutoff1=1174.5

def get_patched_corrections(rapidity_bin):
    """Get the patched NP corrections, currently using:
    Jet pt 0-1101 : ratio_2 (which uses (bornsuppfactor, bornktmin) = (800,600) )
    Jet pt 1101 - 2787 : ratio_4 (which uses (bornsuppfactor, bornktmin) = (11000,1250) )
    
    """
    bins_1, bins_high_1, ratio_1, error_ratio_1 = return_bins_pre_post(rapidity_bin, 1)
    bins_2, bins_high_2, ratio_2, error_ratio_2 = return_bins_pre_post(rapidity_bin, 2)
    bins_3, bins_high_3, ratio_3, error_ratio_3 = return_bins_pre_post(rapidity_bin, 3)
    bins_4, bins_high_4, ratio_4, error_ratio_4 = return_bins_pre_post(rapidity_bin, 4)
    bins_5, bins_high_5, ratio_5, error_ratio_5 = return_bins_pre_post(rapidity_bin, 5)

    #Get the bins and then bin centers (pt) of each rapidity file
    # print('BINS HIGH', bins_high_1[-1])
    jet_pt=list(bins_1)
    jet_pt.append(bins_high_1[-1])
    print('JET PT= ', jet_pt)
    jet_pt_centers=(np.array(jet_pt)[1:]+np.array(jet_pt)[:-1])/2

    patched_ratio=np.empty(len(jet_pt_centers))
    
    index_1101 = list(jet_pt_centers).index(cutoff1)
    # patched_ratio[0:index_1101]=ratio_2[0:index_1101]
    patched_ratio[0:index_1101]=ratio_2[0:index_1101]


    patched_ratio[index_1101:]=ratio_4[index_1101:]
    

    patched_ratio_error=np.empty(len(jet_pt_centers))
    
    # patched_ratio_error[0:index_1101]=error_ratio_2[0:index_1101]
    patched_ratio_error[0:index_1101]=error_ratio_2[0:index_1101]

    patched_ratio_error[index_1101:]=error_ratio_4[index_1101:]


    patched_ratio_relative_unc = np.array(patched_ratio_error)/np.array(patched_ratio)
    return jet_pt_centers, patched_ratio, patched_ratio_error, patched_ratio_relative_unc    





# patched_ratio, patched_ratio_error, patched_ratio_relative_unc = get_patched_corrections(rapidity_bin =  'd01-x01-y01')
nrows, ncols = 4, 2
fig, axs = plt.subplots(nrows, ncols,figsize=(15,15))
fig.suptitle(FIG_TITLE,fontsize=20)

if AK=='4':
    ADK_DICT=MAP_DICT_AK4
elif AK=='7':
    ADK_DICT=MAP_DICT_AK7

for rapidity_bin_i, rapidity_bin in enumerate(ADK_DICT.keys()):
    print(rapidity_bin)

    jet_pt_centers, patched_ratio, patched_ratio_error, patched_ratio_relative_unc = get_patched_corrections(rapidity_bin)


    
    # axs=axs.flatten()
    axs[rapidity_bin_i,0].scatter(jet_pt_centers, patched_ratio, label=ADK_DICT[rapidity_bin]['ylabel'], color=ADK_DICT[rapidity_bin]['color'] )
    axs[rapidity_bin_i,0].errorbar(jet_pt_centers, patched_ratio, yerr= patched_ratio_relative_unc,fmt='none', c='black', linewidth=2, capsize=2)

    axs[rapidity_bin_i,0].set_ylim((0.9,1.1))
    axs[rapidity_bin_i, 0].set_ylabel('Patched NPC',fontsize=16)
    axs[rapidity_bin_i, 0].text(x=cutoff1-600, y=0.95, s=r'$(800,600)$',size=12,color ='r')
    axs[rapidity_bin_i, 0].text(x=cutoff1+100, y=0.95, s=r'$(11000,1250)$',size=12,color='r')
    
    axs[rapidity_bin_i, 1].scatter(jet_pt_centers, patched_ratio_relative_unc, label=ADK_DICT[rapidity_bin]['ylabel'],  color=ADK_DICT[rapidity_bin]['color'])
    axs[rapidity_bin_i,1].set_ylim((0,patched_ratio_relative_unc.max()+0.01))
    axs[rapidity_bin_i, 1].set_ylabel(r'$\Delta_{rel}$ Patched NPC',fontsize=15)
    axs[rapidity_bin_i, 1].text(x=cutoff1-600, y=0.004, s=r'$(800,600)$',size=12,color='r')
    axs[rapidity_bin_i, 1].text(x=cutoff1+100, y=0.004, s=r'$(11000,1250)$',size=12,color='r')
    for i in range(nrows):
        # axs[i].legend(loc='best')
        for j in range(ncols):
            axs[i, j].set_xlabel(r'Jet $p_T$ [GeV]', fontsize=18)
            axs[i,j].axvline(x=cutoff1, color='r')
            axs[i,j].axhline(y=1, color='black', linestyle='--')
            axs[i,j].legend( loc='upper right', fontsize=15)


plt.tight_layout(pad=2.0)

plt.savefig('patched/'+IMG_TITLE+'.png')

plt.show()