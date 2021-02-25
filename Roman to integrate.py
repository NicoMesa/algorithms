Roman= {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
total = 0
x = str(input("Enter a Roman number:\n "))
for i in range(len(x)):
	if i + 1 != len(x) and Roman[x[i]] < Roman[x[i+1]]:
		total = total - Roman[x[i]]
	else:
		total = total + Roman[x[i]]
print(total)
