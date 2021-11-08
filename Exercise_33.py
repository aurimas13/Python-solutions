# Solution of Exercise 33 - Exercise_33.py
#
# Uploaded by Aurimas A. Nausedas on 11/23/20.
# Updated by Aurimas A. Nausedas on 11/06/21.

i=0
numbers = [] #list in python
no = int(raw_input("limit number? "))
y = int(raw_input("Increment by how much? "))

#for i in range(0,no):

while i<no:
	print "At the top i is %d" % i
	numbers.append(i)

	i += y
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i 


print "The numbers: "

for num in numbers: 
	print num
