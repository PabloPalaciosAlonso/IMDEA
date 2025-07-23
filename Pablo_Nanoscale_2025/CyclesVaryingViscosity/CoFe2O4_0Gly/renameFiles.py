import os
import numpy as np

def readFreqAndField(filename):
    file = open(filename)
    for line in file:
        if "Tuned frequency" in line:
            frequency = (line.split(" ")[-2])
            field = (line.split(" ")[-6])
            break
    return field, frequency
        
files = os.listdir()
for filename in files:
    if "CoFe" in filename and "~" not in filename:
        [field, freq] = readFreqAndField(filename)
        newFilename = "CoFe2O4_"+field+"kAm_"+freq+"kHz.txt"
        os.rename(filename, newFilename)
