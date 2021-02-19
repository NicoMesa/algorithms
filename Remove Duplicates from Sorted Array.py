x = input("Enter a number:\n")
y = []
characters = [' ', ',']
for i in characters:
	x = x.replace(i, '')
for i in x:
	if i not in y:
		y.append(i)
print(len(y),y)

