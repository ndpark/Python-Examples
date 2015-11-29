"""Exercise 8: Printing. Printing
This exercise focuses on priting using strings"""

formatter = "%r %r %r %r" #Formatter 'formats' patterns

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True) #Quotes around True, False would make it into strings
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right,",
	"But it didn't sing.",
	"So I said goodnight."
)

# You should always use %s and  %r only for debugging (representation)
#
