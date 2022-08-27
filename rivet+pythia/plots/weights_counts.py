import matplotlib.pyplot as plt
import matplotlib
import argparse
import pprint



matplotlib.rcParams.update({
    "text.usetex": True})
import numpy as np
import pandas as pd
import mplhep as hep
hep.style.use("CMS") 

#MAPPING DICTIONARY BETWEEN The histo name and the rapidity bin ranges

parser=argparse.ArgumentParser(description='directory')
parser.add_argument('--D', required=True)
parser.add_argument('--Matrix', type=bool, required=False, default=False, help='if True, generate a matrix of the NPC in the (x,y)=(hadron,parton) space')
args = parser.parse_args()
D=args.D
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

post_yoda = 'suppr250_bornktmin10_1B_ParsiParams_posthadron_merged.yoda'
pre_yoda='suppr250_bornktmin10_1B_ParsiParams_prehadron_merged.yoda'
one_hist= 'BEGIN YODA_HISTO1D_V2 /CMS_2021_I1972986/' + 'd01-x01-y01'
two_hist= 'BEGIN YODA_HISTO1D_V2 /CMS_2021_I1972986/' + 'd02-x01-y01'
n_bins=MAP_DICT[ 'd01-x01-y01']['n_bins']

def get_hists_from_yoda(yoda_file):
    """ example of a yodafile is post_yoda = 'suppr250_bornktmin10_1B_ParsiParams_posthadron_merged.yoda"""
    sumw_l=[]
    sumw2_l=[]
    edges_low_l=[]
    counts_l = []
    with open(D+'/%s' % yoda_file, 'r') as f:
            f_readlines=f.readlines()
            for line_ind, line in enumerate(f_readlines):
                if one_hist in line:
                    begin_hist_ind = line_ind
                    # print(begin_hist_ind)
                # f.seek(0)
                    being_data_ind = begin_hist_ind+13
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
                        counts_l.append(count)
                        print(count)
                        being_data_ind +=1
    return counts_l, edges_low_l, sumw_l, sumw2_l

# print('len(edges_low_l)',len(edges_low_l))
# print(',len(sumw_l)',len(sumw_l))                    



# edges_low_l=np.array(edges_low_l,dtype=float)
# sumw_l=np.array(sumw_l,dtype=float)

counts_l_post, edges_low_l_post, sumw_l_post, sumw2_l_post = get_hists_from_yoda(yoda_file=post_yoda)
counts_l_pre, edges_low_l_pre, sumw_l_pre, sumw2_l_pre= get_hists_from_yoda(yoda_file=pre_yoda)
################################### PLOTTING ###################################
plt.scatter(edges_low_l_post, sumw_l_post, label='sum $w$ per bin, post')
plt.scatter(edges_low_l_pre, sumw_l_pre, label='sum $w$ per bin, pre')
ratio=np.array(counts_l_post,dtype=float)/np.array(counts_l_pre,dtype=float)
plt.scatter(edges_low_l_pre, ratio, label=r'ratio=$\frac{counts_{post}}{counts_{pre}}$')

plt.legend()
plt.show()



# if __name__ == '__main__':
    #Lets use --D suppr250_bornktmin10_1B_ParsiParams