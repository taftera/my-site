# Asking Questions

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

# By adding a " , " after each print, it allows to be answered in-line.
# raw_input, presents a prompt to the user.

print "So you're %r old, %r tall and %r heavy." % (age, height, weight)
