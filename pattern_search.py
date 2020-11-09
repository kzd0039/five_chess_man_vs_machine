from collections import Counter

#pattern search method for all method
#total pattern numbers: , labeled from to 
#the score for different pattern is pre-defined by different value

#place chess on current postion and check all the pattern
#return all the existed pattern occured on current position

def pattern(board, r, c, isBlack):
    color = 2 if isBlack else 1
    board[r][c] = color
    patterns = search(board, r, c, color)
    board[r][c] = 0
    return score(patterns)

# return four direction 
def direction():
    return [[[0,1],[0,-1]],[[1,0],[-1,0]],[[1,1],[-1,-1]],[[1,-1],[-1,1]]]

# return if postion is out of range
def isValid(i, j):
    return i > -1 and i < 15 and j > -1 and j < 15

def score(patterns):
    map = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0,
           6:0, 7:0, 8:0, 9:0, 10:0,
           11:0, 12:0, 13:0, 14:0, 15:0,
           16:0, 17:0, 18:0, 19:0, 20:0,}
    ans = 0
    for p in patterns.keys():
        ans += map[p] * patterns[p]
    return ans

# five contiguous chess on the board
def search(board, r, c, color):
    ans = Counter()
    for d in direction():
        linkedChess = 1
        end = []
        for a, b in d:
            i = r + a
            j = c + b
            while isValid(i,j) and board[i][j] == color:
                linkedChess += 1
                i += a
                j += b
            end.append([i,j])
        #pattern1: 5
        if linkedChess >= 5:
            ans[1] += 1
        #pattern2: blank + 4 + blank
        #pattern3: blank + 4 + rival/out of bound
        elif linkedChess == 4:
            count = 0
            for row, col in end:
                if not (isValid(row,col) and board[row][col] == 0):
                    count += 1
            if count == 0:
                ans[2] += 1
            elif count == 1:
                ans[3] += 1
        #pattern4:
        #pattern6:
        #pattern8:
        #pattern13:
        elif linkedChess == 3:
            count = 0
            for row, col in end:
                if not (isValid(row,col) and board[row][col] == 0):
                    count += 1
            if count == 0:
                a, b = d[0]
                end[0][0] += a
                end[0][1] += b
                a, b = d[1]
                end[1][0] += a
                end[1][1] += b
                count2 = 0
                for row, col in end:
                    if isValid(row,col) and board[row][col] == color:
                        ans[4] += 1
                    elif isValid(row,col) and board[row][col] == 0:
                        ans[6] += 1
                    else:
                        ans[13] += 1
            elif count == 1:
                count[8] += 1 
        #pattern5:
        #pattern7:
        #pattern9:
        #pattern11:
        #pattern17:
        #pattern20:
        elif linkedChess == 2:
            count = []
            index = 0
            for row, col in end:
                if not (isValid(row,col) and board[row][col] == 0):
                    continue
                count.add(index)
                index += 1
            if len(count) == 2:
                pass
            elif len(count) == 1:
                row, col = end[index]
                row += d[index][0]
                col += d[index][1]
                if isValid(row,col) and board[row][col] == color:
                    ans[9] += 1
                if isValid(row,col) and board[row][col] == 0:
                    ans[17] += 1
        #pattern4:
        #pattern9:
        #pattern11:
        #pattern12:
        #pattern14:
        #pattern15:
        #pattern16:
        #pattern18:
        #pattern19:
        elif linkedChess == 1:
            count = 0
            for row, col in end:
                if not (isValid(row,col) and board[row][col] == 0):
                    count += 1
            if count == 0:
                pass
            elif count == 1:
                pass       

    return False



def main():
    pass

if __name__ == '__main__':
    main()
