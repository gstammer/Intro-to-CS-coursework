"""
Created on 4/6/21

@author: Georgie Stammer
"""


import random


def handleUserInputDebugMode():
    """
    Asks the user if they want debug mode of play mode
    returns True for debug & False for play
    """
    mode = input("Which mode do you want: (d)ebug or (p)lay: ")
    if mode == "d":
        return True
    if mode == "p":
        return False




def handleUserInputWordLength():
    """
    Asks the user how many letters in the word they'll guess & returns it as
    an integer
    """
    length = input("How many letters in the word you'll guess: ")
    return int(length)




#keep same
def handleUserInputDifficulty():
    '''
    This function asks the user if they would like to play the game in (h)ard or (e)asy mode, then returns the
    corresponding number of misses allowed for the game.
    '''
    print("How many misses do you want? Hard has 8 and Easy has 12.")
    dif = input("(h)ard or (e)asy> ")
    if dif == "h":
        return 8
    elif dif == "e":
        return 12




def createTemplate(currTemplate, letterGuess, word):
    """
    returns a new word template based on if the letter guessed is in the secret
    word
    """
    template = list(currTemplate)
    for index in range(len(word)):
        if word[index] == letterGuess:
            template[index] = letterGuess
    newtemplate = "".join(template)
    return newtemplate




def getNewWordList(currTemplate, letterGuess, wordList, debug):
    """
    returns a tuple with a new template & a possible word list based on which
    template has the most possible corresponding words
    """
    d = {}
    for word in wordList:
        temp = createTemplate(currTemplate, letterGuess, word)
        if temp not in d:
            d[temp] = []
        d[temp] = d[temp] + [word]
    if debug:
        dsort = sorted([item for item in d.items()])
        for item in dsort:
            print(item[0] + " : " + str(len(item[1])))
        print("# keys = " + str(len(dsort)))
    choosetemp = list(d.keys())[0]
    chooselist = d[choosetemp]
    underscores = choosetemp.count("_")
    numwords = len(chooselist)
    for key in d.keys():
        newnumwords = len(d[key])
        if newnumwords > numwords:
            chooselist = d[key]
            choosetemp = key
            numwords = newnumwords
            underscores = key.count("_")
        elif newnumwords == numwords:
            newunderscores = key.count("_")
            if newunderscores > underscores:
                chooselist = d[key]
                choosetemp = key
                numwords = newnumwords
                underscores = key.count("_")
    ret = (choosetemp, chooselist)
    return ret




def createDisplayString(lettersGuessed, missesLeft, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    for index in range(len(alpha)):
        if alpha[index] in lettersGuessed:
            alpha[index] = " "
    alpha = "".join(alpha)
    mis = str(missesLeft)
    word = " ".join(hangmanWord)
    x = "letters not yet guessed: " + alpha + "\nmisses remaining = " +\
        mis + "\n" + word
    return x




def processUserGuessClever(guessedLetter, hangmanWord, missesLeft):
    """
    returns a list with the new # of misses remaining & a bool for if the user's
    guess was correct
    """
    if guessedLetter in hangmanWord:
        newmisses = missesLeft
        correct = True
    else:
        newmisses = missesLeft - 1
        correct = False
    return [newmisses, correct]




#keep same
def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''
    let = input("letter> ")
    while let in lettersGuessed:
        print("you already guessed that")
        let = input("letter> ")
    return let




def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''
    f = open(filename, 'r')
    allwords = []
    for line in f:
        allwords.append(line.strip())
    debug = handleUserInputDebugMode()
    length = handleUserInputWordLength()
    words = [x for x in allwords if len(x) == length]
    missesLeft = handleUserInputDifficulty()
    print()
    missStart = missesLeft
    secretWord = words[random.randrange(0, len(words))]
    hangmanWord = []
    for x in range(length):
        hangmanWord.append("_")
    lettersGuessed = []
    while missesLeft > 0 and "".join(hangmanWord) != secretWord:
        displayString = createDisplayString(lettersGuessed, missesLeft,
                                            hangmanWord)
        print(displayString)
        if debug:
            print("(word is " + secretWord + ")")
            print("# possible words: " + str(len(words)))
        guessedLetter = handleUserInputLetterGuess(lettersGuessed,
                                                   displayString)
        lettersGuessed.append(guessedLetter)
        lettersGuessed = sorted(lettersGuessed)
        changeword = getNewWordList("".join(hangmanWord), guessedLetter, words,
                                    debug)
        hangmanWord = list(changeword[0])
        words = changeword[1]
        secretWord = words[random.randrange(0, len(words))]
        process = processUserGuessClever(guessedLetter, hangmanWord, missesLeft)
        missesLeft = process[0]
        if process[1]:
            print("good job!\n")
        else:
            print("you missed: " + guessedLetter + " not in word\n")
    if "".join(hangmanWord) == secretWord:
        print("you guessed the word: " + secretWord)
        won = True
    elif missesLeft == 0:
        print("you're hung!!\nword is " + secretWord)
        won = False
    print("you made " + str(len(lettersGuessed)) + " guesses with " + \
          str(missStart - missesLeft) + " misses\n")
    return won



if __name__ == "__main__":
    '''
    Running Hangman.py should start the game, which is done by calling runGame, therefore, we have provided you this code below.
    '''
    again = True
    wincount = 0
    losecount = 0
    while again:
        won = runGame('lowerwords.txt')
        playagain = input("Do you want to play again? y or n> ")
        if playagain == "n":
            again = False
        if won:
            wincount += 1
        else:
            losecount += 1
    print("You won " + str(wincount) + " game(s) and lost " + str(losecount))