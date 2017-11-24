
n= int(input("digite um numero inteiro: ")

aux1 = n % 2 
aux2 = n % 3
aux3 = n% 5

if (aux1 == 0) and (aux2 ==0) and (aux3 == 0):
	print ("não primo")
else:
	print ("primo")
