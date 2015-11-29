"""Exercise 25: Even more practice
This uses the actual python program to run

- use return when you want the function to return a value 
- use "from ex25 import *" so you dont have to type ex25 everytime
- use help(ex25) if ya boy need help
- ctrl c to go back 

"""


def break_words(stuff):
	"""This function will break up words for us.
	This function will split whatever sentence we put into words --> the ' ' will act as a signal"""
	words = stuff.split(' ')
	return words
	
def sort_words(words):
	"""Sorts the words inputted by the function above into an alphabetical order"""
	return sorted(words)
	
def print_first_word(words):
	"""Prints the first word after 'popping' it off."""
	word = words.pop(0)
	print word
	
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word
	
def sort_sentence(sentence):
	"""Takes a full sentence, break it into words, then returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last (sentence):
	"""Prints the first and last words of the sentence"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the firs and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
