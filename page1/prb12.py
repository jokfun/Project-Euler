#https://projecteuler.net/problem=12

number_divisor = 500

count=0
cursor = 0
while count<number_divisor:
	cursor+=1
	count=0
	test = int((cursor*(cursor+1))/2)
	for i in range(1,test):
		if test%i==0:
			count+=1
print("The first value which have over {} divisors is {}.".format(number_divisor,cursor))