from sys import argv #IMPORT will add features (modules) from Python modules set

#script, first, second, third = argv #'unpacks and assigns' argv to four variables

#print "The script is called:", script
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third

#You must run the program and type the arguments in
#Ex) python ex13.py 1 2 3
#If I plug in three arguments then the fitsy onr isn't shown


#Study drils 
#1 - When less than 3 inputs, displays: need more than 3 values to unpack

#2 - Fewer/ more arguments

#3 add raw input to argv

script, first, second, third, fourth = argv
print "script?",script
print "first", first
print "second", second
print "third", third
print "fourth", fourth

print "Write down some random stuff and it'll print the first one"
script = raw_input()
first = raw_input()
second = raw_input()
third = raw_input()
fourth = raw_input()

#Printing first script 
print script 