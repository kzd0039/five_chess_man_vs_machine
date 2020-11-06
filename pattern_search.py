#pattern search method for all method
#total pattern numbers: , labeled from to 
#the score for different pattern is pre-defined by different value

#place chess on current postion and check all the pattern
#return all the existed pattern occured on current position

def pattern(board, r, c, isBlack):
    color = 2 if isBlack else 1
    board[r][c] = color
    output = [ ]
    for i,f in enumerate(caseList()):
        if f(board, r, c, color):
            output.append(i+1)
    return output

# return four direction 
def direction():
    return [[[0,1],[0,-1]],[[1,0],[-1,0]],[[1,1],[-1,-1]],[[1,-1],[-1,1]]]

# return all the case search function
def caseList():
    return [case1, case2, case3, case4, case5, 
            case6, case7, case8, case9, case10, 
            case11, case12, case13, case14, case15, 
            case16, case17, case18, case19, case20]

# return if postion is out of range
def isValid(i, j):
    return i > -1 and i < 15 and j > -1 and j < 15

# five contiguous chess on the board
def case1(board, r, c, color):
    for d in direction():
        linkedChess = 1
        for a, b in d:
            i = r, j = c
            i += a
            j += b
            while isValid(i,j) and board[i][j] == color:
                linkedChess += 1
                i += a
                j += b
        #if found 5 contiguous chess, return True
        if linkedChess >= 5:
            return True

    return False

# four contiguous chess on board and both ends are not occupied
def case2(board, r, c, color):
    for d in direction():
        linkedChess = 1
        end = []
        for a, b in d:
            i = r, j = c
            i += a
            j += b
            while isValid(i,j) and board[i][j] == color:
                linkedChess += 1
                i += a
                j += b
            end.append([i,j])
        #if found 4 contiguous chess
        if linkedChess == 4:
            output = True
            for row, col in end:
                if not (isValid(row,col) and board[row][col] == 0):
                    output = False
            if output:
                return True
    return False

# four contiguous chess on board and with one end occupied
def case3(board, r, c, color):
    for d in direction():
        linkedChess = 1
        end = []
        for a, b in d:
            i = r, j = c
            i += a
            j += b
            while isValid(i,j) and board[i][j] == color:
                linkedChess += 1
                i += a
                j += b
            end.append([i,j])
        #if found 4 contiguous chess
        if linkedChess == 4:
            count = 0
            for row, col in end:
                if not (isValid(row,col) and board[row][col] == 0):
                    count += 1
            if count == 1:
                return True
    return False

def case4(board, r, c, color):
    for d in direction():
        pass
    
    return False

def case5(board, r, c, color):
    return False

def case6(board, r, c, color):
    return False

def case7(board, r, c, color):
    return False

def case8(board, r, c, color):
    return False

def case9(board, r, c, color):
    return False

def case10(board, r, c, color):
    return False

def case11(board, r, c, color):
    return False

def case12(board, r, c, color):
    return False

def case13(board, r, c, color):
    return False

def case14(board, r, c, color):
    return False

def case15(board, r, c, color):
    return False

def case16(board, r, c, color):
    return False

def case17(board, r, c, color):
    return False

def case18(board, r, c, color):
    return False

def case19(board, r, c, color):
    return False

def case20(board, r, c, color):
    return False


def main():
    pass

if __name__ == '__main__':
    main()
