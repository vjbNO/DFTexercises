import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


datafile = '../Data/energies_EnergyConvergence'
i=0
E0=100
step = 100
with open(datafile,'r') as file:
    for line in file:
        data = line.strip()
        x = float(data.split()[-2])
        print('read out energy:',x)
        plt.scatter(E0+i*step,x,color='black')
        i += 1
plt.xlabel('ENCUT')
plt.ylabel('Total energy')
plt.tight_layout()
plt.savefig('../Plots/test_energyconvergence.pdf')
plt.show()
