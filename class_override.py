__metaclass__ = type

#constructor is initializing method and it is called automatically after ojbect is created

#override constructor needs special attention than normal method(non-constructors)
#if you override the constructor of a class, you need to call the constructor of the superclass(the class you inherit from)
#otherwise, you risk having an object that isn't properly initialized

class Bird:
    def __init__(self):
        self.hungry = True
        
    def eat(self):
        if self.hungry:
            print 'Aaah...'
            self.hungry = False
        else:
            print 'No, thanks!'
            
            
class SongBird(Bird):
    def __init__(self):
        #super method is called with the current class and instance as its arguments, 
        #and any method you call on the returned object will be fetched from the superclass rather than the current class
        super(SongBird, self).__init()
        self.sound = 'Squawk!'
    def sing(self):
        print self.sound
        
        
      
        