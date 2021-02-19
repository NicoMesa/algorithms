# palindrome
# It recognize if a word or number is a palindrome or not. 

x = (input("Ingrese una palabra: "))
if x == x[::-1]:
	print("Es palindromo")
else:
	print("No es palindromo")
