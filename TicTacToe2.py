def three_variables_equal(a,b,c):
    if (a==b and b==c) :
        return True
    else:
        return False
def check_win(one,two,three,four,five,six,seven,eight,nine):
    if (three_variables_equal(one,two,three) or three_variables_equal(four,five,six)
        or three_variables_equal(seven,eight,nine) or three_variables_equal(one,four,seven) or
        three_variables_equal(two,five,eight) or three_variables_equal(three,six,nine) or
        three_variables_equal(one,five,nine)):
        return True
    else:
        return False

