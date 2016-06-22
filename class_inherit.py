__metaclass__ = type

class Person:

	def setName(self, name):
		self.name = name
		
	def getName(self):
		return self.name
		
	def greet(self):
		print "hello, world! I'm %s." % self.name
		

class Student(Person):
    def setScore(self, score):
        self.score = score
        
    def getScore(self):
        return self.score
        
        
stu = Student()
stu.setName('stu1');
stu.greet()

stu.setScore(100)
print stu.getScore()