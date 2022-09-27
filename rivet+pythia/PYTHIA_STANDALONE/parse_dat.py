import matplotlib.pyplot as plt
import matplotlib
import argparse
# import parse_paris_yoda  as Paris
from parse_paris_yoda import MAP_DICT_PARIS_4 

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

RANGE=(0.9,1.3)
XMAX=967 + 10
#ASSUMING EVERYTHING is in /RAW/CMS_2021_I1972986/  , for example /RAW/CMS_2021_I1972986/d23-x01-y01
# TUNE='CUETP8M1-NNPDF2.3LO'
# TUNE='Monash2013'
# TUNE="CUETP8M1-NNPDF2.3LO"
TUNE='CUETP8M'

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
# 300 AND 600 BORNKTMIN WITH 800 SUPPR
# begin_post_hist_string ='BEGIN HISTO1D /suppr800_bornktmin600_100M_posthadron_merged.yoda/CMS_2021_I1972986/'
# begin_pre_hist_string ='BEGIN HISTO1D /suppr800_bornktmin600_100M_prehadron_merged.yoda/CMS_2021_I1972986/'


#THE suppr_0_500M_prehadron_merged.yoda is the .yoda hist name
#do ls directory to see the .yoda hist names


dir_211_10431 = '../../xfitter_datafiles/xfitter-datafiles/lhc/cms/jets/2111.10431/NP/'

def xfitter_NPs(rap_bin):
    file_string = dir_211_10431 + MAP_DICT_AK7[rap_bin]['xfitter_file']
    print(file_string)
    
    n_bins=MAP_DICT_AK7[rap_bin]['n_bins']
    with open(file_string, 'r') as f:
        bins_list=[]
        NPC_list=[]


        fr =f.readlines()
        for line_ind, line in enumerate(fr):
            bins_list.append(float(line.strip().split()[2]))
            NPC_list.append(float(line.strip().split()[-1]))
        
        return np.array(bins_list) , np.array(NPC_list)
            




            
            
if args.D=="suppr800_bornktmin600_1B_ParisParams_MSTP":
    begin_post_hist_string =' BEGIN HISTO1D /suppr800_bornktmin600_1B_ParisParams_MSTP_posthadron_merged.yoda/CMS_2021_I1972986'
    begin_pre_hist_string =' BEGIN HISTO1D /suppr800_bornktmin600_1B_ParisParams_MSTP_prehadron_merged.yoda/CMS_2021_I1972986'

elif args.D=="500M_supp250":#bornktmin0
    begin_post_hist_string ='BEGIN HISTO1D /merged_posthadron_500M_supp250.yoda/CMS_2021_I1972986/'
    begin_pre_hist_string ='BEGIN HISTO1D /merged_prehadron_500M_supp250.yoda/CMS_2021_I1972986/'

elif args.D=="suppr0_bornktmin10_1B":
    begin_post_hist_string = 'BEGIN HISTO1D /suppr0_bornktmin10_1B_posthadron_merged.yoda/CMS_2021_I1972986'
    begin_pre_hist_string = 'BEGIN HISTO1D /suppr0_bornktmin10_1B_prehadron_merged.yoda/CMS_2021_I1972986'
elif args.D=="suppr0_bornktmin20_1B":
    begin_post_hist_string = 'BEGIN HISTO1D /suppr0_bornktmin20_1B_posthadron_merged.yoda/CMS_2021_I1972986'
    begin_pre_hist_string = 'BEGIN HISTO1D /suppr0_bornktmin20_1B_prehadron_merged.yoda/CMS_2021_I1972986'
elif args.D=="Monash_HardQCD_1B":
    begin_post_hist_string = 'BEGIN HISTO1D /Monash_HardQCD_1B_posthadron_merged.yoda/CMS_2021_I1972986'
    begin_pre_hist_string = 'BEGIN HISTO1D /Monash_HardQCD_1B_prehadron_merged.yoda/CMS_2021_I1972986'

elif args.D=="Monash_HardQCD_10k":
    begin_post_hist_string = 'BEGIN HISTO1D /posthadron_10k.yoda/CMS_2021_I1972986'
    begin_pre_hist_string = 'BEGIN HISTO1D /prehadron_10k.yoda/CMS_2021_I1972986'

elif args.D=="Monash_HardQCD_1B/OneRun":
    begin_post_hist_string = 'BEGIN HISTO1D /posthadron601.yoda/CMS_2021_I1972986'
    begin_pre_hist_string = 'BEGIN HISTO1D /prehadron601.yoda/CMS_2021_I1972986'
elif args.D=="Monash_HardQCD_1B/Merged_Rivet":
    begin_post_hist_string = 'BEGIN HISTO1D /Monash_HardQCD_1B_posthadron_merged.yoda/CMS_2021_I1972986'
    begin_pre_hist_string = 'BEGIN HISTO1D /Monash_HardQCD_1B_prehadron_merged.yoda/CMS_2021_I1972986'
