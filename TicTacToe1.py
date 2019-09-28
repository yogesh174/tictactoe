input_choose = input("Player 1:Choose X or O")
input_start = input("Do you want to start the game?")

li = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
def print_board():
    print(' {} | {} | {} '.format(li[7],li[8],li[9]))
    print("------------")
    print(" {} | {} | {} ".format(li[4],li[5],li[6]))
    print("------------")
    print(" {} | {} | {} ".format(li[1],li[2],li[3]))
def three_variables_equal(a,b,c):
    if (a==b and b==c) :
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
while True:
    x_pos = int(input("Enter X position:"))
    if x_pos in li1:
        print("{} position not empty".format(x_pos))


    li[x_pos] = 'X'
    if check_win():
        print("Player 1 wins the match")
        break
    o_pos = int(input("Enter O position:"))
    if check_win():
        print("Player 2 wins the match")
        break
    li1.append(x_pos)
    li1.append(o_pos)



