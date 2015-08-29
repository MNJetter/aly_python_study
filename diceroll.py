##################################################
## EXPERIMENT 001                               ##
## Objective: Create d20 dice roller            ##
## - Milestone 1 (single die, --------------OK! ## 
##               i.e., 1dn + 0)                 ##
## - Milestone 2 (single die modified, -----OK! ##
##               i.e., 1dn + n)                 ##
## - Milestone 3 (all variables open, --WORKING ## 
##               i.e., ndn + n)                 ##
##################################################
## (c) 2015 Aly Woolfrey                        ##
##################################################

# get a seed for "random" numbers
import random
random.seed()

##################################################
## ask the user how many dice they are rolling  ##
## MILESTONE IN PROGRESS---JUST NOTES FOR NOW   ##
## -  First get input to define multiplier.     ##
## -  Then figure out how to get that number of ##
##    dice... this part is extra hard because   ##
##    we're not just multiplying dice, like     ##
##    getting a d4 roll and tacking on a '* n'  ##
##    to the equation. We need to actually      ##
##    re-roll the die in question a number of   ##
##    times equal to the multiplier input       ##
##    value below. I'm sure it will end up      ##
##    being a loop of some sort...              ##
## -  Something will have to change in line 57  ##
##    ...but what?                              ##
##################################################

# ask the user about what kind of roll it is
mplr = int(raw_input("How many dice? >> "))
nmbr = int(raw_input("What kind of dice? >> d"))
mdfr = int(raw_input("What kind of modifier? >> "))

# roll the dice :)
roll = mdfr + random.randint(1, nmbr)

# display the result
print "You rolled a %d!" % roll
