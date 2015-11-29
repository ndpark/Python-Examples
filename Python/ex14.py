"""Exercise 14: Prompting and Passing
Basic stuff like using inputs and stuff"""

from sys import argv

script, user_name = argv
prompt = 'Answer: ' #Prompt will be after this phrase

print "Hi %s, I'm the %s script" % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "Say swag"
swag = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
you are %r
 % (likes, lives, computer, swag)