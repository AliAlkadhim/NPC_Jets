import uproot
import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
hep.style.use("CMS")
print(uproot.__version__)
import uproot3
print(uproot3.__version__)
import uproot3 as uproot
import argparse

parser=argparse.ArgumentParser(description='just files')
parser.add_argument('--pre', type=str, help='the root file of pre')
parser.add_argument('--post', type=str, help='the root file of post')
parser.add_argument('--N', type=int, help='the number of events simulated')
args=parser.parse_args()


def tworuns(filepre, filepost, N):
    ptbins=[97,  133,  174,  220,  272,  330,  395,  468,  548,  638,  737,  846, 967, 1101, 1248, 1410, 1588, 1784, 2000, 2238, 2500, 2787]
    with uproot.open(filepre) as filepre:
        with uproot.open(filepost) as filepost:
            print('file keys', filepre.keys())
            treepre = filepre["tree"]
            treepost = filepost["tree"]
            print()
            print('treepre keys',treepre.keys())
            print()
            print('treepre["pTJet"] =',treepre["pTJet"])
    #         print()
            ptpre = treepre.arrays(["pTJet"], outputtype = tuple)
            ptpost = treepost.arrays(["pTJet"], outputtype = tuple)

    #         # pt_part = pt["pTPartonJets"]
    #         # pt_had = pt["pTHadronJets"]
            # print('pt=', pt)


            r=(10,200)
            b=22

            Partonptcounts, Partonptedges = np.histogram(ptpre, bins=b, range=r)
            Hadronptcounts, Hadronptedges = np.histogram(ptpost, bins=b, range=r)

            print('Partonptcounts = ', Partonptcounts)
            print('PartonPartonptcounts.shape = ', Partonptcounts.shape)


            Partonptcenters = (Partonptedges[1:]+Partonptedges[:-1])/2
            Hadronptcenters = (Hadronptedges[1:]+Hadronptedges[:-1])/2

    #         print('Partonptcounts = ', Partonptcounts)

    #         print('Partonptcounts.shape = ', Partonptcounts.shape)
    #         print('\nPartonptedges.shape =' , Partonptedges.shape)
    #         print('\nPartonptcenters.shape =' , Partonptcenters.shape)


            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10,10), gridspec_kw={'height_ratios': [2,1]})


            ax1.scatter(Partonptcenters, Partonptcounts, label=r'parton-level $N_{jets}$',
                    color="r",facecolors='none', marker="X", s=14, linewidth=0.9)

            ax1.scatter(Hadronptcenters, Hadronptcounts, label='hadron-level $N_{jets}$', 
                        color="k",facecolors='none', marker="X", s=20, linewidth=0.9)

            ax1.set_yscale('log')
            #ax1.set_yticks()

            
            ax1.legend()

            ratio = Hadronptcounts/Partonptcounts

            ax2.scatter(Partonptcenters, ratio,
                    color="red",facecolors='none', marker="o", s=12, linewidth=1)
            ax2.step(Partonptcenters, ratio,
                    color="r",   linewidth=2)
            ax2.set_ylabel(r'$\frac{N_{jets}^{hadron}}{N_{jets}^{parton}}$')
            ax2.set_xlim(r)
            ax2.set_ylim((0.9,1.2))
            # ticks=np.linspace(0, 1.7, 4)
            #ticks=[0,0.5,1,1.5,2]
            #ax2.set_yticks(ticks)
            ones=np.linspace(0,1000, num=1000)

            ax2.scatter(ones, np.ones(1000), marker="o", s=5,linewidth=0.7)
            ax2.legend(loc='upper left')
            ax2.set_xlabel(r'$p_T$ [GeV]')
            # plt.savefug('pythia_standalone_
            fig.suptitle('Pythia Standalone, %d Events' % N )
            fig.subplots_adjust(left=0.15)
            plt.savefig('Pythia_Standalone_NP_TwoRuns_%d_Events.png' % N)
            plt.show()

def main():
        tworuns(filepre=args.pre,filepost=args.post, N=args.N)

if __name__ == '__main__':
        main()
