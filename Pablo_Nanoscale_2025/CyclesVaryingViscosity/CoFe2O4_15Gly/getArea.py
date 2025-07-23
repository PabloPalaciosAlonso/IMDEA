import os
import numpy as np

def askFieldIntensity():
    fieldIntensity = input("Which field intensity you want to analyze?\n(The value of the field intensity should be contained in the name of all the files as valuekAm)\n")
    return fieldIntensity

def readFreqAreaAndError(filename):
    file = open(filename)
    for line in file:
        if "Tuned frequency" in line:
            frequency = float(line.split(" ")[-2])
        if "Area" in line:
            area = float(line.replace(" ","").split("\t")[-2])
            error = float(line.replace(" ","").split("\t")[-1])
            break
    return frequency, area, error
        
files = os.listdir()
fieldIntensity = askFieldIntensity()
fileWrite = open("Areas_field_"+str(fieldIntensity)+"_kAm.txt", "w")
fileWrite.write("#f\tArea\tError\n")
frequencyDict = {}
for filename in files:
    if " "+str(fieldIntensity)+"kAm" in filename or " "+str(fieldIntensity)+" kAm" in filename:
        [f,A, dA] = readFreqAreaAndError(filename)
        frequencyDict[f] = [A, dA]

frequencies = np.sort(np.array(list(frequencyDict.keys())))
for f in frequencies:
    fileWrite.write(str(f)+"\t"+str(frequencyDict[f][0])+"\t"+str(frequencyDict[f][1])+"\n")
fileWrite.close()
