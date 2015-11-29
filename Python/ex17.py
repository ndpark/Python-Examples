"""Exercise 17: More files
Copies content of one file to another:
Key functions :open(), read(), close()
"""


#This program copies one file to another

#Imports arguments
from sys import argv
#Imports function exists, which checks if a file exists, from os.path
from os.path import exists

#Declaring arguments
script, from_file, to_file = argv

#Copying one file to another file
print "Copying from %s to %s" % (from_file,to_file)

#Opens from_file and assigns it to in_file
#Assigns what is inside in_file to indata
#(;) ends a line
in_file = open(from_file); indata = in_file.read()

#When I did indata = open(from_file).read(), i didn't have to include close since
#it closes on its own

#Using length function to return how many characters there are
print "The input file is %d bytes long" % len(indata)

#Exists function check whethere or not the file exists
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input(">>")

#Opens to_file in write mode so it can edit
out_file = open(to_file, 'w')

#Write the content of indata (which is the content of to_file) to out_file
out_file.write(indata)

print "Alright, all done."

#Close each file and saves it
out_file.close()
in_file.close()


#Things to do :
# What is import statement
# what is cat 
# Why do i need output.close 