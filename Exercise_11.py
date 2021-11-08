# Exercise_11.py
#
# Uploaded by Aurimas A. Nausedas on 11/23/20.
# Updated by Aurimas A. Nausedas on 11/06/21.

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

colour = raw_input("What's your favourite colour? ")
print "So,you're %r old, %r tall and %r heavy. Your favourite colour is %r" % (
	age, height, weight, colour)
