import uproot
import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
hep.style.use("CMS")
print(uproot.__version__)
import uproot3
print(uproot3.__version__)
import uproot3 as uproot

def tworuns(filepre, filepost):
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


            r=(0,200)
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


            ax1.scatter(Partonptcenters, Partonptcounts, label='parton-level jet $p_T$ bin centers',
                    color="r",facecolors='none', marker="X", s=10, linewidth=0.9)

            ax1.scatter(Hadronptcenters, Hadronptcounts, label='hadron-level jet $p_T$ bin centers', 
                        color="k",facecolors='none', marker="X", s=20, linewidth=0.9)


            
            ax1.legend()

            ratio = Hadronptcounts/Partonptcounts

            ax2.scatter(Partonptcenters, ratio,
                    color="r",facecolors='none', marker="X", s=12, linewidth=1)
            ax2.step(Partonptcenters, ratio, label='ratio',
                    color="r",   linewidth=1)

            ax2.set_xlim(r)
            ax2.set_ylim((0,1.8))
            # ticks=np.linspace(0, 1.7, 4)
            ticks=[0,0.5,1,1.5,2]
            ax2.set_yticks(ticks)
            ones=np.linspace(0,1000, num=1000)

            ax2.scatter(ones, np.ones(1000), marker="o", s=5,linewidth=0.7)
            ax2.legend(loc='upper left')
            ax2.set_xlabel(r'$p_T$ [GeV]')
            # plt.savefug('pythia_standalone_
            fig.suptitle('Pythia Standalone, $10^6$ Events')
            plt.savefig('Pythia_Standalone_NP_TwoRuns_1M.png')

tworuns(filepre='TwoTime_pre_1M.root',filepost='TwoTime_post_1M.root')