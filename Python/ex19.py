#Exercise 19: Functions and Variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %s cheeses!" % cheese_count
	print "You have %s boxes of crackers" % boxes_of_crackers
	print "That's enough for a party!"
	print "Get a blanket?? Idk what this means"
	
print "\nWe can just give the function numbers directly"
cheese_and_crackers(20,30)

print "\nOr use variables"
numberCheese = 10
numberBoxes = 20 
cheese_and_crackers(numberCheese,numberBoxes)

print "\nOperations are possible within functions as well"
cheese_and_crackers(10+5, 20-7)

print "\nWe can combine the two -- variables AND math!!!!"
cheese_and_crackers(numberCheese+200000,numberBoxes-6001231)

print "\nPlease input number of cheese & boxes of crackers"
cheeseNumber = raw_input("How many cheese you got? ")
boxNumber = raw_input("How many crackas you got ? ")
cheese_and_crackers(cheeseNumber,boxNumber)

"""
What I learned: 
Use %s instead of %s because %s is more broad
All similar to C++!
"""
