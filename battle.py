from greedy import _greedy
from alpha_beta_pruning import _alpha_beta_pruning
from heuristic import _heuristic
from minimax import _minimax
from status import check

def battles(f1, f2, record):
    board = [[0 for n in range(15)] for n in range(15)]
    isBlack = True
    chessCount = 0
    while (True):
        board = f1(board, isBlack, chessCount)
        result = check(board, isBlack, chessCount)
        if result != 0:
            record[result] += 1
            break
        for r in board:
            print(r, end = '\n')
        print('-------------------------------------------------')
        chessCount += 1
        isBlack = not isBlack

        board = f2(board, isBlack, chessCount)
        result = check(board, isBlack, chessCount)
        if result != 0:
            record[result] += 1
            break
        for r in board:
            print(r, end = '\n')
        print('-------------------------------------------------')
        chessCount += 1
        isBlack = not isBlack

def main():
    # initialized the board
    # black = 2, white = 1, null = 0
    board = [[0 for n in range(15)] for n in range(15)]
    isBlack = True
    chessCount = 0

    #base line battle
    #candidate: alpha_beta_prouning, greedy, heuristic, minimax
    #target: find the one with the best success rate
    #method: compare a and b first, get the winner, then compare c with the winner. 
    #        four candiate need 3 battles total
    #        battle time for each comparision: 100

    # example of battle, greedy versus minimax
    # By default, the first method holds black and the other method holds white
    #1: number of white wins(second algorithm, minimax here), 
    #2: number of black wins(first algorith, greedy here),
    #-1: number of draws
    
    record = {1:0, 2:0, -1:0}
    for i in range(1):
        # reset all the parameter
        battles(_greedy,_greedy,record)

    print(record)


if __name__ == '__main__':
    main()