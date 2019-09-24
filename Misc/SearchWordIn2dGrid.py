
def generateDirections(grid, originalRowIdx, originalColIdx, word):
    matches=[]
    numRows, numCols = len(grid), len(grid[0])

    left = (0, -1, 'left');             right = (0, 1, 'right');
    up = (-1, 0, 'up');                 down = (1, 0, 'down');
    leftdown = (1, -1 ,'leftdown');     leftup = (-1,-1, 'leftup');
    rightdown = (1, 1, 'rightdown');    rightup = ( -1,1, 'rightup');

    for dx, dy, dir in [ left, right, up, down,leftdown, leftup, rightdown, rightup]:
        rowIdx,colIdx = originalRowIdx, originalColIdx
        w = [grid[rowIdx][colIdx]] #initialize word with first char since we already know it's a match
        rowIdx +=dx; colIdx+=dy;

        #while it's inbounds and we're under world length, keep loopin
        while rowIdx>=0 and rowIdx<numRows and colIdx>=0 and colIdx<numCols and len(w)<len(word):
            w.append(grid[rowIdx][colIdx])
            rowIdx+=dx; colIdx+=dy;

        w = ''.join(w)
        if len(w)==len(word) and w==word:
            matches.append((originalRowIdx, originalColIdx, dir))

    print(matches)
    return matches


from collections import defaultdict
def crossword(grid, word):
    dirWords = []
    for rowIdx, row in enumerate(grid):
        for colIdx, char in enumerate(row):
            if char == word[0]:
                dirWords = generateDirections(grid, rowIdx, colIdx, word)
                # print(dirWords)


grid=[
    ['c','d','o','g'],
    ['a','u','c','m'],
    ['t','c','a','t'],
    ['t','e','t','c'],
    ['a','a','a','k'],
    ['c','t','t','k'],
]
word='cat'
crossword(grid, word)