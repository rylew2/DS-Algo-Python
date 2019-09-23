
def generateDirections(grid, rowIdx, colIdx, word):
    dirs = []
    length = len(word)
    numRows, numCols = len(grid), len(grid[0])


    colGrid = list(zip(*grid)) # grid with columns for up down and diagonals

    condition = { # condition
        'right': length <= (numCols - colIdx),
        'left': length <= (colIdx +1),
        'up' : length <= (rowIdx+1),
        'down': length <= (numRows - rowIdx)
    }
    # w = ''

    # rightward
    if condition['right']:
        w = ''.join(grid[rowIdx][colIdx: colIdx+length])
        if w == word: dirs.append( (w,'right', [rowIdx, colIdx]) )

    # leftward (reversed)
    if condition['left']:
        w = ''.join(reversed(grid[rowIdx][0:colIdx+1]))
        if w==word: dirs.append( (w, 'left', [rowIdx, colIdx]))

    # upward
    if condition['up']:
        w = ''.join( [ grid[i][colIdx] for i in range(rowIdx, rowIdx-length, -1) ] )
        if w == word: dirs.append( (w, 'up', [rowIdx, colIdx]) )

    # downward
    if condition['down']:
        w = ''.join( [ grid[i][colIdx] for i in range(rowIdx, rowIdx+length)  ] )
        if w == word:  dirs.append( (w, 'down', [rowIdx, colIdx]) )

    # leftupward
    if condition['left'] and condition['up']:
        w=[]; r=rowIdx; c=colIdx;
        for i in range(length):
            w.append(grid[r][c])
            r-=1; c-=1;
        w = ''.join(w)
        print('leftupward word = {}'.format(w))
        if w == word: dirs.append((w, 'leftup', [rowIdx, colIdx]))

    # downleftward
    if condition['left'] and condition['down']:
        w = []; r = rowIdx;  c = colIdx;
        for i in range(length):
            w.append(grid[r][c])
            r += 1; c -= 1;
        w = ''.join(w)
        if w == word: dirs.append((w, 'leftdown', [rowIdx, colIdx]))


    # rightupward
    if condition['right'] and condition['up']:
        w = []; r = rowIdx;  c = colIdx;
        for i in range(length):
            w.append(grid[r][c])
            r -= 1; c += 1;
        w = ''.join(w)
        if w == word: dirs.append((w, 'leftdown', [rowIdx, colIdx]))

    # downrightward
    if condition['right'] and condition['up']:
        w = []; r = rowIdx;  c = colIdx;
        for i in range(length):
            w.append(grid[r][c])
            r += 1; c += 1;
        w = ''.join(w)
        if w == word: dirs.append((w, 'leftdown', [rowIdx, colIdx]))

    return dirs


from collections import defaultdict
def crossword(grid, word):
    d = defaultdict(set)
    dirWords = []
    for rowIdx, row in enumerate(grid):
        for colIdx, char in enumerate(row):
            if char == word[0]:
                dirWords = generateDirections(grid, rowIdx, colIdx, word)
                print('in dirWords')
                print(dirWords)

            for thisWord, direction, indices in dirWords:
                d[direction].add(tuple(indices))
                # print('')

    print(d)




grid=[
    ['c','d','o','g'],
    ['a','u','c','m'],
    ['t','c','a','t'],
    ['a','e','t','c'],
    ['t','a','a','k'],
    ['t','t','t','k'],


]
word='cat'

crossword(grid, word)