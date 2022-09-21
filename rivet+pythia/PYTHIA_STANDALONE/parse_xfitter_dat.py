import os
import numpy as np

dir_211_10431 = '../../xfitter_datafiles/xfitter-datafiles/lhc/cms/jets/2111.10431/NP/'
print(os.listdir(dir_211_10431))
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

def xfitter_NPs(rap_bin):
    file_string = dir_211_10431 + MAP_DICT_AK4[rap_bin]['xfitter_file']
    print(file_string)
    
    n_bins=MAP_DICT_AK4[rap_bin]['n_bins']
    with open(file_string, 'r') as f:
        bins_list=[]
        NPC_list=[]


        fr =f.readlines()
        for line_ind, line in enumerate(fr):
            bins_list.append(float(line.strip().split()[2]))
            NPC_list.append(float(line.strip().split()[-1]))
        
        return np.array(bins_list) , np.array(NPC_list)
            
                


def main():
    rap_bin='d03-x01-y01'
    bins, NP=xfitter_NPs(rap_bin)
    print(NP.shape)
    print(NP)
    print()
    print(bins)
    
if __name__ == '__main__':
    main()