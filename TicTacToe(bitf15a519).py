t=['*','*','*','*','*','*','*','*','*']
def draw():
    print ("  Tic Tac Toe\n\n")
    print ("Player 1=X","  ","Player 2=O")	 
    print (t[0],"  |  ",t[1],"  |  ",t[2])
    print ("____|_______|_____")
    print (t[3],"  |  ",t[4],"  |  ",t[5])
    print ("____|_______|_____" )
    print (t[6],"  |  ",t[7],"  |  ",t[8])
    print ("    |       |     ")
def checkWin():
    if t[0] == 'X' and t[1] == 'X' and t[2] == 'X':
         return 1
    elif t[0] == 'O' and t[1] == 'O' and t[2] == 'O':
            return 2
    elif t[3] == 'X' and t[4] == 'X' and t[5] == 'X':
            return 1
    elif t[3] == 'O' and t[4] == 'O' and t[5] == 'O':
            return 2
    elif t[6] == 'X' and t[7] == 'X' and t[8] == 'X':
            return 1
    elif t[6] == 'O' and t[7] == 'O' and t[8] == 'O':
            return 2
    elif t[0] == 'X' and t[3] == 'X' and t[6] == 'X':
            return 1
    elif t[0] == 'O' and t[3] == 'O' and t[6] == 'O':
            return 2
    elif t[1] == 'X' and t[4] == 'X' and t[7] == 'X':
            return 1
    elif t[1] == 'O' and t[4] == 'O' and t[7] == 'O':
            return 2
    elif t[2] == 'X' and t[5] == 'X' and t[8] == 'X':
            return 1
    elif t[2] == 'O' and t[5] == 'O' and t[8] == 'O':
            return 2
    elif t[0] == 'X' and t[4] == 'X' and t[8] == 'X':
            return 1
    elif t[0] == 'O' and t[4] == 'O' and t[8] == 'O':
            return 2
    elif t[2] == 'X' and t[4] == 'X' and t[6] == 'X':
            return 1
    elif t[2] == 'O' and t[4] == 'O' and t[6] == 'O':
            return 2
def reset():
    for n in range(8):
        t[n] = '*'
    draw()
def play():
    turn=1
    ch=1
    while ch==1:
        a=int(input("\nEnter Numbers from 0 to 8 to select the corresponding box: "))
        if turn == 1:
            if a>=0 and a<=8:
                t[a]='X'
                turn = 2
                draw()
            if checkWin()==1:
                print ("Player 1 Wins")
                ch=int(input("\n\n Press 1 to play again: "))
                if ch == 1:
                    reset()
        elif turn == 2:
            if a>=0 and a<=8:
                t[a]='O'
                turn = 1
                draw()
            if checkWin() == 2:
                print ("Player 2 Wins")
                ch=int(input("\n\n Press 1 to play again: "))
                if ch == 1:
                    reset()
draw()
play()
