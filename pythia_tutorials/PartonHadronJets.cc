// #include  <iostream>
#include "TFile.h"
#include "TTree.h"
#include "Pythia8/Pythia.h"

using namespace Pythia8;

//--------------------------------------------------------------------------

// Generic routine to extract the particles that existed right before
// the hadronization machinery was invoked.

//later the following will be done
  //  getPartonLevelEvent( pythia.event, partonLevelEvent);//catch all the particles at the parton level 
    // copy parton level event by catching it from the function and attaching it to a partonLevelEvent object
void getPartonLevelEvent( Event& event, Info& info, Event& partonLevelEvent) {

  // Copy over all particles that existed right before hadronization.
  partonLevelEvent.reset();
  for (int i = 0; i < event.size(); ++i)
  if (event[i].isFinalPartonLevel()) {
    //recall that ID codes are PDG codes, where negative means antiparticle
	// cout << "the status code of the parton level particle in this event including MPI" << event[i].status() << endl;
		//recall that status codes for particles at the top of the event record are positve, but when the particle
    // decays, its status code gets negated. info.nMPI() is the number of hard interactions in the current event.

    // cout << "the id code of the parton level particle in this event " << event[i].id() << endl;
  // status codes 31 – 39 imply particles from MPI
    int status = event[i].statusAbs();
    // cout << "ABS ( STATUS CODE OF THIS PARTICLE)" << status << endl;
          // if (status == 31 || status == 32 || status==33 || status=34|| status=35 || status==36|| status==37|| status==38 || status==39) {
          // if (status == 31 || status == 32 || status == 33 || status == 34 || status == 35 || status == 36 || status == 37 )  {

    int iNew = partonLevelEvent.append( event[i] );
          
    // Set copied properties more appropriately: positive status,
    // original location as "mother", and with no daughters.
    partonLevelEvent[iNew].statusPos();
    partonLevelEvent[iNew].mothers( i, i);
    partonLevelEvent[iNew].daughters( 0, 0);
  }
}
//------------------------------------------------
  // Remember you can Switch off all showering and MPI when extimating the cross section after
  // the merging scale cut. This is just for illustration
  // bool fsr = pythia.flag("PartonLevel:FSR");
  // bool isr = pythia.flag("PartonLevel:ISR");
  // bool mpi = pythia.flag("PartonLevel:MPI");
  // bool had = pythia.flag("HadronLevel:all");
  // pythia.settings.flag("PartonLevel:FSR",false);
  // pythia.settings.flag("PartonLevel:ISR",false);
  // pythia.settings.flag("HadronLevel:all",false);
  // pythia.settings.flag("PartonLevel:MPI",false);
//--------------------------------------------------------------------------

// Generic routine to extract the particles that exist after the
// hadronization machinery. Normally not needed, since SlowJet
// contains the standard possibilities preprogrammed, but this
// method illustrates further discrimination.

void getHadronLevelEvent( Event& event, Event& hadronLevelEvent) {

  // Iterate over all final particles.
  hadronLevelEvent.reset();
  for (int i = 0; i < event.size(); ++i) {
    bool accept = false;
    if (event[i].isFinal()) accept = true;

    // Copy over accepted particles, with original location as "mother".
    if (accept) {
      int iNew = hadronLevelEvent.append( event[i] );
// cout << "the status code of the hadron level particle in this event " << event[i].status() << endl;

      hadronLevelEvent[iNew].mothers( i, i);
    }

  }

}
//--------------------------------------------------------------------------

