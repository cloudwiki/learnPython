alphaNums = [1,'a','b','c','world', 2,3,4,'hehe',7,'haha',1001]

print alphaNums

print "cast all to string"
str_alphaNums = map(str, alphaNums)
print str_alphaNums
print "find all numeric values:"

def isnum(x):
    return isinstance(x,int)
    
print filter(isnum, alphaNums)

print "find all string values:"

def isstr(x):
    return isinstance(x,str)
    
print filter(isstr, alphaNums)

print "find all string with 4 characters:"
def lenEQ(x):
    return isinstance(x,str) and len(x) == 4
    
print filter(lenEQ, alphaNums)
