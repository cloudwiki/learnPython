#Any python programs you saved in a file can be imported as a module
#when you imported a module foo.py, it will be translated to a format that python can handle more efficiently.(.pyc)
#when you import the same module again, python will import the .pyc file unless the .py has changed
#modules are executed the first time they are imported into your program.
#Eventhough you can import any program as a module, but module is meant to define things rather than do things(such as printing text).


#'__main__' is the name of the scope in which top-level code executes. 
#A module's __name__ is set equal to '__main__' when read from standard input, a script, or from an interactive prompt.
#When the module file is imported form another module, __name__ will be set to the module's name
#or put it another way: if the python interpreter is running the module(soucre file) as the main program, it set __name__ to __main.
# if the file is being imported from another module, __name__ will be set to the module's name

def hello():
    print "hello, world"
    
def test():
    print "start testing..."
    hello()
#the following block is ignored, when the module is imported from other modules, because it's  not the main program    
if __name__ == '__main__': test() #if the module is running as the main program in python interpreter.


