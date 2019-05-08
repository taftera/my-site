# Prompting and Passing - argv & raw_input

from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s" % user_name
likes = raw_input(prompt)
# By adding the variable "prompt" inside the (parenthesys),
# it displays it's content allowing to have a "> " before every required answer

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have %r computer. Nice.
""" % (likes, lives, computer)

# Study Drills
# - Find out what Zork and Adventure is - hmm? > https://github.com/iamjawa/zork-py
