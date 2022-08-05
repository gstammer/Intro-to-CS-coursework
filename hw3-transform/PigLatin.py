"""
Created on 3/17/21

@author: Georgie Stammer
"""

def isVowel(ch):
    """
    returns True if ch is a vowel and False otherwise
    """
    return "aeiouAEIOU".count(ch) > 0

def encrypt(word):
    """
    returns a string that is word in pig latin form
    """
    if isVowel(word[0]):
        return word + "-way"
    elif word[0] == "q" or word[0] == "Q":
        ch = 2
        while ch < len(word) and (not isVowel(word[ch])):
            ch += 1
        if ch == len(word):
            return word[2:] + "-" + word[:2] + "ay"
        else:
            return word[ch:] + "-" + word[:ch] + "ay"
    else:
        ch = 1
        while ch < len(word) and (not isVowel(word[ch]) and word[ch] != "y"):
            ch += 1
        if ch == len(word):
            return word + "-way"
        else:
            return word[ch:] + "-" + word[:ch] + "ay"

def decrypt(word):
    """
    returns the normal version of a word given in pig latin
    """
    if word[-4:] == "-way":
        return word[:-4]
    else:
        x = word.rfind("-")
        start = word[x + 1:-2]
        end = word[:x]
        return start + end

if __name__ == '__main__':

    print(encrypt("hello"))
    print(encrypt("ello"))
    print(encrypt("quiz"))
    print(encrypt("zzzz"))
    print(encrypt("qurrr"))
    print(encrypt("quran"))
    print(encrypt("i"))
    print(encrypt("myth"))
    print(encrypt("yay"))
    print(encrypt("strength"))
    print(encrypt("HELLO"))

    print(decrypt(encrypt("hello")))
    print(decrypt(encrypt("ello")))
    print(decrypt(encrypt("quiz")))
    print(decrypt(encrypt("zzzz")))
    print(decrypt(encrypt("qurrr")))
    print(decrypt(encrypt("quran")))
    print(decrypt(encrypt("i")))
    print(decrypt(encrypt("myth")))
    print(decrypt(encrypt("yay")))
    print(decrypt(encrypt("strength")))
    print(decrypt(encrypt("HELLO")))
    print(decrypt(encrypt("good-natured")))