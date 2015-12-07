"""Exercise 33: While- loops 
Practice using while loops"""

max = 0 ;

max =raw_input('>>')
def countup(max):
	i = 0
	numbers = []
	max =raw_input('>>')
	
	while i < max:
		print "At the top i is %d" %i
		numbers.append(i)
		
		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
		
	print "The numbers: "
	for num in numbers:
		print num

countup()

	
