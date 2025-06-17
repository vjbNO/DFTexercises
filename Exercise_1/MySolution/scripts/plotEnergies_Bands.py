import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


datafile = 'energies_band'
i=1
for i in range(8):
    with open(datafile+str(i),'r') as file:
        E = []
        for line in file:
            data = line.strip()
            x = float(data.split()[-4])
            E.append(x)
    plt.plot(np.arange(len(E)),E,marker='o')
    i += 1
plt.xlabel('k')
plt.ylabel('E')
plt.tight_layout()
plt.savefig('test_Bandstructure.pdf')
plt.show()
