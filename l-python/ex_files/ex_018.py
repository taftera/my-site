# Names, Variables, Code, Functions

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
# def = define - it's pythons way to start a function. Then we get " : " which indicates that everything indented will be in the funtion.

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Alex", "Bobanni")
print_two_again("Carla", "Danny")
print_one("Elmer!")
print_none()

# Study Drills
#
#  Everything is allowed in the name of a function :)
#  The " * " inside the (parenthesys) tells Python to take all the arguments to the function
