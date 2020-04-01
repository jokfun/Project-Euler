#https://projecteuler.net/problem=1

import numpy as np 

x = 3
y = 5

maxValue = 1000

#Both solutions print the same answer


#Smallest answer
result = np.sum([i for i in range(x,maxValue) if i%x == 0] + [i for i in range(y,maxValue) if i%y == 0])
print(result)




#Long one
tab = []
for k in [x,y]:
	for i in range(k,maxValue):
		if i%k == 0:
			tab.append(i)
result = 0
for k in tab:
	result+=k
print(result)