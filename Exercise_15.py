# Exercise_15.py
#
# Uploaded by Aurimas A. Nausedas on 11/23/20.
# Updated by Aurimas A. Nausedas on 11/06/21.

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
