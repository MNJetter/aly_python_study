name = 'Aly'
age = 32 # as of mid-2015
height = 65 # inches
weight = 220 # lbs
eyes = 'green'
teeth = 'white'
hair = 'blond'

height_cm = height * 2.54
weight_kg = weight / 2.2

print "Let's talk about %s." % name
print "She's %d inches tall." % height
print "She's %d pounds heavy." % weight
print "Yeah, she knows, that's pretty heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Outside the US, she's %s cm tall." % height_cm

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)
