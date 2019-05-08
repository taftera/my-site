# Reading Files

from sys import argv

script, filename = argv
# we ask for the file location with "filename" variable

txt = open(filename)
# open() = "opens" the file sent, don't know if I could send it an URL

print "Here's your file %r" % filename
print txt.read()
# By read() = it "displays" the variable

txt.close()
# By close() = it terminates the process of reading the desired file.

print "Type the filename again:"
file_again = raw_input("> ")
# File prompt to target desired file.

txt_again = open(file_again)

print txt_again.read()

txt_again.close()

# Study Drills
# Couldn't find this...
# Run pydoc file and scroll down until you see the read() command (method/function). See all the other ones you can use? Skip the ones that have __ (two underscores) in front because those are junk. Try some of the other commands.
