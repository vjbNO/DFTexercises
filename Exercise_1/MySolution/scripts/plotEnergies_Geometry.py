import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


datafile = 'energies_Geometry'
i=0
n0=4.1
step = 0.1
with open(datafile,'r') as file:
    for line in file:
        data = line.strip()
        x = float(data.split()[-2])
        print('read out energy:',x)
        plt.scatter(n0+i*step,x,color='black')
        i += 1
plt.xlabel('distance')
plt.ylabel('Total energy')
plt.tight_layout()
plt.savefig('test_Geometry.pdf')
plt.show()
