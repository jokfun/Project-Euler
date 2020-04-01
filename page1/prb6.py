#https://projecteuler.net/problem=6

max_value = 100

sum_square = 0
square_sum = 0

for i in range(1,max_value+1):
	sum_square+=i**2
	square_sum+=i
print("Result :",(square_sum**2)-sum_square)