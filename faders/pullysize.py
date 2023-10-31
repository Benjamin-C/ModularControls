minDiam = 4 # mm
maxDiam = 15 # mm
travelTime = 0.500 # s
travelLength = 80 # mm
ppr = 12 # pulse per revolution

import numpy as np
import matplotlib.pyplot as plt

times = np.linspace(0.1, 0.5, 100)
mmps = travelLength / times
minCirc = (np.pi * minDiam)
maxCirc = (np.pi * maxDiam)

ppt = (travelLength / minCirc) * ppr
mmpp = travelLength / ppt
print(mmpp)

minRPM = (mmps / maxCirc) * 60
maxRPM = (mmps / minCirc) * 60

fix,ax = plt.subplots()

ax.plot(times, minRPM)
ax.plot(times, maxRPM)

ax2 = ax.twinx()
ax2.plot(times, mmps, "--")

ax.grid(True, 'both')
ax2.grid(True, 'both')

plt.show()
