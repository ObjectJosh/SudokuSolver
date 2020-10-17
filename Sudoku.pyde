sudoku = [
    [3,8,5,0,0,0,0,0,0],
    [9,2,1,0,0,0,0,0,0],
    [6,4,7,0,0,0,0,0,0],
    [0,0,0,1,2,3,0,0,0],
    [0,0,0,7,8,4,0,0,0],
    [0,0,0,6,9,5,0,0,0],
    [0,0,0,0,0,0,8,7,3],
    [0,0,0,0,0,0,9,6,2],
    [0,0,0,0,0,0,1,4,5],
]

gridx = 603
gridy = 603
def setup():
    size(gridx, gridy)
    background(255)

def draw():
    drawGrid(sudoku)
    mapNums(sudoku)
    solveRow(sudoku)
        
def drawGrid(board):
    x1 = 0;
    x2 = gridx
    y1 = 0;
    y2 = 0;
    for i in range(len(board)+1):
        if y1 % (gridx//3)//3 == 0:
            strokeWeight(3)
        else:
            strokeWeight(1)
        line(x1, y1, x2, y2)
        line(y1, x1, y2, x2);
        y1 += gridy//len(board)
        y2 += gridy//len(board)

def mapNums(board):
    x1 = gridx//9 - (0.5*(gridx//9))
    y1 = gridy//9 - (0.5*(gridy//9))
    textSize(40)
    textAlign(CENTER, CENTER)
    fill(0);
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != 0:
                text(board[row][col], x1, y1)
            x1+=gridx//9
        y1+=gridy//9
        x1 = gridx//9 - (0.5*(gridx//9))

def solveRow(board):
    if isCompleted(board) == False:
        return True
    else:
        r = isCompleted(board)[0]
        c = isCompleted(board)[1]
    if board[r][c] == 0:
        for count in range(1, 10):
            if isValid(r, c, count, board):
                board[r][c] = count
                if solveRow(board):
                    return True
                board[r][c] = 0
    return False

def isValid(row, col, num, board):
    if num != 0:
        for c in range(len(board[0])):
            if board[row][c] == num:
                return False
        for r in range(len(board)):
            if board[r][col] == num:
                return False
    row_pos = row//3
    col_pos = col//3
    start_row = row_pos * 3
    start_col = col_pos * 3
    for r in range(3):
        for c in range(3):
            if board[r + start_row][c + start_col] == num:
                return False
    return True

def isCompleted(board):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 0:
                return r, c
    return False
            
