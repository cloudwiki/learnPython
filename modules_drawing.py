import drawing
import drawing.shape
import drawing.color

drawing.getCanvas()
line = drawing.shape.getLine()
drawing.insertShape(line)

triangle = drawing.shape.getTriangle(5,5,5)
color = drawing.color.getColor('yellow')
drawing.insertShape(triangle)
drawing.fillColor(color)

retangle = drawing.shape.getRetangle()
color = drawing.color.getRGBColor(45,35,125)
drawing.insertShape(retangle)
drawing.fillColor(color)