__metaclass__ = type

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
        
    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
        
    def __iter__(self):
        return self
        
#############################
fib = Fibs()
print fib.next()
print fib.next()
print fib.next()
print fib.next()
print fib.next()
print fib.next()

fib_list = Fibs()

print [fib_list.next() for x in range(1,10)]


#create iterator from an iterable object(list)
iter_from_list = iter([1,2,3,4,5,6,7,8])
print iter_from_list.next()
print iter_from_list.next()
print iter_from_list.next()
print iter_from_list.next()
print iter_from_list.next()
print iter_from_list.next()
print iter_from_list.next()
print iter_from_list.next()


#make sequences from iterators
#fibonacci number with upper limit
class Fibs_With_Limit:
    def __init__(self, max):
        self.a = 0
        self.b = 1
        self.max = max
        
    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if (self.a > self.max): raise StopIteration
        return self.a
        
    def __iter__(self):
        return self

fib_limit = Fibs_With_Limit(20) 
print "generate fibonacci seq less than: ", fib_limit.max
print list(fib_limit)
