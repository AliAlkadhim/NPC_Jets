import os, sys, subprocess, time
from plotting import PDF
import py8settings as py8s


# Write beam settings to file.
cmnd_file = "settings.cmnd"
subprocess.call(["bash","-c","touch "+cmnd_file])
py8s.beam_settings(cmnd_file)


# Apply basic settings.
py8s.basic_settings(cmnd_file)


# Switch on/off simulation steps.
py8s.onoff_settings(cmnd_file)


# Write settings for phase-space cuts to file.
py8s.pscuts_settings(cmnd_file, 2)


# Write additional settings if needed.
#py8s.more_settings(cmnd_file, [".."])


# Start pythia+dire.
startdire = "main300 --visualize_event --input "+cmnd_file
subprocess.call(["bash","-c",startdire])


subprocess.call(["bash","-c","dot -Tpdf event-"+cmnd_file+".dot -o event-"+cmnd_file+".pdf"])
PDF("event-"+cmnd_file+".pdf",size=(900,600))



