// Headers and Namespaces.
#include "Pythia8/Pythia.h" // Include Pythia headers.
// #include  <iostream>
#include "TFile.h"
#include "TTree.h"

// THIS EXPECTS THAT YOU HAVE A .cmnd ARGUMENTS FILE
// for example, I'm using Paris_prehadron.cmnd
using namespace Pythia8;
// Let Pythia8:: be implicit.
int main(int argc, char* argv[]) {
// Set up generation.
Pythia pythia;
  // Confirm that external files will be used for input and output.
  cout << "\n >>> PYTHIA settings will be read from file " << argv[1] <<endl;

// READ FROM .cmnd FILE
pythia.readFile(argv[1]);


    // make root file and ttree
TFile *weights  = new TFile("weight_studies/WEIGHTS_pre_10K_ParisParams.root", "recreate");
TTree *tree = new TTree("tree", "tree");


// Get initial info frmo argument file
int nevents = pythia.mode("Main:numberOfEvents");
  // int    nAbort    = pythia.mode("Main:timesAllowErrors");

cout << "\n will generate" << nevents << "events" << endl;



//initialize variables to be stored in root
int numJets;
double pTJet;
double evtWeight;
//make ttree branches
tree->Branch("numJets", &numJets, "numJets/I");
tree->Branch("pTJet", &pTJet, "pTJet/D");
tree->Branch("evtWeight", &evtWeight, "evtWeight/D");

// optional parameters (to override .cmnd file)
// pythia.readString("HardQCD:all		= on"); // Switch on process.
// pythia.readString("Beams:idA = 2212 "); //proton.
// pythia.readString("Beams:idB = 2212 "); //proton.
// pythia.readString("Beams:eCM = 13000 "); 
// //pythia.readString("PhaseSpace:pTHatMin	= 10 "); 
//  pythia.readString("PhaseSpace:bias2Selection=on");
// pythia.readString("PartonLevel:MPI = off");
// pythia.readString("HadronLevel:all = off");  


// Declare Pythia object
// pythia.readString("Next:numberShowEvent = 5");
pythia.init(); // Initialize; incoming pp beams is default.

double radius   = 0.4;
double pTjetMin = 10.;
double etaMax   = 4.;
double pow = -1;
// Decalre SlowJet (FastJet) object
SlowJet Jet( pow, radius, pTjetMin, etaMax);

// Generate nevents.

for (int iEvent=0; iEvent < nevents; ++iEvent) {

    if (!pythia.next()) continue;
     //START PARTICLE LOOP
//  for (int i = 0; i < pythia.event.size(); ++i) {
     
// cout << "i = " << i << ", id = " << pythia.event[i].() << endl;
// }
  // Get the event weight
  evtWeight = pythia.info.weight();
  //fill tree with weight
  tree->Fill();
  Jet.analyze(pythia.event);
  numJets = Jet.sizeJet();
  tree->Fill();
  for (int i=0; i< numJets; ++i) {
      pTJet = Jet.pT(i); 
      tree->Fill();
}
}
pythia.stat();
cout << " <<< \n >>> root events will be written to file " << argv[2] << " <<< \n" << endl;

weights->Write();
weights->Close();

return 0;
}
