#https://projecteuler.net/problem=16

digit = 1000
#Sum of digits of 2^1000 is 1366.

value = str(2**digit)
value = sum([int(k) for k in value])
print("Sum of digits of 2^{} is {}.".format(digit,value))