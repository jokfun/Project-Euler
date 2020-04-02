#https://projecteuler.net/problem=14

maxValue = 1000000
#Under 1000000 and starting with 837799, for a length of 525 the longest chain is : blablabla

maxlength = -1
chain = []
for i in range(1,maxValue+1):
	pos = i
	test = [pos]
	while pos!=1:
		if pos%2==0:
			pos= int(pos/2)
		else:
			pos = 3*pos + 1
		test.append(pos)
	if len(test)>maxlength:
		maxlength = len(test)
		chain = test[:]
print("Under {} and starting with {}, for a length of {} the longest chain is :\n{}".format(maxValue,chain[0],maxlength,chain))
