# Parameters, Unpacking, Variables

from sys import argv
# IMPORT = Python ask what you "plan to use"
# argv = ARGumented Variable (standard name in programming)
# These are MODULES that gives "features"

# Study Drill - combine with raw_input
fourth = raw_input("What's your fourth variable?")

script, first, second, third = argv
# Why can't I add the fourth varible up there ?

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth

# To run the program, you gotta add the 3 variables
# ex:
# $ python ex_013.py first 2nd 3rd.
# Being "first 2nd 3rd" the variables being printed.
# If there's not enough values, this message will display: "ValueError: need more than 3 values to unpack"

# Note:
# - Command line arguments (argv) are considered "strings"
