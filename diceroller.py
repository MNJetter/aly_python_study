##################################################
## Begin DICEROLLER.                            ##
##################################################
## This script is a d20-style dice roller. It   ##
## requires the user to input numbers for a     ##
## multiplier, dice type, and modifier, and     ##
## displays relevant information on the screen, ##
## including the result of each roll.           ##
##################################################
## (c) 2015 Aly Woolfrey                        ##
##################################################

import random

random.seed()

rollnums = []

def roll_the_dice(d_mult, d_type, d_mod):
    print "Rolling %dd%d + %d." % (d_mult, d_type, d_mod)
    while d_mult > 0:
        rollnums.append(random.randint(1, d_type))
        d_mult -= 1
    totalroll = sum(rollnums)
    print "Your raw rolls are: %s" % (rollnums)
    print "Your total unmodified roll is: %d" % (totalroll)
    print "Your final number is %d" % (totalroll + d_mod)

mult_num = int(raw_input("Input multiplier (_DX + X): "))
type_num = int(raw_input("Input dice type (XD_ + X): "))
mod_num = int(raw_input("Input your modifier. Type 0 if there is no modifier. (XDX + _): "))
roll_the_dice(mult_num, type_num, mod_num)

##################################################
## End DICEROLLER.                              ##
##################################################
