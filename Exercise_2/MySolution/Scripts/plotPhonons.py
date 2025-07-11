import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy.linalg import eig

m1 = 24.305 #u
m2 = 15.999 #u

datafile = '../Data/Forces'

data = np.loadtxt(datafile)
print('data:',data)
# format of data: in rows replacement 1x,1y,1z,2x,2y,2z
Fxs = data[:,3]
Fys = data[:,4]
Fzs = data[:,5]

ForceMatrix = np.zeros((6,6))
ForceMatrix[:3,0] = data[0,3:]/np.sqrt(m1*m1)
ForceMatrix[3:,0] = data[1,3:]/np.sqrt(m1*m2)

ForceMatrix[:3,1] = data[2,3:]/np.sqrt(m1*m1)
ForceMatrix[3:,1] = data[3,3:]/np.sqrt(m1*m2)

ForceMatrix[:3,2] = data[4,3:]/np.sqrt(m1*m1)
ForceMatrix[3:,2] = data[5,3:]/np.sqrt(m1*m2)

ForceMatrix[:3,3] = data[6,3:]/np.sqrt(m1*m2)
ForceMatrix[3:,3] = data[7,3:]/np.sqrt(m2*m2)

ForceMatrix[:3,4] = data[8,3:]/np.sqrt(m1*m2)
ForceMatrix[3:,4] = data[9,3:]/np.sqrt(m2*m2)

ForceMatrix[:3,5] = data[10,3:]/np.sqrt(m1*m2)
ForceMatrix[3:,5] = data[11,3:]/np.sqrt(m2*m2)


D = -1*ForceMatrix/(0.01)
print('ForceMatrix:\n',D)


valuesD,vectorsD = np.linalg.eig(D)

eV_to_Joule = 1.60218e-19
amu_to_kg = 1.66054e-27
Angstrom_to_m = 1e-10
conversion_factor = eV_to_Joule / (amu_to_kg * Angstrom_to_m**2)


print(valuesD,valuesYM)

print('eigenvalues in THz:',np.sqrt(conversion_factor*valuesD)/(2*np.pi*1e12))
