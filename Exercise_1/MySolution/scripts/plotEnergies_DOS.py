import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


datafile = 'DOSCAR'

data1 = np.array(pd.read_csv(datafile,sep='\s+',header=5,nrows=1001))
Etot = data1[:,0]
DOStot = data1[:,1]
DOScum = data1[:,2]

data2 = np.array(pd.read_csv(datafile,sep='\s+',header=1007,skiprows=lambda i: i%1002 == 0))
E = data2[:,0]
s = data2[:,1]
py = data2[:,2]
pz = data2[:,3]
px = data2[:,4]


plt.plot(Etot,DOStot,color='red',label='total')

plt.scatter(E,s,color='black',label='s',s=1)
plt.scatter(E,py,color='navy',label='py',s=1)
plt.scatter(E,pz,color='blue',label='pz',s=1)
plt.scatter(E,px,color='turquoise',label='px',s=1)

plt.xlim(6-6,6+6)
plt.ylim(0,5)
plt.legend()
plt.xlabel('E')
plt.ylabel('DOS')
plt.tight_layout()
plt.savefig('test_DOS.pdf')
plt.show()