int main(int argc, char* argv[]) {

// make root file and ttree
TFile *Jetsoutput  = new TFile("Jetsoutput_2.root", "recreate");
TTree *tree = new TTree("tree", "tree");

// delcalre the variables for hadrons and partons
int numJetsParton, numJetsHadron;
//numbers of parton jets in an event, number of hadron jets in an event
double pTPartonJets, pTHadronJets, yPartonJets, yHadronJets, phiPartonJets, phiHadronJets;

//Define tree branches: we don't want histograms since well analyze the trees later
tree->Branch("numJetsParton", &numJetsParton, "numJetsParton/I");
tree->Branch("numJetsHadron", &numJetsHadron, "numJetsHadron/I");
tree->Branch("pTPartonJets", &pTPartonJets, "pTPartonJets/D");
tree->Branch("pTHadronJets", &pTHadronJets, "pTHadronJets/D");
tree->Branch("yPartonJets", &yPartonJets, "yPartonJets/D");
tree->Branch("yHadronJets", &yHadronJets, "yHadronJets/D");
tree->Branch("phiPartonJets", &phiPartonJets, "phiPartonJets/D");
tree->Branch("phiHadronJets", &phiHadronJets, "phiHadronJets/D");

  // Number of events, generated and listed ones.
  int nEvent    =50000;
  int nListEvts = 1;// number of Event objects that you want to list (display in stdout)
  int nListJets = 5;//number of Slowjet objects you want to list (diplay)

  // Generator. LHC process and output selection. Initialization.
  Pythia pythia;

pythia.readFile(argv[1]);

//   pythia.readString("Beams:eCM = 13000.");
//   pythia.readString("HardQCD:all = on");
//   pythia.readString("PhaseSpace:pTHatMin = 200.");
//   pythia.readString("Next:numberShowInfo = 0");
//   pythia.readString("Next:numberShowProcess = 0");
//   pythia.readString("Next:numberShowEvent = 5");

  pythia.init();

  // Parton and Hadron Level event records. Remeber to initalize.
  Event partonLevelEvent;//initialize Event class, which is basically a vector of particles
  partonLevelEvent.init("Parton Level event record", &pythia.particleData);
  Event hadronLevelEvent;
  hadronLevelEvent.init("Hadron Level event record", &pythia.particleData);

  //  Parameters for the jet finders. Need select = 1 to catch partons.
  double radius   = 0.4;
  double pTjetMin = 10.;
  double etaMax   = 4.;
  int select      = 1;

  // Initialize SlowJEt objects
  //Set up anti-kT clustering, comparing parton and hadron levels. -1=antikt
  SlowJet antiKTpartons( -1, radius, pTjetMin, etaMax, select);
  //make sure you don't put select=-1 for hadron jets
  SlowJet antiKThadrons( -1, radius, pTjetMin, etaMax);

  // Begin event loop. Generate event. Skip if error.
  for (int iEvent = 0; iEvent < nEvent; ++iEvent) {
    if (!pythia.next()) continue;

    // Construct parton and hadron level event.
    getPartonLevelEvent( pythia.event, pythia.info, partonLevelEvent);//catch all the particles at the parton level 
    // copy parton level event by atching it from the function and attaching it to partonLevelEvent object, which is an Event object
    getHadronLevelEvent( pythia.event, hadronLevelEvent);

    // List first few events.
    // if (iEvent < nListEvts) {
    //   pythia.event.list();
    //   partonLevelEvent.list();
    //   hadronLevelEvent.list();
    // }

    // Analyze jet properties and list first few analyses.
    antiKTpartons.analyze( partonLevelEvent );
    antiKThadrons.analyze( hadronLevelEvent );

//Print list
    // if (iEvent < nListJets) {
    //   antiKTpartons.list();
    //   antiKThadrons.list();
    // }

// FILL TREE
numJetsParton = antiKTpartons.sizeJet() ;
numJetsHadron = antiKThadrons.sizeJet() ;
tree->Fill();

  for (int i = 0; i < antiKTpartons.sizeJet(); ++i) {
pTPartonJets = antiKTpartons.pT(i) ;// Recall that pTPartonJets is just a branch in tree
yPartonJets = antiKTpartons.y(i);
phiPartonJets = antiKTpartons.phi(i);
  tree->Fill();
  }

  for (int i = 0; i < antiKThadrons.sizeJet(); ++i) {
  pTHadronJets = antiKThadrons.pT(i) ;
  yHadronJets = antiKThadrons.y(i);
  phiHadronJets = antiKThadrons.phi(i);
  tree->Fill();
  }

  // End of event loop. Statistics. Histograms.
  }
  pythia.stat();

// Write the file and close it
Jetsoutput->Write();
Jetsoutput->Close();
  // Done.
  return 0;
}
