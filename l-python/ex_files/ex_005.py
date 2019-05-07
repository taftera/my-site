# More Variables & Printing

my_name = 'Alex Turati'
my_age = 37
my_height = 69 # inches
my_weight = 156
my_eyes = 'Black'
my_teeth = 'Yellowish'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "Or", my_height / 12, "'", my_height % 12," I think."
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# Tricky part, lots of variables
print "If I add %d, %d and %d I get %d" % (my_age, my_height, my_weight, my_age + my_height + my_weight)
