#Exercise 1 : Comment on everything

# This string changes %d with the number 10, making it display that number
x = "There are many %d types of people." % 10
# Variable binary will simply display "binary"
binary = "binary"
# Variable "do_not" will simply display "don't"
do_not = "don't"
# The y will display this sentence below, but with binary and do_not 
y = "Those who know %s and those who %s." % (binary, do_not)

#This will print the modified variables x and y
print x
print y

#These will reiterate what is said above, but in a bigger string
print "I said: %r." % x
print "I also said: '%s.' " % y

#This is a taste of bool // or just means False
hilarious = False
#This variable has %r embedded in it therefore needs one when you want to display this sentence
joke_evaluation = "Isn't that joke so funny?! %r"

# This will print joke evaluation but with hilarious since that is the formatter
print joke_evaluation % hilarious

#Notes:
#"TypeError: not all arguments converted during string formatting" means that there is more % formatters in the strings than the variables
# %r is used for debugging purposes since it displayed raw data


w = "This is the left side of..."
e = "a string with a right side."

# This is adding two stirngs together
print w + e