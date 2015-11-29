"""Exercise 20: Functions and files
Practice using different functions"""

from sys import argv

#Imports these stuff 
script, input_file = argv

#Function declaration. f means file -  it will go to the start of each file at the beginning
# Ergo, this function starts reading the file from the beginning
def print_all(f):
	print f.read()

#This function looks starts at the beginning. 'seek' looks at the byte size 
def rewind(f):
	f.seek(0)

#This function will print the line number and then print the actual content of the line
def print_a_line(line_count, f):
	print line_count, f.readline()

#Assigns what is within input_file to current_file (Basically makes it readable by program)
current_file = open(input_file)

print "Let's print the whole file: \n"

print_all(current_file)

print "\nNow let's rewind, kind of like a tape"

rewind(current_file)

print "\nLet's print three lines"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)