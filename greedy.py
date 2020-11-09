from pattern_search import pattern, score

# construct the method here
# black = 2, white = 1, null = 0
def _greedy(board, isBlack, chessCount):
    # base case: no chess on the board, put the first chess on r = 7,c = 7
    chess = 2 if isBlack else 1
    if chessCount == 0:
        board[7][7] = chess
    return board

    position = [-1, -1]
    max_score = -1
    for r in range(15):
        for c in range(15):
            cur_pattern = pattern(board, r, c, isBlack)
            cur_score = score(cur_pattern)
            if cur_score > max_score:
                postion = [r, c]
                max_score = cur_score
    
    board[r][c] = chess
    return board


def main():
    pass

if __name__ == '__main__':
    main()