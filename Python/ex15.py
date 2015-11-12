#Use of argv to get the filename

from sys import argv

#Type in the name of the script then filename
script, filename = argv

txt = open(filename)

#Calling a function on txt 
print "Here is your file %r" %filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

#First part indicates which file to read, second part indicates the function