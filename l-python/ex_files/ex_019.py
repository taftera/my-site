# Functions and Variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blacket.\n"
# def = function that prints out the variables inputed in the (parenthesys)

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)
# This way the function, gets inputed numbers as a keys.

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# This way the function, gets inputed variables as keys

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
# As long as a " , " separates the categories you can do math with it.

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# Combined with variables

# raw_input prompt - remember to create integers as an input
cc = int(raw_input("How many cheese slices do you have?"))
boc = int(raw_input("How many boxes of crackers do you have?"))
cheese_and_crackers(cc, boc)


# For functions, we can input several type of different variables.
#  Numbres
#  Variables
#  Do Math
#  Combine it
