import random
import pyfiglet
def displayHangmanBoard(phaseInt):
    """
    show the current hangman board on the screen based on the given phase
    :param phaseInt: integer to identify the phase
    :return: none
    """
    if phaseInt == 0:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
    if phaseInt == 1:
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    if phaseInt == 2:
        print("________")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    if phaseInt == 3:
        print("________")
        print("|       |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    if phaseInt == 4:
        print("________")
        print("|       |")
        print("|     (*.*)")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    if phaseInt == 5:
        print("________")
        print("|       |")
        print("|     (*.*)")
        print("|    o--|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    if phaseInt == 6:
        print("________")
        print("|       |")
        print("|     (*.*)")
        print("|    o--|--o")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    if phaseInt == 7:
        print("________")
        print("|       |")
        print("|     (*.*)")
        print("|    o--|--o")
        print("|       |")
        print("|       |")
        print("|")
        print("|")
        print("|")
        print("|")
    if phaseInt == 8:
        print("________")
        print("|       |")
        print("|     (*.*)")
        print("|    o--|--o")
        print("|       |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
    if phaseInt == 9:
        print("________")
        print("|       |")
        print("|     (*.*)")
        print("|    o--|--o")
        print("|       |")
        print("|       |")
        print("|      /")
        print("|")
        print("|")
        print("|")
    if phaseInt == 10:
        print("________")
        print("|       |")
        print("|     (*.*)")
        print("|    o--|--o")
        print("|       |")
        print("|       |")
        print("|      / \\")
        print("|")
        print("|")
        print("|")

def askLetter(guessedLetters):
    guess = input("Guess: ")
    while guess.islower() == False or len(guess) > 1 or guess in guessedLetters:
        if guess.islower() == False:
            guess = input("Guess: ")
        elif len(guess) > 1:
            guess = input("Guess: ")
        else:
            break
    return guess

def displayBoard(wordBoard):
    print('word: ' + " ".join(wordBoard))

def updateBoard(currentBoard, letter, positionsList):
    """
    takes current board and adds newly guessed letters
    :param currentBoard:
    :param letter:
    :param positionsList:
    :return:
    """
    for i in positionsList:
        print(i)
        currentBoard[i] = letter
    return currentBoard

def getWord():
    text = open("words.txt", "r")
    return random.choice("".join(text.readlines()).split())


def checkGuess(word, guessLetter):
    """
    check if the letter exists in the word
    :param word:
    :param guessLetter:
    :return: int[] list of index positions of letter in word
    """

    indices = []
    for i in range(len(word)):
        if word[i] == guessLetter:
            indices.append(i)
    return indices

def outputResult(result):
    """
    output result to the screen
    :param result: string
    :return:
    """
    print(result)

def playGame(word):
    """
    run the game
    :return: string result
    """

    # initialize hangmanBoard
    hangmanBoardInt = 0
    max_guesses = 10


    # initialize guessedLetters to empty list
    guessedLetters = []

    # initialize wordBoard
    wordBoard = ["_"] * len(word)

    print(" ".join(wordBoard))
    game_over = False
    won = False

    while not game_over:

        letter = askLetter(guessedLetters) # get letter from the user
        positions = checkGuess(word, letter)

        if len(positions) > 0:
            wordBoard = updateBoard(wordBoard, letter, positions)

        else:
            hangmanBoardInt += 1

        displayBoard(wordBoard)
        displayHangmanBoard(hangmanBoardInt)

        if "".join(wordBoard).lower() == word.lower():
            won = True
            game_over = True

        if hangmanBoardInt == max_guesses:
            game_over = True

        guessedLetters.append(letter)
        print("Guessed Letters: " + " ".join(guessedLetters))

    if won:
            return "Won"
    else:
        return "Lost"

def main():

    filename = "words.txt"
    word = getWord()
    result = playGame(word)
    outputResult(result)
main()
