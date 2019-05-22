# Even More Practice

##NOTE: However, this exercise is a little different. You won't be running it. Instead you will import it into Python and run the functions yourself.
##Terminal > type "python" > type "import ex_025" - No need for extension ".py"
##Inputs
##>>> sentence = "All good things come to those who wait."
##>>> words = ex_025.break_words(sentence)
##
##>>> sorted_words = ex_025.sort_words(words)
##>>> sorted_words
##
##>>> ex_025.print_first_word(words)
##
##>>> ex_025.print_last_word(words)
##
##>>> ex_025.print_first_and_last(sentence)
##
##>>> ex_025.print_first_and_last_sorted(sentence)


def break_words(stuff):
    """This function will break words for us."""
    words = stuff.split(' ')
    return words

def sorted_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prnts the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and the last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

#Study Drills
# 2.- Try: help(ex_025) > it displays the information like name, file path & functions along with the """documentation""".
# 2.- help(ex_025.break_words) > displays just the function selected.
# 3.- Can also use "from ex_025 import *"
