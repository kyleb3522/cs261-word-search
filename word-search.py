# CS261 Word Search
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

PUZZLE_FILENAME = "puzzle.txt"

# You do not need to modify this function. It is provided for you.
def load_puzzle():
    """
    Returns the square word search puzzle size, the puzzle letters, the list of words contained in the puzzle.
    size is the square dimensions of the puzzle
    puzzle is a list of all the letters in the puzzle (left to right, top to bottom)
    wordlist is a list of words in the puzzle (strings of uppercase letters).

    """
    
    print("Loading puzzle from file...")
    inFile = open(PUZZLE_FILENAME, 'r')
    puzzle = []
    wordlist = []
    size = int(inFile.readline())
    print("  ","puzzle size is {} x {}".format(size, size))
    puzzle = list(inFile.readline().strip())
    print("  ", len(puzzle), "puzzle letters loaded")
    for line in inFile:
        wordlist.append(line.strip().upper())
    print("  ", len(wordlist), "words loaded.")
    return size, puzzle, wordlist

def solve_puzzle(size, puzzle, wordlist):

    """
    TODO:
    Print welcome message
    Find all the words in the puzzle. Words can be oriented up, down, left, right, diagonally.
    For each found word print the word, start location (row,column) and direction
    With the unused letters (those not appearing in any word) print the hidden message.
    """

    pass  # TO DO... Remove this line when you implement this function
    # initial commit

#
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    size, puzzle, wordlist = load_puzzle()
    solve_puzzle(size, puzzle, wordlist)
