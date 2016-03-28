count = 0
s = 'abbbccddddcc'
for char in s:
    if char:
        count += 1
return count


def lenRecur(aStr):
    
    if aStr == '':
        return 0

    return 1 + lenRecur(aStr[1:])

lenRecur('asdcdfdf', 0)


def isIn(char, aStr):

    if aStr == '':
        return False
    if len(aStr) == 1:
        return char == aStr[0]
    
    mid = len(aStr)/2
    print mid
    mChar = aStr[mid]
    if char == mChar:
        return True
    elif char < mChar:
        print aStr[:mid]
        return isIn(char, aStr[:mid])
    else:
        print aStr[mid+1:]
        return isIn(char, aStr[mid+1:])
        
        
        
def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False
    
    
    def semordnilap(str1, str2):
        if len(str1) != len(str2):
            return False
        if len(str1) == 1:
            return str1 == str2
        if (str1[0] == str2[-1]):
            return semordnilap(str1[1:], str2[:-1])
        else:
            return False   
      
    return semordnilap(str1, str2)




def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    tup2 = ()
    for i in range(len(aTup)):
        if (i%2==0):
            tup2 = tup2 + (aTup[i],)
    return tup2
    
Univs = ['Harvard', 'MIT']    
for e in Univs:
    print('Univs contains ')
    print e
    print(' which contains')
    for u in e:
        print('     '  + u)
        
        
def a():
    return 3
b = [1, 2, a(), 4]
print b





def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a
    


def halve(a):
    return a/2

def inc(a):
    return a+1

temp = [inc, square, halve, abs]







def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    values = []
    values = aDict.values()
    print values
    count = 0
    for x in values:
        count = count + len(x)
        print count
        print x
    return count





def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    for e in secretWord:
        if e not in lettersGuessed:
            count += 1
    
    if count > 0:
        return False
    else:
        return True




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessed = ''
    length = len(secretWord)
    for i in range(length):
        if (secretWord[i] in lettersGuessed):
            guessed = guessed + secretWord[i]
        else:
            guessed = guessed + '_ '
    return guessed
    
    
    

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    guessed = ''
    allLetters = string.ascii_lowercase
    for i in range(26):
        if (allLetters[i] not in lettersGuessed):
            guessed = guessed + allLetters[i]
        else:
            guessed = guessed + ''
    return guessed






def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    length = len(secretWord)
    lettersGuessed = []
    mistakesMade = 8
    so_far = getGuessedWord(secretWord, lettersGuessed)
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(length) + " letters long")
    print("------------------------------")
    while (mistakesMade > 0):
        print("You have " + str(mistakesMade) + " guesses left.")
        availableLetters = getAvailableLetters(lettersGuessed)
        print("Available letters: " + str(availableLetters))
        guess = str(raw_input("Please guess a letter: "))
        guess = guess.lower()
        if guess not in availableLetters:
            print("Oops! You've already guessed that letter: " + str(so_far))
            print("------------------------------")
        else:
            lettersGuessed.append(guess)
            if guess not in secretWord:
                mistakesMade -= 1
                print("Oops! That letter is not in my word: " + str(so_far))
                print("------------------------------")
            else:
                so_far = getGuessedWord(secretWord, lettersGuessed)
                print("Good guess: " + str(so_far))
                print("------------------------------")
                if isWordGuessed(secretWord, lettersGuessed):
                    break
    if(mistakesMade == 0):
        print("Sorry, you ran out of guesses. The word was " + str(secretWord) + ".")
    else:
        print("Congratulations, you won!")

 
       
    
    
    
    
    
    
    