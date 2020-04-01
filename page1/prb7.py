#https://projecteuler.net/problem=7

prim_number = 10001
#Answer will be 10743 for 10 001

def isPrime(number,listPrime):
	for k in listPrime:
		if number%k==0:
			return False
	return True

listPrime = []
cursor = 2
while(len(listPrime)!=prim_number):
	if isPrime(cursor,listPrime)==True:
		listPrime.append(cursor)
	cursor+=1
print("{} is the {}st prime number.".format(listPrime[-1],prim_number))
