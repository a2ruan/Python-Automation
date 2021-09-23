#If you want to make a class (lib), that is not instanced.  Use static methods.

class Math:

	@staticmethod
	def add5(x):
		return x + 5

	@staticmethod
	def add10(x):
		return x + 10

	@staticmethod
	def hello_world():
		print('Hello World')

print(Math.add5(5)) 