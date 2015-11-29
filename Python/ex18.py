"""Exercise 18: Names, Variables, Code, Functions
How to declare functions



Multi line string can be used as multi- line comments!
Functions do three things
1. Name pieces of code the way variables name strings and numbers
2. Take arguments the way scripts take argv
3. Use 1 and 2 to make mini scripts
"""
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1,arg2)
	
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" % (arg1,arg2)
	
def print_one(arg1):
	print "arg1: %r" % (arg1)
	
def print_none ():
	print " Nothing!"
	
print_two("Hello", "It's me")
print_two_again("Hello", "It's me")
print_one("Hello from the other side")
print_none()

"""
How to declare a function:
1. Use def say you are declaring a function
2. Give it a name, then put what is being input into function within ()
3. DON'T FORGET ':'
4. In python, parameter of funtion depends on spacing.
For example,
	swag
	is seperate from
		swag
This is pretty cool
5. After :, just declare it like you would in C++