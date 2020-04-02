#https://projecteuler.net/problem=17

#The number of letters used to write 1 to 1000 is 21489

dic_digit = {
	"0":0,
	"1":3,
	"2":3,
	"3":5,
	"4":4,
	"5":4,
	"6":3,
	"7":5,
	"8":5,
	"9":4
}
dic_10 = {
	"10":3,
	"11":6,
	"12":6,
	"13":8,
	"14":8,
	"15":7,
	"16":7,
	"17":9,
	"18":8,
	"19":8
}

dic_double = {
	"0":0,
	"2":6,
	"3":6,
	"4":6,
	"5":5,
	"6":5,
	"7":7,
	"8":6,
	"9":6
}

count = 0
for i in range(1,1000):
	cursor = [k for k in str(i)]
	if len(cursor)==1:
		count+=dic_digit[cursor[0]]
	else :
		pos = 0
		if len(cursor)==3:
			pos=1
			count+=dic_digit[cursor[0]]+7
		if not(cursor[0+pos]=="0" and cursor[1+pos]=="0"):
			count+=3 #the "and"
			if cursor[0+pos]=="1":
				count+=dic_10[cursor[0+pos]+cursor[1+pos]]
			else:
				count+=dic_double[cursor[0+pos]]+dic_digit[cursor[1+pos]]
count+=11 #one thousand
print("The number of letters used to write 1 to 1000 is",count)