elif args.D=="Monash_HardQCD_Random_10M":
    begin_post_hist_string = 'BEGIN HISTO1D /Monash_HardQCD_Random_10M_posthadron_merged.yoda/CMS_2021_I1972986/'
    begin_pre_hist_string = 'BEGIN HISTO1D /Monash_HardQCD_Random_10M_prehadron_merged.yoda/CMS_2021_I1972986/'

elif args.D=="CUETP8M1-NNPDF2.3LO_HardQCD_1B":
    begin_post_hist_string = 'BEGIN HISTO1D /CUETP8M1-NNPDF2.3LO_HardQCD_1Bposthadron_merged.yoda/CMS_2021_I1972986'
    begin_pre_hist_string = 'BEGIN HISTO1D /CUETP8M1-NNPDF2.3LO_HardQCD_1Bprehadron_merged.yoda/CMS_2021_I1972986'
elif args.D=="CUETP8M1-NNPDF2.3LO_HardQCD_10B":
    begin_post_hist_string = 'BEGIN HISTO1D /CUETP8M1-NNPDF2.3LO_HardQCD_10Bposthadron_merged.yoda/CMS_2021_I1972986'
    begin_pre_hist_string = 'BEGIN HISTO1D /CUETP8M1-NNPDF2.3LO_HardQCD_10Bprehadron_merged.yoda/CMS_2021_I1972986'
elif args.D=="CUETP8M1-NNPDF2.3LO_HardQCD_1T":
    begin_post_hist_string = 'BEGIN HISTO1D /CUETP8M1-NNPDF2.3LO_HardQCD_1T_posthadron_merged.yoda/CMS_2021_I1972986'
    begin_pre_hist_string = 'BEGIN HISTO1D /CUETP8M1-NNPDF2.3LO_HardQCD_1T_prehadron_merged.yoda/CMS_2021_I1972986'

elif args.D=="Paris_CUETP8M_10B":
    begin_post_hist_string = 'BEGIN HISTO1D /Paris_CUETP8M_10B_posthadron_merged.yoda/CMS_2021_I1972986'
    begin_pre_hist_string = 'BEGIN HISTO1D /Paris_CUETP8M_10B_prehadron_merged.yoda/CMS_2021_I1972986'
    

def return_bins_pre_post(one_hist):
    file_string = args.D + '/' + begin_file_string+ one_hist +'.dat'
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
        for line_ind, line in enumerate(f_readlines):
            
            #PRE
            if begin_pre_hist_string in line:
                begin_pre_hist_ind = line_ind
                # +8 if --mc-errs, +7 if no -mc-errs
                begin_pre_table_ind = line_ind +line_add_num
                
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
                begin_post_table_ind = line_ind + line_add_num
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



