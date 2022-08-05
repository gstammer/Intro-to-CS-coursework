"""
Created on 3/17/21

@author: Georgie Stammer
"""

shift = 3
lower_alph = "abcdefghijklmnopqrstuvwxyz"
upper_alph = lower_alph.upper()
shifted_lower = lower_alph[3:] + lower_alph[:3]
shifted_upper = upper_alph[3:] + upper_alph[:3]

def encrypt(word):
    """
    returns word encrypted with a caesar cipher
    """
    global shift
    global lower_alph
    global upper_alph
    global shifted_lower
    global shifted_upper
    new = ""
    for ch in word:
        if ch in lower_alph:
            dex = lower_alph.index(ch)
            new += shifted_lower[dex]
        elif ch in upper_alph:
            dex = upper_alph.index(ch)
            new += shifted_upper[dex]
        else:
            new += ch
    return new

def setShift(x):
    """
    alters global variables to set the shift for future caesar cipher encryption
    """
    global shift
    global lower_alph
    global upper_alph
    global shifted_lower
    global shifted_upper
    shift = x
    shifted_lower = lower_alph[x:] + lower_alph[:x]
    shifted_upper = upper_alph[x:] + upper_alph[:x]

def findShift(string):
    """
    tests each possible caesar cipher shift & returns the shift that was
    used to encrypt string (determined by which produces the most real words)
    """
    import os.path
    file = os.path.join("data", "lowerwords.txt")
    f = open(file)
    wordsClean = [w.strip() for w in f.read().split()]
    matches = []
    if " " in string:
        string = string.split()
    else:
        string = [string]
    for x in range(26):
        setShift(x)
        shifted = [encrypt(word).lower() for word in string]
        count = len(set(shifted) & set(wordsClean))
        matches.append(count)
    best = max(matches)
    return 26 - matches.index(best)

if __name__ == '__main__':

    print(encrypt("Hat"))
    print(encrypt("abcABC"))

    setShift(10)
    print(encrypt("Hat"))
    print(encrypt("abcABC"))

    setShift(1)
    print(encrypt("hi my name is"))
    print(encrypt("abcABC"))

    print(findShift("ibu"))
    print(findShift("ij nz obnf jt"))
    print(findShift("Zkdw grhv wkh ira vdb?"))

    setShift(26 - findShift("Zkdw grhv wkh ira vdb?"))
    print(encrypt("Zkdw grhv wkh ira vdb?"))

    setShift(26 - findShift("Lzw Fglgjagmk Bmehafy Xjgy gx Usdsnwjsk Ugmflq"))
    print(encrypt("Lzw Fglgjagmk Bmehafy Xjgy gx Usdsnwjsk Ugmflq"))