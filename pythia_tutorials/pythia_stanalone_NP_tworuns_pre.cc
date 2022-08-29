// Headers and Namespaces.
#include "Pythia8/Pythia.h" // Include Pythia headers.
// #include  <iostream>
#include "TFile.h"
#include "TTree.h"


using namespace Pythia8;
// Let Pythia8:: be implicit.
int main() {
// Set up generation.
Pythia pythia;
    // make root file and ttree
TFile *TwoTime_pre_1M  = new TFile("TwoTime_pre_1M.root", "recreate");
TTree *tree = new TTree("tree", "tree");

int numJets;
double pTJet;

tree->Branch("numJets", &numJets, "numJets/I");
tree->Branch("pTJet", &pTJet, "pTJet/D");

pythia.readString("HardQCD:all		= on"); // Switch on process.
pythia.readString("Beams:idA = 2212 "); //proton.
pythia.readString("Beams:idB = 2212 "); //proton.
pythia.readString("Beams:eCM = 13000 "); 
pythia.readString("PhaseSpace:pTHatMin	= 10 "); 


pythia.readString("PartonLevel:ISR = on   "); 
pythia.readString("PartonLevel:FSR= on"); 
pythia.readString("PartonLevel:MPI = off");
pythia.readString("HadronLevel:all = off");  


// Declare Pythia object
// pythia.readString("Next:numberShowEvent = 5");
pythia.init(); // Initialize; incoming pp beams is default.

  double radius   = 0.4;
  double pTjetMin = 10.;
  double etaMax   = 4.;
double pow = -1;
SlowJet Jet( pow, radius, pTjetMin, etaMax);

// Generate 5 nevents.
int nevents = 1000000;
for (int iEvent=0; iEvent < nevents; ++iEvent) {

    if (!pythia.next()) continue;
     //START PARTICLE LOOP
//  for (int i = 0; i < pythia.event.size(); ++i) {
     
// cout << "i = " << i << ", id = " << pythia.event[i].() << endl;
// }

  Jet.analyze(pythia.event);
  numJets = Jet.sizeJet();
  tree->Fill();
  for (int i=0; i< numJets; ++i) {
      pTJet = Jet.pT(i); 
      tree->Fill();
}
}
pythia.stat();
TwoTime_pre_1M->Write();
TwoTime_pre_1M->Close();

return 0;
}
