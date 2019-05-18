# More variables and printing

# My variables
my_name = 'Alex Turati'
my_age = 37
my_height = 69
my_weight = 145
my_eyes = 'Brown'
my_teeth = 'Yellowish'
my_hair = 'Black'

# Printing in-line
print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
# doing the division
print "Or ", my_height / 12, "' ", my_height % 12, " inches"

print "He's %d pounds heavy." % my_weight
print "Actually that's not to heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
