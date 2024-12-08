import matplotlib.pyplot as plt
import numpy as np
import random as rndm
import pandas as pd

n = int(input(""))

list1 = []
list2 = []

for i in range(n):
    list1.append(i)
    j = rndm.random()
    if (j>0.5):
        list2.append(i + (j*(10**(rndm.random()))))
    else:
        list2.append(i - (j*(10**(rndm.random()))))

nplist1 = np.array(list1)
nplist2 = np.array(list2)

np1 = nplist1.view()
np2 = nplist2.view()
npline = np.array([[np1[0],np1[n-1]],[np2[0],np2[n-1]]])

plt.plot(npline[0],npline[1])
plt.plot(np1,np2,'o')
plt.show()

dataset = pd.Series(np2, index = np1)

print(dataset)