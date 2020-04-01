#https://projecteuler.net/problem=2

import numpy as np

x = 1
y = 2
maxvalue = 4e6

tab = [x,y]
cursor = x+y
i = 1
while cursor<maxvalue:
	tab.append(cursor)
	cursor = tab[i] + tab[i-1]
	i+=1
result = np.sum([k for k in tab if k%2==0])
print(result)

