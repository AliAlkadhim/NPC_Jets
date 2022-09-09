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
parser.add_argument('--slice', required=True)
parser.add_argument('--Matrix', type=bool, required=False, default=False, help='if True, generate a matrix of the NPC in the (x,y)=(hadron,parton) space')
args = parser.parse_args()
SLICE=args.slice
#ASSUMING EVERYTHING is in /RAW/CMS_2021_I1972986/  , for example /RAW/CMS_2021_I1972986/d23-x01-y01

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



if SLICE=='250_10':
    dir = 'suppr250_bornktmin10_1B_ParsiParams'
    fig_title=r'$(250,10) $, 1B Events, AK4 $0 \le | y| \le 0.5$'
    post_yoda = 'suppr250_bornktmin10_1B_ParsiParams_posthadron_merged.yoda'
    pre_yoda='suppr250_bornktmin10_1B_ParsiParams_prehadron_merged.yoda'
    one_hist= 'BEGIN YODA_HISTO1D_V2 /RAW/CMS_2021_I1972986/' + 'd01-x01-y01'
    two_hist= 'BEGIN YODA_HISTO1D_V2 /RAW/CMS_2021_I1972986/' + 'd02-x01-y01'

elif SLICE=='800_600':
    dir = 'suppr800_bornktmin600_1B_ParisParams_MSTP'
    fig_title='$(800,600) $, 1B Events, AK4 $0 \le | y| \le 0.5$'
    post_yoda = 'suppr800_bornktmin600_1B_ParisParams_MSTP_posthadron_merged.yoda'
    pre_yoda='suppr800_bornktmin600_1B_ParisParams_MSTP_prehadron_merged.yoda'
    one_hist= 'BEGIN YODA_HISTO1D_V2 /RAW/CMS_2021_I1972986/' + 'd01-x01-y01'
    two_hist= 'BEGIN YODA_HISTO1D_V2 /RAW/CMS_2021_I1972986/' + 'd02-x01-y01'



n_bins=MAP_DICT[ 'd01-x01-y01']['n_bins']

def get_hists_from_yoda(yoda_file):
    """ example of a yodafile is post_yoda = 'suppr250_bornktmin10_1B_ParsiParams_posthadron_merged.yoda"""
    sumw_l=[]
    sumw2_l=[]
    edges_low_l=[]
    counts_l = []
    with open(dir+'/%s' % yoda_file, 'r') as f:
            f_readlines=f.readlines()
            for line_ind, line in enumerate(f_readlines):
                if one_hist in line:
                    begin_hist_ind = line_ind
                    # print(begin_hist_ind)
                # f.seek(0)
                    being_data_ind = begin_hist_ind+12
                    # pprint.pprint(f_readlines[being_data_ind:being_data_ind+n_bins])
                    for i in range(n_bins):
                        edge_low = f_readlines[being_data_ind].split()[0]
                        edges_low_l.append(float(edge_low))
                        # print(edge_low)
                        # print('####################################################')
                        sumw = f_readlines[being_data_ind].split()[2]
                        # print(sumw)
                        sumw_l.append(float(sumw))
                        sumw2 = f_readlines[being_data_ind].split()[3]
                        sumw2_l.append(sumw2)
                        count = f_readlines[being_data_ind].split()[-1]
                        counts_l.append(float(count) + 1.e-10)
                        print('COUNTS = ', count)
                        being_data_ind +=1
    return np.array(counts_l,dtype=float), np.array(edges_low_l,dtype=float),  np.array(sumw_l,dtype=float), np.array(sumw2_l,dtype=float)

# print('len(edges_low_l)',len(edges_low_l))
# print(',len(sumw_l)',len(sumw_l))                    



# edges_low_l=np.array(edges_low_l,dtype=float)
# sumw_l=np.array(sumw_l,dtype=float)

counts_l_post, edges_low_l_post, sumw_l_post, sumw2_l_post = get_hists_from_yoda(yoda_file=post_yoda)
counts_l_pre, edges_low_l_pre, sumw_l_pre, sumw2_l_pre= get_hists_from_yoda(yoda_file=pre_yoda)
################################### PLOTTING ###################################
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,10), gridspec_kw={'height_ratios': [2,1.5]})
fig.suptitle(fig_title)
ax1.step(edges_low_l_post, sumw_l_post, where='mid', linewidth=1, label='$\sum w$  post')
ax1.step(edges_low_l_pre, sumw_l_pre,where='mid', linewidth=1, label='$\sum w$  pre')

ax1.set_xticklabels([])
ax1.set_ylabel(r'$\sum w$')
ax1.set_yscale('log')
ratio=np.array(counts_l_post,dtype=float)/np.array(counts_l_pre,dtype=float)

Neff_post = (sumw2_l_post)/sumw_l_post
Neff_pre = (sumw2_l_pre)/sumw_l_pre

ax2.scatter(edges_low_l_post, Neff_post, linewidth=0.5, label=r'$N_{eff}$ post',alpha=0.4, color='r')
ax2.scatter(edges_low_l_pre, Neff_pre, linewidth=0.5, label=r'$N_{eff}$ pre',alpha=0.4, color='blue')

ax2.scatter(edges_low_l_post, counts_l_post, linewidth=0.5, label=r'$\sigma$ post',alpha=0.4, color='black')
ax2.scatter(edges_low_l_pre, counts_l_pre, linewidth=0.5, label=r'$\sigma$ pre',alpha=0.4, color='green')


ax2.set_ylabel(r'$N_{eff}$')
ax2.set_yscale('log')
# ax2.set_ylabel(r'NP ratio=$\frac{counts_{post}}{counts_{pre}}$')
# ax2.scatter(edges_low_l_pre, ratio/ratio,color='k', linewidth=0.4)
# ax2.set_ylim((0,2))

fig.subplots_adjust(wspace=0.5, hspace=0.2)
# ax1.legend();#
ax2.set_xlabel(r'$p_T$  [GeV]')
ax2.legend(fontsize=12)
ax1.legend()
# plt.gca().set_position([0, 0, 1, 1])
# plt.show()
plt.savefig('weights_counts/'+str(SLICE)+'_1B_Neff.png')

# if __name__ == '__main__':
    #Lets use --D suppr250_bornktmin10_1B_ParsiParams