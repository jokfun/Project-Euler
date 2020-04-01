#https://projecteuler.net/problem=4

numberDigit = 4

minValue = 10**(numberDigit-1)
maxValue = 10**numberDigit-1

def isPalindrome(x,y):
	val = str(x*y)
	for i in range(int(len(val)/2)):
		if val[i]!=val[-i-1]:
			return False
	return True

x = 0
y = 0
test = -1

for i in range(minValue,maxValue):
	for j in range(minValue,maxValue):
		if isPalindrome(i,j)==True and i*j>test:
			x,y,test = i,j,i*j
print("Highest palindrome is {} for x={} and y={}".format(test,x,y))
