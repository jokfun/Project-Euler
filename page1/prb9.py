#https://projecteuler.net/problem=9
#The poduct is 31875000 for the couple 200,375,425

import math

for a in range(0,332):
	for b in range(a+1,499):
		for c in range(b+1,1000):
			if a**2+b**2==c**2 and a+b+c==1000:
				print("The poduct is {} for the couple {}.".format(a*b*c,str(a)+","+str(b)+","+str(c)))
				quit()