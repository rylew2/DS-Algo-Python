

def generateDirections(grid, pos):
    dirs = []
    row, col = pos

    # rightward

    # leftward (reversed)
    # upward
    # downward
    # leftupward
    # rightupward
    # downleftward
    # downrightward

    return dirs



def crossword(grid, word):


    for rowIdx, row in enumerate(grid):
        for colIdx, char in enumerate(row):
            if char == word[0]:
                dirs = generateDirections(grid, (rowIdx, colIdx))

            for s in dirs:
                pass
                # if word.fin









grid=[
    ['s','d','o','g'],
    ['c','u','c','m'],
    ['a','c','a','t'],
    ['t','e','t','k']
]
word='cat'

crossword(grid, word)