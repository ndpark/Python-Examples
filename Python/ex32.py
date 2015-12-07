"""Exercise 32: Loops and Lists
Practice using making lists and using for loops
Exercises 29-31 were omitted"""

the_count = [1,2,3,4,5]
fruits =['apples','bananas','pears','apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#Goes through a list
#For loop declares a variable, number, and assigns the values of the_count to it, then print
for number in the_count:
	print "This is count %d" % number
	
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
#using %r since variable type is unknown
for i in change:
	print "I got %r" % i
	
#How to build lists:

elements = []

#Range goes from i -> j-1 for (i,j)
for i in range(0,6):
	print "Adding %d to the list" %i
	elements.append(i)
	
for i in elements:
	print "Element was : %d" %i
	
#To make a 2D list:
#[[1,2,3],[1,2,3]]
