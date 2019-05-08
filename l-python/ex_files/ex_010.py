# What was that ? - the use of backslash in formatting of "Escape Sequences"

tabby_cat = "\tI'm tabbed in."
# \t = tab
persian_cat = "I'm split\non a line."
# \n = enter
backslash_cat = "I'm \\ a \\ cat."
# \\ = just single backlash

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

##
# ESCAPE SEQUENCES
# ==================
# \\            Backslash (\)
# \'            Single- quote (')
# \"            Double- quote (")
# \a            ASCII bell (BEL)
# \b            ASCII backspace (BS)
# \f            ASCII formfeed (FF)
# \n            ASCII linefeed (LF)
# \N            {name}Character named name in the Unicode database (Unicode only)
# \r            ASCII carriage return (CR)
# \t            ASCII horizontal tab (TAB)
# \uxxxx        Character with 16- bit hex value xxxx (Unicode only)
# \Uxxxxxxxx    Character with 32- bit hex value xxxxxxxx (Unicode only)
# \v            ASCII vertical tab (VT)
# \ooo          Character with octal value oo
# \xhh          Character with hex value hh
##

print "Try out code: "
while True:
  for i in ["/","- ","|","\\","|"]:
    print "%s\r" % i,
# It just cycles through the bars to make like a "loading" gif
