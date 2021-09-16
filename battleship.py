import random

SizeX = 6
SizeY = 6
board = [[0]*SizeY for i in range(SizeX)]
mask = [[True]*SizeY for i in range(SizeX)]
alphabet = ("A","B","C","D","E","F","G","H","I","J")

def print_board(unmask=False):
    print(" ABCDEF")
    for i in range(SizeY):
        s = str(i + 1)
        for j in range(SizeX):
            s2 = " "
            if board[i][j] == 1: s2 = "*"
            if board[i][j] == 2: s2 = "+"
            if mask[i][j] == True and not unmask: s2 = " "
            s += s2
        print(s)

def place_ships():
    direction = bool(random.randint(0, 1))
    max_x = SizeX - 1
    max_y = SizeY - 1
    if not direction:
        max_x = SizeX - 5
    else:
        max_y = SizeY - 5
    posx = random.randint(0, max_x)
    posy = random.randint(0, max_y)
    board[posx][posy] = 1
    print(posx, posy, direction)
    for i in range(1, 4):
        if not direction: board[posx + i][posy] = 1
        else: board[posx][posy + i] = 1

def Winning_condition():
    end = True
    for i in range(SizeX):
        for j in range(SizeY):
            if board[i][j] == 1 and mask[i][j] == True:
                end = False
    return end


place_ships()
print_board()
ended = Winning_condition()
while not ended:
    s = input("Your shot:")
    guessx = int(s[1]) - 1
    guessy = alphabet.index(s[0])
    print(guessx, guessy)
    if board[guessx][guessy] != 1:
        board[guessx][guessy] = 2
    mask[guessx][guessy] = False
    print_board()
