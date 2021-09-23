#class methods, class attribute
# CLASS ATTRIBUTE REQUIRES CLASS.ATTRIBUTE TO ACCESS
# CLASS METHOD MUST USE cls (class object general) AS PARAMETER, AND CAN MODIFY THE CLASS STATE
# STATIC METHOD DON'T NEED cls.  No params OK, BUT CANNOT MODIFY THE CLASS STATE

class Person:
	number_of_people = 0
	

	def __init__(self, name):
		self.name = name
		Person.number_of_people += 1  
		# remember to use Class.attribute

	@classmethod
	def get_number_of_people(cls):
		return cls.number_of_people

	@classmethod 
	def add_person(cls):
		cls.number_of_people += 1

	@staticmethod #cannot modify class state, only execute
	def print_greeting():
		print("hello world")
		 
p1 = Person("Tim")
p2 = Person("Jill")
print(Person.number_of_people)
Person.add_person()
print(Person.number_of_people)
Person.print_greeting()
