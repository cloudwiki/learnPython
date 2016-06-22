__metaclass__ = type

class FooBar:
    def __init__(self):
        print "This is constructor of FooBar"
        self.somevar = 42
        
#    def __init__(self, somevar):
#        print "This is another constructor with parameter"
#        selft.somevar = somevar
        
foo = FooBar()
print foo.somevar

#bar = FooBar("hello")
#print bar.somevar
###Doesn't python support method override???