print "How old are you",
age = raw_input()
print "How tall are you",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r years old, %r inches tall, and %r kilograms heavy" % (age, height, weight)
# Commas are used so that print doesn't end the line with new line character and go to the next line

# raw_input () will not catch user error kinda similar to %r but not really
# input () will be read by the program as if it were code 
# When the inputs were: 38, 6'2" , and 180 lbs
# The output: So you're '38' old, '6\'8"' tall, and '180lbs' heavy
# \n is there becasue the ' after 6 is interpreted as \n due to escape sequences 
# if it wasn't changed it would simply end the string after 6
print "How swag are you",
swag = raw_input()

print "Dawg, you are %r swag??? Sick yo!" % swag

#Let's test input out 
print "Please enter something with an apostrophy in there",
test = input()
#Stops here if i put something with ' in there
print "This will show as %r" % test

