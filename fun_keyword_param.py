print "demo for keyword parameters"

def hello(greeting, name):
    'hello function with keyword parameters'
    print greeting, ",", name
   
def hello_2(name, greeting="hi"):
    'hello function with keyword parameters and default values'
    print greeting, ",", name   

def hello_3(greeting, *names):
    'hello function with unlimited parameters'
    print greeting, names

def hello_4(greeting, *names, **keyParams):
    'hello function with unlimited parameters & keyword params'
    print greeting, names, keyParams
    
    
print "position parameters:"
hello('hi', 'sam')

print "keyword parameters:"
hello(greeting='hi', name='sam')
hello(name='sam', greeting='hi')

print "demo for keyword parameters and default values"
hello_2(name="sam")

print 'hello function with unlimited parameters'

hello_3('hello', 'sam','jack','tom')


print 'hello function with unlimited parameters & keyword params'

hello_4('hello', 'sam','jack','tom', keyParams='Nice to meet you.')