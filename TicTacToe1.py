input_choose = input("Player 1:Choose X or O")
while (input_choose not in ['X','O']):
        print("INVALID INPUT !![Enter X or O]")
        input_choose = input("Player 1:Choose X or O")
if (input_choose == 'X'):
    x = 'p1'
    o = 'p2'
    print("Player 2 is assigned 'O'")
elif (input_choose == 'O') :
    x = 'p2'
    o = 'p1'
    print("Player 2 is assigned 'X'")

#input_start = input("Do you want to start the game?[Y/N]")


li = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def print_board():
    print(' {} | {} | {} '.format(li[7],li[8],li[9]))
    print("------------")
    print(" {} | {} | {} ".format(li[4],li[5],li[6]))
    print("------------")
    print(" {} | {} | {} ".format(li[1],li[2],li[3]))

def print_pboard():
    print(' 7 | 8 | 9 ')
    print("------------")
    print(" 4 | 5 | 6 ")
    print("------------")
    print(" 1 | 2 | 3 ") 

def three_variables_equal(a,b,c):
    if (a==b and b==c and ( a == 'X' or a == 'O' )) :
        return True
    else:
        return False

def check_win():
    if (three_variables_equal(li[1],li[2],li[3]) or three_variables_equal(li[4],li[5],li[6])
        or three_variables_equal(li[7],li[8],li[9]) or three_variables_equal(li[1],li[4],li[7]) or
        three_variables_equal(li[2],li[5],li[8]) or three_variables_equal(li[3],li[6],li[9]) or
        three_variables_equal(li[1],li[5],li[9]) or three_variables_equal(li[3],li[5],li[7])):
        return True
    else:
        return False
li1=[]
#Printing the board with positions
print_pboard()
print("To assign 'X' and 'O' to the above board just enter the position numbers[1-9]")

while True:
    
    #Taking input for X position
    x_pos = None
    while(type(x_pos) != int):
        try:
            x_pos = int(input("Enter X position[1-9]:"))
        except ValueError :
            print("You have entered a string.Please enter X position[1-9]:")
        
    #Checking if X position is in between 1 to 9
    while (x_pos not in range(1,10)):
        print("Enter X position in between 1 to 9 only")
        x_pos = int(input("Enter X position[1-9]:"))
    
    
    #Checking if X position is empty or not
    while (x_pos in li1):
        print("{} position not empty".format(x_pos))
        x_pos = int(input("Enter X position[1-9]:"))

    #Assigning X its position in board and printing the board
    li[x_pos] = 'X'
    print_board()

    #UNDO
    ux=input("To undo press 'U' or else press any key to continue")
    if ux == 'U':
        li[x_pos] = " "
        print_board()
        #Taking input for X position
        x_pos = None
        while(type(x_pos) != int):
            try:
                x_pos = int(input("Enter X position[1-9]:"))
            except ValueError :
                print("You have entered a string.Please enter X position[1-9]:")

        #Checking if X position is in between 1 to 9
        while (x_pos not in range(1,10)):
            print("Enter X position in between 1 to 9 only")
            x_pos = int(input("Enter X position[1-9]:"))

        #Checking if X position is empty or not
        while (x_pos in li1):
            print("{} position not empty".format(x_pos))
            x_pos = int(input("Enter X position[1-9]:"))

        #Assigning X its position in board and printing the board
        li[x_pos] = 'X'
        print_board()

    #Checking if Player assigned X wins with this move or not
    if check_win():
        if (x == 'p1'):
            print("Player 1 wins the match")
        elif (x == 'p2'):
            print("Player 2 wins the match")
        break

    #Noting down the position numbers in a list
    li1.append(x_pos)

    if(len(li1) == 9 ):
        print("Well Played \n Its a DRAW!")
        break

    #Taking input for O position
    o_pos = None
    while(type(o_pos) != int):
        try:
            o_pos = int(input("Enter O position[1-9]:"))
        except ValueError :
            print("You have entered a string.Please enter O position[1-9]:")


    #Checking if O position is in between 1 to 9
    while (o_pos not in range(1,10)):
        print("Enter O position in between 1 to 9 only")
        o_pos = int(input("Enter O position[1-9]:"))

    #Checking if O position is empty or not
    while (o_pos in li1):
        print("{} position not empty".format(o_pos))
        o_pos = int(input("Enter O position[1-9]:"))

    #Assigning O its position in board and printing the board
    li[o_pos] = 'O'
    print_board()

    #UNDO
    uo=input("To undo press 'U' or else press any key to continue")
    if uo == 'U':
        li[o_pos] = " "
        print_board()

        #Taking input for O position
        o_pos = None
        while(type(o_pos) != int):
            try:
                o_pos = int(input("Enter O position[1-9]:"))
            except ValueError :
                print("You have entered a string.Please enter O position[1-9]:")


        #Checking if O position is in between 1 to 9
        while (o_pos not in range(1,10)):
            print("Enter O position in between 1 to 9 only")
            o_pos = int(input("Enter O position[1-9]:"))

        #Checking if O position is empty or not
        while (o_pos in li1):
            print("{} position not empty".format(o_pos))
            o_pos = int(input("Enter O position[1-9]:"))
    
        #Assigning O its position in board and printing the board
        li[o_pos] = 'O'
        print_board()

        
    #Checking if Player assigned O wins with this move or not
    if check_win():
        if (o == 'p2') :
            print("Player 2 wins the match")
        elif (o == 'p1') :
            print("Player 1 wins the match")
        break

    #Noting down the position numbers in a list
    li1.append(o_pos)

    
#Should rectify error for What if x_pos and o_pos are not numbers



