__metaclass__ = type

class Person:

	def setName(self, name):
		self.name = name
		
	def getName(self):
		return self.name
		
	def greet(self):
		print "hello, world! I'm %s." % self.name
		
		
		
		
foo = Person()

bar = Person()

foo.setName('Sam')
bar.setName('Jack')
foo.greet()

bar.greet()