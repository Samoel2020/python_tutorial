num1= 6
num2= 23
num3= 7
from math import sqrt
def solver(a,b,c):
	
	x1 = (-b + sqrt(b**2 - 4*a*c)/2*a)
	x2 = (-b - sqrt(b**2 - 4*a*c)/2*a)

	return x1, x2

x1, x2 =solver(num1, num2, num3)
print(x1, x2)