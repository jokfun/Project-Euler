#https://projecteuler.net/problem=10

max_value = 2000000
#Sum of prime numbers below 2000000 is 142913828922.

def isprime(number,listPrime):
	for k in listPrime:
		if number%k==0:
			return False
	return True

listPrime = []
for i in range(2,max_value+1):
	if isprime(i,listPrime)==True:
		listPrime.append(i)
print("Sum of prime numbers below {} is {}.".format(max_value,sum(listPrime)))