import match sqrt

ax = int(input())
ay = int(input())
bx = int(input())
by = int(input())

d = sqrt (((ax - bx) ** (ax - bx)) + ((by - by) ** (by - by)))

if ( d >= 10 ):
	print ("longe")
else:
	print ("perto")
