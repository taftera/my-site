# Functions and Files

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()
#read() = reads and prints the targeted file

def rewind(f):
    print f.seek(0)
#seek() = opens a file and starts reading from the current position inserted from the variable.
#seek deals with bytes, not lines.

def print_a_line(line_count, f):
    print line_count, f.readline()
#readline = the line from the file and moving ahead to the right after the " \n "

current_file = open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape"
rewind(current_file)
#rewind = goes back to the start of the file since it's targeted to 0

print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)
#current_line: selects a line to be printed
#current_line = 1
current_line = current_line + 1
print_a_line(current_line, current_file)
#current_line = 2
current_line = current_line + 1
print_a_line(current_line, current_file)
#current_line = 3
