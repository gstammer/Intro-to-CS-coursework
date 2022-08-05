'''
Description:
        You must create a Hangman game that allows the user to play and guess a secret word.  
        See the assignment description for details.
    
@author: Georgie Stammer    gss30
'''


import random

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




def getWord(words, length):
    '''
    Selects the secret word that the user must guess. 
    This is done by randomly selecting a word from words that is of length length.
    '''
    possible = [x for x in words if len(x) == length]
    rando = random.randint(0, len(possible))
    return possible[rando]




def createDisplayString(lettersGuessed, missesLeft, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''
    let = " ".join(sorted(lettersGuessed))
    mis = str(missesLeft)
    word = " ".join(hangmanWord)
    x = "letters you've guessed: "+let+"\nmisses remaining = "+mis+"\n"+word
    return x




def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''
    print(displayString)
    let = input("letter> ")
    while let in lettersGuessed:
        print("you already guessed that")
        let = input("letter> ")
    return let




def updateHangmanWord(guessedLetter, secretWord, hangmanWord):
    '''
    Updates hangmanWord according to whether guessedLetter is in secretWord and where in secretWord guessedLetter is in.
    '''
    updated = hangmanWord[:]
    for dex in range(len(secretWord)):
        if secretWord[dex] == guessedLetter:
            updated[dex] = guessedLetter
    return updated




def processUserGuess(guessedLetter, secretWord, hangmanWord, missesLeft):
    '''
    Uses the information in the parameters to update the user's progress in the hangman game.
    '''
    newword = updateHangmanWord(guessedLetter, secretWord, hangmanWord)
    correct = True
    if newword == hangmanWord:
        missesLeft -= 1
        correct = False
    return [newword, missesLeft, correct]




def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''
    f = open(filename, 'r')
    words = []
    for line in f:
        words.append(line.strip())
    length = random.randint(5, 11)
    missesLeft = handleUserInputDifficulty()
    missStart = missesLeft
    secretWord = getWord(words, length)
    hangmanWord = []
    for x in range(length):
        hangmanWord.append("_")
    lettersGuessed = []
    while missesLeft > 0 and "".join(hangmanWord) != secretWord:
        displayString = createDisplayString(lettersGuessed, missesLeft,
                                            hangmanWord)
        guessedLetter = handleUserInputLetterGuess(lettersGuessed,
                                                   displayString)
        lettersGuessed.append(guessedLetter)
        lettersGuessed = sorted(lettersGuessed)
        out = processUserGuess(guessedLetter, secretWord, hangmanWord,
                               missesLeft)
        hangmanWord = out[0]
        missesLeft = out[1]
        if out[2]:
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
          str(missStart - missesLeft) + " misses")
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