def main():
    if not args.Matrix:
        fig, axs = plt.subplots(nrows=4, ncols=2, figsize=(20,10))
        for hist_ind_4, hist_4 in enumerate(MAP_DICT_AK4.keys()):

            bins_4, pre_4, post_4, pre_error_4 , post_error_4 = return_bins_pre_post(hist_4)
            NPC_4 = post_4/pre_4
            
            print('bins_4 %d' % hist_ind_4, bins_4)
            print('pre_error_4 y bin %d' % hist_ind_4, pre_error_4)
            print('post_error_4 %d' % hist_ind_4, post_error_4)
            print('pre_4', pre_4)
            print('post_4', post_4)
            # Delta (post/pre) = |post/pre| sqrt{([Delta post]/post)^2 + ([Delta pre]/pre)^2 }
            factor_4 = np.abs(np.divide(post_4,pre_4))
            error_NPC_4 = factor_4 * np.sqrt((post_error_4/post_4)**2 + (pre_error_4/pre_4)**2)
            print('error_NPC_4',error_NPC_4)
            np.save(args.D+'/'+hist_4+'_errors.npy',error_NPC_4)

            axs[hist_ind_4,0].step(bins_4, NPC_4, label=MAP_DICT_AK4[hist_4]['ylabel'], where='mid',linewidth=2, color=MAP_DICT_AK4[hist_4]['color'])
            axs[hist_ind_4, 0].errorbar(bins_4, NPC_4, yerr = error_NPC_4, fmt='none', c='black', linewidth=2, capsize=2)
            axs[hist_ind_4, 0].set_xlabel('$p_T$ [GeV]', fontsize=21)
            axs[hist_ind_4,0].set_ylabel(r'$\mathbf{\frac{\sigma_{PS+MPI+HAD}}{\sigma_{PS}}}$', fontsize=22)
            # axs[hist_ind_4,0].set_ylim(-0.1,max(NPC_4)*1.2)
            # axs[hist_ind_4,0].set_ylim(0.85,1.2)

            
            
            axs[hist_ind_4,0].set_ylim(RANGE)
            #STANDARD RANGE (PLOT THIS RANGE FIRST BEFORE CHAGING)
            # axs[hist_ind_4,0].set_xlim(min(bins_4),max(bins_4))
            axs[hist_ind_4,0].set_xlim(min(bins_4),XMAX)
            # axs[hist_ind_4,0].set_xticks(bins_4)
            # axs[hist_ind_4,0].set_xlim(100, 2500)
            axs[hist_ind_4,0].axhline(y=1, color='black', linestyle='--')

            axs[hist_ind_4,0].legend(loc='best',fontsize=19)
            axs[hist_ind_4,0].grid(axis='x')
            axs[hist_ind_4,0].set_yticks([0.9,1.0,1.1])
            
            
        #NOW ITERATE OVER PARIS DICTIONARIES
        for hist_ind, hist in enumerate(Paris.MAP_DICT_PARIS_4.keys()):
            pre_bins_list, pre_entries_list= get_bin_entries_list(Paris.pre_filename,hist, Paris.MAP_DICT_PARIS_4[hist]['n_bins']) 
            
            
        for hist_ind_7, hist_7 in enumerate(MAP_DICT_AK7.keys()):

            bins_7, pre_7, post_7, pre_error_7, post_error_7  = return_bins_pre_post(hist_7)
            NPC_7 = post_7/pre_7
            

            factor_7 = np.abs(np.divide(post_7,pre_7))
            error_NPC_7 = factor_7 * np.sqrt((post_error_7/post_7)**2 + (pre_error_7/pre_7)**2)
            print('error_NPC_7',error_NPC_7)
            np.save(args.D+'/'+hist_7+'_errors.npy',error_NPC_7)

            axs[hist_ind_7,1].step(bins_7, NPC_7, label=MAP_DICT_AK7[hist_7]['ylabel'], where='mid',linewidth=2, color=MAP_DICT_AK7[hist_7]['color'])
            axs[hist_ind_7, 1].errorbar(bins_7, NPC_7, yerr = error_NPC_7, fmt='none', c='black',linewidth=2,capsize=2)
            
            axs[hist_ind_7,1].set_xlabel('$p_T$ [GeV]', fontsize=21)
            axs[hist_ind_7,1].set_ylabel(r'$\mathbf{\frac{\sigma_{PS+MPI+HAD}}{\sigma_{PS}}}$', fontsize=22)
            # axs[hist_ind_7,1].set_title('bornktmin 10, bornsuppfact 250',font='MonoSpace')
            # axs[hist_ind_7,1].set_ylim(-0.1, max(NPC_7)*1.2)
            # axs[hist_ind_7,1].set_ylim(0.85,1.2)
                        #Xfitter
            # xfitter_bins, xfitter_NP = xfitter_NPs(hist_7)
            # axs[hist_ind_7,1].step(xfitter_bins, xfitter_NP, label=r'arxiv:$2111.10431$', where='mid', linewidth=2, color='purple')
            
            
            
            axs[hist_ind_7,1].set_ylim(RANGE)
            #STANDARD RANGE (PLOT THIS RANGE FIRST BEFORE CHAGING)
            # axs[hist_ind_7,1].set_xlim(min(bins_7),max(bins_7))
            axs[hist_ind_7,1].set_xlim(min(bins_7),XMAX)
            # axs[hist_ind_7,1].set_xlim(100,2500)
            axs[hist_ind_7,1].axhline(y=1, color='black', linestyle='--')
            # axs[hist_ind_7,1].set_xticks(bins_7)
            axs[hist_ind_7,1].legend(loc='upper center', fontsize=19, mode='expand', ncol=2)
            axs[hist_ind_7,1].grid(axis='x')
            axs[hist_ind_7,1].set_yticks([0.9,1.0,1.1])

            
            # plt.tight_layout()
        
        
        fig.suptitle('Paris Params Pythia STA (HardQCD:all) $10^{10}$ events, Tune: %s' % TUNE.split('_')[0], font='MonoSpace')
        plt.tight_layout()
        plt.savefig(args.D+'/ALLBINS_Paris_Params_smallrange_HardQCD_%sRANDSOMSEED_RIVETMERGE_PYTHIA_STANDALONE.png'%str(args.D))
        plt.show()









    elif args.Matrix:
        average_pre=[]
        average_post=[]
        average_NPC = []
        average_bins=[]
        # for hist_ind, hist in enumerate(MAP_DICT.keys()):
        #     bins, pre, post = return_bins_pre_post(hist)
        #     NPC = post/pre
        # print(average_bins)

        bins, pre, post = return_bins_pre_post(list(MAP_DICT)[0])
        post_2d, pre_2d = np.meshgrid(post, pre)
        NPC = post_2d/pre_2d
        print(NPC)
        H= plt.pcolormesh(post_2d, pre_2d, NPC, vmin=- np.abs(NPC).max(), vmax=np.abs(NPC).max(), cmap ='Greens')
        #x: post, y: pre
        plt.colorbar(H)
        plt.show()

if __name__=="__main__":
    main()