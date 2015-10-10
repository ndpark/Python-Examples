# \n is basically like C++ it stands for "new line character"
# '\\' will printout one double slash
# Another important escape sequence is escaping a single quote or double quote.
# Ex) "I "understand" Joe"; "understand" ends the string
# So use single quote/ double quote 
# "I am 6'2\" tall." escape double-quote inside string
# 'I am 6'\2" tall.' escape single-quote inside string

tabby_cat = "\tI'm tabbing in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."


fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

#Study drill #2
studydrill = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print studydrill #This is exercise 2
print "This is an example from the text about inside and outside double/single quote"
print "\nI am 6'2\" tall" #Basically it's saying the quotation mark is quotation mark, not a operator
print '\nI am 6\'2" tall'
#Look at page 39 for all the escape sequences