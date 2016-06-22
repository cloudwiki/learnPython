"color module"
    
def getColor(colorName='red'):
    print "get color", colorName
    return colorName
    
def getRGBColor(r=50, g=50, b=50):
    print "get RGB edges : ", (r, g, b)
    return "RGB(%d,%d,%d)" % (r, g, b)
    