from pattern_search import pattern, score

# construct the method here
# black = 2, white = 1, null = 0
def _greedy(board, isBlack, chessCount):
    # base case: no chess on the board, put the first chess on r = 7,c = 7
    chess = 2 if isBlack else 1
    if chessCount == 0:
        board[7][7] = chess
        return board

    x, y = -1, -1
    max_score = -1
    for r in range(15):
        for c in range(15):
            if (board[r][c] == 0):
                cur_score = pattern(board, r, c, isBlack)
                if cur_score > max_score:
                    x, y = r, c
                    max_score = cur_score
    
    board[x][y] = chess
    return board


def main():
    pass

if __name__ == '__main__':
    main()