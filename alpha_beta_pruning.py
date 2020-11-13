from pattern_search import pattern


# construct the method here
# black = 2, white = 1, null = 0
def _alpha_beta_pruning(board, isBlack, chessCount):
    # base case: no chess on the board, put the first chess on r = 7,c = 7
    chess = 2 if isBlack else 1
    if chessCount == 0:
        board[7][7] = chess
        return board
    firstMove = possibleMove(board)
    lengthFirst = len(firstMove)
    HashNextMove = {}
    maxTemp = -1000000
    for i in range(lengthFirst):
        temp = firstMove[i]
        r = temp[0]
        c = temp[1]  # make the first move here,row and column
        original1 = board[r][c]
        board[r][c] = chess
        secondMove = possibleMove(board)
        if chess == 2:
            secondChess = 1  # second move would reverse color
        else:
            secondChess = 2
        isBlack = not isBlack  # second move would reverse color
        lengthSecond = len(secondMove)
        minVal = 1000000
        for j in range(lengthSecond):
            temp2 = secondMove[j]
            r2 = temp2[0]
            c2 = temp2[1]
            original2 = board[r2][c2]
            board[r2][c2] = secondChess
            thirdMove = possibleMove(board)
            if secondChess == 2:
                thirdChess = 1    #reverse color
            else:
                thirdChess = 2
            isBlack = not isBlack
            localMax = float('-inf')
            for k in range(len(thirdMove)):
                temp3 = thirdMove[k]
                r3 = temp3[0]
                c3 = temp3[1]
                localMax = max(localMax, pattern(board, r3, c3, isBlack))
                if localMax > minVal:   # pruning here
                    break
            minVal = min(minVal, localMax)
            board[r2][c2] = original2
        HashNextMove[(r,c)] = minVal
        board[r][c] = original1

    for pos in HashNextMove:
        maxTemp = max(maxTemp, HashNextMove[pos])
    searMax = maxTemp
    for position in HashNextMove.keys():
        minScore = HashNextMove[position]  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if minScore == searMax:
            rowNumber = position[0]
            columnNumber = position[1]
    board[rowNumber][columnNumber] = chess
    return board

def possibleMove(board):
    possibleLocation = []
    for i in range(15):
        for j in range(15):
            if board[i][j] == 0:
                possibleLocation.append([i, j])
    return possibleLocation


def main():
    pass

if __name__ == '__main__':
    main()