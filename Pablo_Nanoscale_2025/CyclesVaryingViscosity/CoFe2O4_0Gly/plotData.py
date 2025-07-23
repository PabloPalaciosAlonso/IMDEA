import scientificPlot as splt
import sys
import os
import numpy as np

fieldIntensity = sys.argv[1]
files = os.listdir()
ax = None
for file in files:
    if "_"+fieldIntensity+".0kAm" in file and ".txt" in file:
        if "297" in file or "198" in file:
            continue
        data = np.loadtxt(file)
        print(file)
        ax = splt.plot(data[:,-2], data[:,-1], ax)
splt.show()
