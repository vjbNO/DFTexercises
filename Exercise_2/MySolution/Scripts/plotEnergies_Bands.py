import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


datafile = '../Data/energies_band'
i=1
for i in range(8):
    with open(datafile+str(i),'r') as file:
        E = []
        for line in file:
            data = line.strip()
            x = float(data.split()[-4]) - 6
            E.append(x)
    plt.plot(np.arange(len(E)),E,marker='o')
    i += 1
plt.xticks([0,9,19,29,39],['L','Gamma','X','U,K','Gamma'])
plt.ylabel('E-E_f (eV)')
plt.tight_layout()
plt.savefig('../Plots/test_Bandstructure.pdf')
plt.show()
