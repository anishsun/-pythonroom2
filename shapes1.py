import turtle

anish = turtle.Turtle()

sides = 8
length = 40
angle = 180 -180 * ( sides - 2 ) / sides

numbers = range(0, sides)

for numbers in numbers:
	anish.forward(length)
	anish.left(angle)
