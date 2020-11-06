# construct the method here
# black = 2, white = 1, null = 0
def alpha_beta_pruning(board, isBlack, chessCount):
    # base case: no chess on the board, put the first chess on r = 7,c = 7
    chess = 2 if isBlack else 1
    if chessCount == 0:
        board[7][7] = chess
    return board

def main():
    pass

if __name__ == '__main__':
    main()