my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 #inches
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Acually, that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#This is the tricky part
print "If I add %d, %d, and %d, I get %d." % (my_age, my_height, my_weight, my_age+ my_height + my_weight)


#Exercise 1: Get rid of all "my_" && I also changed data to fit me
name = 'Andy Park'
age = 18
height = 68
weight = 160
eyes = 'Brown'
teeth = 'White'
hair = 'Black'
print ""
print "Exercise 1"
print "Let's talk about %r." % name
print "He's %r inches tall." % height
print "He's %d pounds heavy." % weight
print "Acually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "If I add %r, %r, and %r, I get %r." % (age, height, weight, age+ height + weight)
#Notes:
# 1 = 'Variable' is not valid ; all variales must start with characters
# %r is saying "print this no matter what"

#Exercise 4; Convert inches into cm, pounds into kg
print ""
print "Exercise 4"

name = 'Andy Park'
age = 18
height = 68
weight = 160
height_cm = (height*2.54)
weight_kg = (weight*0.454)
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %r." % name
print "He's %r cm tall." % (height_cm)
print "He's %d kg heavy." % (weight_kg)
print "Acually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "If I add %r, %d, and %s, I get %r." % (age, height_cm, weight_kg, age+ height_cm + weight_kg)
#Notes:
# %d is like int in C++
# %s appears to display the data as is