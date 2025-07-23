import utils as u
import scientificPlot as splt
import sys
import os

fieldIntensity = sys.argv[1]
files = os.listdir()
ax = None
for file in files:
    if "_"+fieldIntensity+".0kAm" in file and ".txt" in file:
        print(file)
        data = u.readMatrix(file, ignore = " ")
        ax = splt.plot(data[:,-2], data[:,-1], ax)
splt.show()
