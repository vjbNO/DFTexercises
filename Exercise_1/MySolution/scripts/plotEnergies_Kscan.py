import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


datafile = 'energies_Kscan'
i=0
n0=4
step = 1
with open(datafile,'r') as file:
    for line in file:
        data = line.strip()
        x = float(data.split()[-2])
        print('read out energy:',x)
        plt.scatter(n0+i*step,x,color='black')
        i += 1
plt.xlabel('n kpoints')
plt.ylabel('Total energy')
plt.tight_layout()
plt.savefig('test_KpointConvergence.pdf')
plt.show()
