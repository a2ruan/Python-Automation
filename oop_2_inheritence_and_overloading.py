# inheritance
class Pet: 
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old")

	def speak(self):
		print("I don't know what I am")

class Cat(Pet):
	def __init__(self, name, age, color):
		super().__init__(name,age)  #important to not overload constructor.  Use super, in case super classes need to connect to database ect.
		self.color = color #extra non-super characteristics can be initialized here

	def speak(self): #EXAMPLE OF OVERLOADING
		print("Meow")

class Dog(Pet):
	def speak(self):
		print("Bark")

class Fish(Pet):
	pass

p1 = Pet("Tim",19)
p1.show()
p1.speak()

c1 = Cat("Bill",19)
c1.show()
c1.speak()

d1 = Dog("Jill",19)
d1.show()
d1.speak()

f1 = Fish("Bubbles",10)
f1.speak() # example of having default methods