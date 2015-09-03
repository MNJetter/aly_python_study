from sys import argv
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

#! truncate the file...not sure what that means...close it? My best guess is that it essentially erases any existing information on the file so the rest of the program can run as a "new" file.
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# These are the original target.write() commands. As part of the study drills, I rewrote them. See below.
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# study drill said to rewrite the above lines as one command. The following are ideas that didn't work, just so that I can remember what I did wrong...
# attempt 1 --> target.write("%s \n %s \n %s \n") % (line1, line2, line3)
# attempt 2 --> target.write("%r \n %r \n %r \n") % (line1, line2, line3)
# attempt 3 --> target.write(line1, "\n", line2, "\n", line3, "\n")
# attempt 4 --> target.write("%r%r%r") % (line1, line2, line3)
# attempt 5 --> target.write("%r \n %r \n %r \n") % line1, line2, line3
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we close it."
target.close()
