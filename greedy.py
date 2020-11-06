import pattern_search

# construct the method heres
# black = 2, white = 1, null = 0
def greedy(board, isBlack, chessCount):
    # base case: no chess on the board, put the first chess on r = 7,c = 7
    chess = 2 if isBlack else 1
    if chessCount == 0:
        board[7][7] = chess
        
    return board

def score():
    map = {1:0, 2:0, 3:0, 4:0, 5:0,
           6:0, 7:0, 8:0, 9:0, 10:0,
           11:0, 12:0, 13:0, 14:0, 15:0,
           16:0, 17:0, 18:0, 19:0, 20:0,}
    return map
def main():
    pass

if __name__ == '__main__':
    main()