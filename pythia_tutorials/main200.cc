// main01.cc is a part of the PYTHIA event generator.
// Copyright (C) 2019 Torbjorn Sjostrand.
// PYTHIA is licenced under the GNU GPL v2 or later, see COPYING for details.
// Please respect the MCnet Guidelines, see GUIDELINES for details.

// This is a simple test program. It fits on one slide in a talk.
// It studies the charged multiplicity distribution at the LHC.

#include "Pythia8/Pythia.h"
using namespace Pythia8;
int main() {
  Pythia pythia;

  // Initialise pythia on LHE file for qqbar-> W
  pythia.init("./w+_production_lhc_0.lhe");

  // Generate event(s).
  pythia.next();
  return 0;
}
