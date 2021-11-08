# Exercise_17.py
#
# Uploaded by Aurimas A. Nausedas on 11/23/20.
# Updated by Aurimas A. Nausedas on 11/06/21.

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copying from %s to %s") % (from_file, to_file)

#we could do these two on one line too, how?
#indata = open(from_file).read()

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

open(to_file, 'w').write(open(from_file).read())

print "Alright, all done."

#out_file.close()
#in_file.close()
