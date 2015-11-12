from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C"
print "If you do want that, hit RETURN"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
#'w' is needed to truncate, and to rwrite 

print "Truncating the file..."
target.truncate()

print "Now I will ask for three lines"
line1 = raw_input("line1:" )
line2 = raw_input("line2:")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

# The plus sign adds these together
line5=line1+"\n"+line2+"\n"+line3
target.write(line5)


print "And finally, we close it."
target.close()