"shape module"
    
def getLine(width=50):
    print "get line with width: ", width
    return "-"*width
    
def getTriangle(m=50, n=50, l=50):
    print "get triangle edges : ", (m,n,l)
    return "Triangle(%d, %d, %d)" % (m, n, l)
    
def getRetangle(length=50, width=30):
    print "get retangle with edges : ", (length, width)
    return "Retangle(%d, %d)" % (length, width)
     
    
    