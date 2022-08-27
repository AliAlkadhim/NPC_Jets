#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

#include <TH1.h>

void read_hists()
{
TFile *f=new TFile("suppr250_bornktmin10_100M_ParsiParams_posthadron_merged.root");
TH1F *h = (TH1F*)f->Get("d21-x01-y01");
h->Draw();
}
