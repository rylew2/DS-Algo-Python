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

def dfsHasWord(grid,i, j, word, wordIdx ):
    # print('i={} j={} word[wordIdx]={}'.format(i,j,word[wordIdx]))
    if  i<0 or i>=len(grid) or j<0 or j>=len(grid[0])-1 or word[wordIdx] != grid[i][j]:
        return False
    if wordIdx == len(word)-1:
        print('found match at i={} j={}'.format(i,j))
        return True

    return any(
        [
        dfsHasWord(grid, i, j+1, word, wordIdx+1),
        dfsHasWord(grid, i, j - 1, word, wordIdx + 1),
        dfsHasWord(grid, i+1, j, word, wordIdx + 1),
        dfsHasWord(grid, i-1, j, word, wordIdx + 1),
        dfsHasWord(grid, i+1, j + 1, word, wordIdx + 1),
        dfsHasWord(grid, i-1, j + 1, word, wordIdx + 1),
        dfsHasWord(grid, i+1, j - 1, word, wordIdx + 1),
        dfsHasWord(grid, i-1, j - 1, word, wordIdx + 1)
        ]
    )

from collections import defaultdict
import numpy as np
def crossword(grid, word):
    # res = np.where(np.array(grid) == word[0]) # get all the locations in grid where char == word's first char
    # locations = list(zip(res[0], res[1]))
    # for rowIdx, colIdx in locations:
    #     generateDirections(grid, rowIdx, colIdx, word)
    #
    row, col = len(grid), len(grid[0])
    firstLetter = word[0]
    ans = []
    for i in range(row): # O(RC)
        for j in range(col):
            if grid[i][j] == firstLetter:
                ans.append(dfsHasWord(grid, i, j, word, 0))

    print(ans)

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