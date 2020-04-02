#https://projecteuler.net/problem=15

val_max = 20
#For a 20*20 grid, there're 137846528820 routes.

#Short version
#Using Pascal's Triangle
score = 2
for i in range(2,val_max+1):
	score = score*(4*i-2)/i
print("For a {}*{} grid, there're {} routes.".format(val_max,val_max,int(score)))

#Super long version
def loop(x,y,val_max):
	value = 0
	if x==val_max and y==val_max:
		return 1
	if x!=val_max:
		value+=loop(x+1,y,val_max)
	if y!=val_max:
		value+=loop(x,y+1,val_max)
	return value
print("For a {}*{} grid, there're {} routes.".format(val_max,val_max,loop(0,0,val_max)))

