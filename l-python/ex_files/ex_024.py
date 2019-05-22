# More Practice

print "Let's practce everything."
print "You\'d need to know \'bout escapes \\ that do \n newlines and \t tabs."

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requiere an explanation
\n\t\twhere there is none.
"""

print "------------"
print poem
print "------------"

five = 10 - 2 + 3 - 6
print "This should be five %s " % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)
#Why does he pulls out the variables before starting the Function ???
#If variables are errased the next print doesn't really works,
#When equalled to 0... the function doesn't updates the values, even if the formula has a starting value entered.

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, %d crates." % secret_formula(start_point)
