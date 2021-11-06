# Exercise_21.py
#
# Updated by Aurimas A. Nausedas on 11/06/21.

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
print "Let's do some math with just functions!"
age = add(30, 5)
height = subtract(78.0, 4.0)
weight = multiply(90, 2)
iq = divide(100.0, 2.0)

print "Age: %f, Height: %f, Weight: %f, IQ: %f" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = multiply(weight, add(age, divide(height, subtract(iq, 5.))))

print "That becomes: ", what, "Can you do it by hand?"
