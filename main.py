global board
board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
player = "X"

'''
Print the board in a visually pleasing way
'''
def printBoard(board):
    for line in board:
        print(line)

'''
Take in user input and replace the appropriate space
'''
def makeMove():
    global player
    x = int(input("Player" + player + ", what is the X coordinate? "))
    y = int(input("What is the Y coordinate? "))

    while board[y][x] != " ":
        print("You must choose an empty spot!")
        x = int(input("Player" + player + ", what is the X coordinate? "))
        y = int(input("What is the Y coordinate? "))

    board[y][x] = "X"
    if player == "X":
        board[y][x] = "X"
        player = "O"
    else: 
        board[y][x] = "O"
        player = "X"

'''
Did the player that just went, win?
'''
#def isWin()
    #row

    #column

    #diagonals

def main():
    printBoard(board)
    gamewon = False
    while gamewon == False:
        tictac()
    print("GAMEOVER")