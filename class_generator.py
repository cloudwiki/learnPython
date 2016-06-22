__metaclass__ = type
#A generator is a kind of iterator that is defined with normal function syntax
#Any function that contains a yield statement is
#called a generator. And it's not just a matter of naming; it will behave quite differently from
#ordinary functions. The difference is that instead of returning one value, as you do with return,
#you can yield several values, one at a time. Each time a value is yielded (with yield), the function
#freezes; that is, it stops its execution at exactly that point and waits to be reawakened.
#When it is, it resumes its execution at the point where it stopped
nested = [[1,2], [3,4], [5]]

#iterate over all the element
def flatten(nested):
    '''Version 1 can only handle two level list(two nested for loop)'''
    for sublist in nested:
        for element in sublist:
            yield element
            
            

print list(flatten(nested))

#help(flatten)

#recursive generator
deeply_nested = [[[1],2],3,4,[5,[6,7]],8,[[[[[[[[[9]]]]]]]]]]


def flatten2(nested):
    '''Version 2 can handle arbitrary levels list using recursive.
e.g. [[[1],2],3,4,[5,[6,7]],8]
    '''
    try:
        for sublist in nested:
            for element in flatten2(sublist):
                yield element
    except TypeError as e:
        yield nested
        


print list(flatten2(deeply_nested))        


#recursive generator avoid str iter
deeply_nested_str = ['foo', ['bar', ['baz']], 1, 'test']


def flatten3(nested):
    '''Version 3 can handle arbitrary levels list using recursive. and ignore iter on str object
e.g. [[[1],2],3,4,[5,[6,7]],8]
    '''
    try:
        try:
            nested + '' #test whether nested is a string
        except TypeError as e: #if nested is not a string, then iterator over it
            pass
        else:  # if nested is an string, return directly
            raise TypeError
        
        for sublist in nested:
            for element in flatten3(sublist):
                yield element        
    except TypeError as e:
        yield nested
        
#print flatten3 function itself
#print flatten3(deeply_nested_str) return object(generator)
print flatten3(deeply_nested_str).next()
print list(flatten3(deeply_nested_str))      



#generator communication to the outside world
def greetting(name):
    while True:
        person = (yield name)
        if person is not None: name = 'hello, ' + person
        
        
print greetting(None).next()
print greetting('sam').next()

g = greetting('test')
print g.next()
print g.next()
g.send('testA')
print g.next()
print g.next()

#greet = greeting()



        
            