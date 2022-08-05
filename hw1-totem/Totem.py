"""
Created on 2/2/21

@author: Georgie Stammer
"""

import random

def part_hair_curly():
    """
    Returns a string that is curly hair & 2 lines tall
    """
    a  = r"012345678901234567"
    a  = r"  OOOOOOOOOOOOOO  " + "\n"
    a += r" OOOOOOOOOOOOOOOO "
    return a

def part_hair_spiky():
    """
    Returns a string that is spiky hair & 2 lines tall
    """
    a  = r"012345678901234567"
    a  = r"  /\ /\ /\ /\ /\  " + "\n"
    a += r" /\/\/\/\/\/\/\/\ "
    return a

def part_hair_straight():
    """
    Returns a string that is hair sticking up straight & 2 lines tall
    """
    a  = r"012345678901234567"
    a  = r"  ||||||||||||||  " + "\n"
    a += r" |||||||||||||||| "
    return a

def part_eyes_pretty():
    """
    Returns a string that is eyes with pretty eyelashes & 3 lines tall
    """
    a  = r"012345678901234567"
    a  = r" | \\__    __// | " + "\n"
    a += r" | \/ o\  / o\/ | " + "\n"
    a += r" |  |__|  |__|  | "
    return a

def part_eyes_sunglasses():
    """
    Returns a string that is cool sunglasses & 3 lines tall
    """
    a  = r"012345678901234567"
    a  = r" |______________| " + "\n"
    a += r" |-\   */\   */-| " + "\n"
    a += r" |  \__/  \__/  | "
    return a

def part_eyes_hearts():
    """
    Returns a string that is heart eyes & 3 lines tall
    """
    a  = r"012345678901234567"
    a  = r" | __ __  __ __ | " + "\n"
    a += r" | \ V /  \ V / | " + "\n"
    a += r" |  \_/    \_/  | "
    return a

def part_nose_freckles():
    """
    Returns a string that is a nose with freckles next to it & 2 lines tall
    """
    a  = r"012345678901234567"
    a  = r" |  ..      ..  | " + "\n"
    a += r" | ... /__\ ... | "
    return a

def part_nose_basic():
    """
    Returns a string that is a basic nose & 1 line tall
    """
    a = r"012345678901234567"
    a = r" |     /__\     | "
    return a

def part_nose_little():
    """
    Returns a string that is a little button nose & 1 line tall
    """
    a = r"012345678901234567"
    a = r" |     (..)     | "
    return a

def part_mouth_happy():
    """
    Returns a string that is an open smiling mouth & 4 lines tall
    """
    a  = r"012345678901234567"
    a  = r" |  __________  | " + "\n"
    a += r" |  \        /  | " + "\n"
    a += r" |   \______/   | " + "\n"
    a += r"  \____________/  "
    return a

def part_mouth_smirk():
    """
    Returns a string that is a sneaky smirking mouth & 2 lines tall
    """
    a  = r"012345678901234567"
    a  = r" |    _______/  | " + "\n"
    a += r"  \____________/  "
    return a

def part_mouth_sad():
    """
    Returns a string that is a sad frown & 3 lines tall
    """
    a  = r"012345678901234567"
    a  = r" |    ______    | " + "\n"
    a += r" |   /      \   | " + "\n"
    a += r"  \____________/  "
    return a




def younggirl_head():
    """
    Prints a head with curly hair, pretty eyes, freckles, and a smiling mouth
    """
    print(part_hair_curly())
    print(part_eyes_pretty())
    print(part_nose_freckles())
    print(part_mouth_happy())

def cooldude_head():
    """
    Prints a head with spiky hair, sunglasses, a basic nose, and a smirk
    """
    print(part_hair_spiky())
    print(part_eyes_sunglasses())
    print(part_nose_basic())
    print(part_mouth_smirk())

def heartbreak_head():
    """
    Prints a head with straight hair, heart eyes, a button nose, and a frown
    """
    print(part_hair_straight())
    print(part_eyes_hearts())
    print(part_nose_little())
    print(part_mouth_sad())




def head_with_eyes(eyefunc):
    """
    Prints a head with straight hair, a basic nose, a smile, and eyes given
    by eyefunc
    """
    print(part_hair_straight())
    print(eyefunc())
    print(part_nose_basic())
    print(part_mouth_happy())

def head_with_hair(hairfunc):
    """
    Prints a head with sunglasses, a basic nose, a smile, and hair given by
    hairfunc
    """
    print(hairfunc())
    print(part_eyes_sunglasses())
    print(part_nose_basic())
    print(part_mouth_happy())

def head_with_mouth(mouthfunc):
    """
    Prints a head with straight hair, sunglasses, a basic nose, and a mouth
    given by mouthfunc
    """
    print(part_hair_straight())
    print(part_eyes_sunglasses())
    print(part_nose_basic())
    print(mouthfunc())




def selfie_band():
    """
    Returns a string that is a 3 line tall selfie band
    """
    a  = r"012345678901234567"
    a  = r" +--------------+ " + "\n"
    a += r" |gss30    gss30| " + "\n"
    a += r" +--------------+ "
    return a

def selfie(eyefunc, mouthfunc):
    """
    Prints a head with a selfie band & eyes and mouth given in parameters
    """
    print(part_hair_straight())
    print(selfie_band())
    print(eyefunc())
    print(part_nose_basic())
    print(mouthfunc())

def head_random():
    """
    Generates 2 random numbers to print a random head w/ parameters that has a
    random part
    """
    x = random.randint(1, 3)
    y = random.randint(1, 3)
    if x == 1:
        eyefunc = part_eyes_hearts
        hairfunc = part_hair_straight
        mouthfunc = part_mouth_sad
    elif x == 2:
        eyefunc = part_eyes_sunglasses
        hairfunc = part_hair_spiky
        mouthfunc = part_mouth_smirk
    else:
        eyefunc = part_eyes_pretty
        hairfunc = part_hair_curly
        mouthfunc = part_mouth_happy

    if y == 1:
        head_with_eyes(eyefunc)
    elif y == 2:
        head_with_hair(hairfunc)
    else:
        head_with_mouth(mouthfunc)




def totem_fixed():
    """
    Calls 3 whole head functions w/o parameters to print 3 fixed heads
    """
    younggirl_head()
    cooldude_head()
    heartbreak_head()

def totem_selfie():
    """
    Calls the selfie helper function to print 3 heads with selfie bands
    """
    selfie(part_eyes_pretty, part_mouth_sad)
    selfie(part_eyes_sunglasses, part_mouth_happy)
    selfie(part_eyes_hearts, part_mouth_smirk)

def totem_random():
    """
    Calls the head_random helper function to print 3 heads, where each
    uses a different head w/ parameters function to randomized a feature.
    Results in one head w/ random eyes, one w/ random hair, and one w/ a
    random mouth
    """
    head_random()
    head_random()
    head_random()




if __name__ == '__main__':
    print("\nfixed totem\n")
    totem_fixed()

    print("\nself totem\n")
    totem_selfie()

    print("\nrandom totem\n")
    totem_random()

