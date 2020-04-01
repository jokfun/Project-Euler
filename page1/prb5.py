#https://projecteuler.net/problem=5

maxNumber = 20
#for 20, result : 232792560

possibilities = [i for i in range(1,maxNumber+1)]

test = True
cursor = 0
while test:
	cursor+=1
	check = True
	for k in possibilities:
		if cursor%k!=0:
			check=False
	if check == True:
		test=False
print("Smallest positive number is",cursor)

