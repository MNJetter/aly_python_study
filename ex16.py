# get argv module and tell the program which arguments are needed
from sys import argv
script, filename = argv

# prompt the user to accept or reject the file name they used in the argument
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# user gets to enter text here
raw_input("?")

# 'create' the file (open a previously nonexistant file) in write mode
print "Opening the file..."
target = open(filename, 'w')

#! truncate the file...not sure what that means...close it?
print "Truncating the file. Goodbye!"
target.truncate()

# give the user a heads-up about the lines to be asked for
print "Now I'm going to ask you for three lines."

# now ask for the lines
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# tell the user that the lines are going in the file
print "I'm going to write these to the file."

# put the lines in the file
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

#! study drill says to rewrite the above lines as one command. The following are ideas that didn't work.
#! target.write("%s \n %s \n %s \n") % (line1, line2, line3)
#! target.write("%r \n %r \n %r \n") % (line1, line2, line3)
#! target.write(line1, "\n", line2, "\n", line3, "\n")
#! target.write("%r%r%r") % (line1, line2, line3)
target.write()

# close the file---good habit.
print "And finally, we close it."
target.close()
