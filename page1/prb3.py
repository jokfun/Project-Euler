#https://projecteuler.net/problem=3

#With this value it'll take tooooooo much time
maxValue = 600851475143

#The test
maxValue = 13195


#First version
def isPrime(number,listPrime):
	for k in listPrime:
		if number%k==0:
			return False
	return True

prime = []
for i in range(2,maxValue):
	if maxValue%i==0 and isPrime(i,prime)==True:
		prime.append(i)
print("Version start at 0 :",prime[-1])


#Second version
for i in range(maxValue,2,-1):
	if maxValue%i==0:
		test = True
		for j in range(2,i-1):
			if i%j==0:
				test=False
				break
		if test==True:
			print("Version start at the end :",i)
			break