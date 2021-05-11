from math import sqrt


#--------------------------------------------------------------------------
class Solver():

	def __init__(self, a, b, c):
		"""
		Class Solver: to solve quadratic equation.
		---
		Parameters:
		@param: a, float.
		@param: b, float.
		@param: c, float
		---
		a*x^2 + b*x + c = 0
		"""
		self.a = a
		self.b = b
		self.c = c

	def mySolver(self):
		"""
		Function: mysolver, to solve the quadratic equation.
		---
		Parameters:
		@param: None
		---
		return:
		x1, x2, float, float, the solutions of the quadratic equation
		"""
		x1 = -self.b + sqrt(self.b**2 - 4*self.a*self.c)/2*self.a
		x2 = -self.b - sqrt(self.b**2 - 4*self.a*self.c)/2*self.a
		
		return x1, x2
#------------------------------------------------------------------------

# instance of the class with parameters
sol = Solver(6, 23, 7)
# call to a function on the class
x1, x2 = sol.mySolver()
# print
print(x1, x2, '\n', sol.a, sol.b, sol.c)


"""
from math import sqrt
def solver(a,b,c):
		
	x1 = (-b + sqrt(b**2 - 4*a*c)/2*a)
	x2 = (-b - sqrt(b**2 - 4*a*c)/2*a)
	return x1, x2


x1, x2 =solver(6, 23, 7)
print(x1, x2)
"""