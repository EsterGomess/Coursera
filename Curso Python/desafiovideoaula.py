import match
# -*- coding: utf-8 -*-

a = float(input())
b = float(input())
c = float(input())

delta = (b*b) - 4 * a * c

x = (-b + sqrt(delta)) / 2 * a
y = (b + sqrt(delta)) / 2 * a

if ( x < 0) and (y < 0):
	print ("esta equação não possui raízes reais""
if (x > 0) and (y < 0):
	print (" a raiz desde equação é ", x)
if (x < 0) and (y > 0):
	print (" a raiz desde equação é ", y)
else : 
	if (x < y)
	print (" as raízes da equação são ",x , "e",y )
	else
	print (" as raízes da equação são ",y , "e",x)
