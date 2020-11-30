from pattern_search import huristic_score
from collections import defaultdict
import random

# construct the method here
# black = 2, white = 1, null = 0


def _minimax(board, isBlack, chessCount, k):
    # base case: no chess on the board, put the first chess on r = 7,c = 7
    chess = 2 if isBlack else 1
    if chessCount == 0:
        board[7][7] = chess
        return board
    positions = defaultdict(list)
    max_score = float('-inf')
    count = 0
    for i in range(15):
        for j in range(15):
            if board[i][j] == 0:
                board[i][j] = chess
                score =  dfs(board, isBlack, k, isBlack)
                board[i][j] = 0
                positions[score].append((i,j))
                if score > max_score:
                    max_score = score
                count += 1
                print('evaluate ' + str(count) + ' position')
                # for r in board:
                #     print(r, end = '\n')
                # print('-------------------------------------------------')
                
    index = random.randint(0,len(positions[max_score])-1)
    x, y = positions[max_score][index]
    board[x][y] = chess
    return board

def dfs(board, isBlack, k, original_player):
    chess = 2 if isBlack else 1
    max_score = float('-inf')
    if k == 1:
        return huristic_score(board, -1, -1, isBlack)
    if isBlack == original_player:
        k -= 1
    for x in range(15):
        for y in range(15):
            if board[x][y] == 0:
                board[x][y] = chess
                max_score = max(max_score, dfs(board, not isBlack, k, original_player))
                board[x][y] = 0          
    return max_score

def main():
    pass

if __name__ == '__main__':
    main()
