# Reading and Writing Files

from sys import argv

script, filename = argv

print "We're goint to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do what that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
# Open arguments
#
# r  = READ Open text file for reading.
# r+ = READ Open for reading and writing.
# w  = WRITE Truncate file to zero length or create a text file for writing.
# w+ = WRITE Open for reading and writing. The file is created if it does not exists, otherwise it is truncated.
# a  = APPEND Open for writing. > The stream is positioned at the end of the file. <
# a+ = APPEND Open for reading and writing. > The stream is positioned at the end of the file. <


print "Truncating teh file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1 + "\n")
target.write(line2 + "\n")
target.write(line3 + "\n")
# By adding " + " you can concatenate information in a single line of code.

print "And finally, we close it."
target.close()
