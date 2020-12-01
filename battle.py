from greedy import _greedy
from alpha_beta_pruning import _alpha_beta_pruning
from heuristic import _heuristic
from minimax import _minimax
from status import check
import time


def battles(f1, f2, record):
    board = [[0 for n in range(15)] for n in range(15)]
    isBlack = True
    chessCount = 0
    k = 2
    while (True):
        board = f1(board, isBlack, chessCount,k)
        chessCount += 1
        result = check(board, isBlack, chessCount)
        for r in board:
            print(r, end = '\n')
        print('-------------------------------------------------')
        if result != 0:
            record[result] += 1
            break
        isBlack = not isBlack

        board = f2(board, isBlack, chessCount,k)
        chessCount += 1
        result = check(board, isBlack, chessCount)
        for r in board:
            print(r, end = '\n')
        print('-------------------------------------------------')    
        if result != 0:
            record[result] += 1
            break
        isBlack = not isBlack
    print(record)


def runningtime(f):
    steps = 0
    k = 2
    start_time = time.time()
    for _ in range(5):
        board = [[0 for n in range(15)] for n in range(15)]
        isBlack = True
        chessCount = 0
        while (True):
            board = f(board, isBlack, chessCount,k)
            chessCount += 1
            result = check(board, isBlack, chessCount)
            if result != 0:
                break
            isBlack = not isBlack

            board = f(board, isBlack, chessCount,k)
            chessCount += 1
            result = check(board, isBlack, chessCount)   
            if result != 0:
                break
            isBlack = not isBlack
        steps += chessCount
    end_time = time.time()
    print('total running time: ',end_time - start_time)
    print('total steps: ', steps)
    print('average running time: ', (end_time - start_time)/steps)

def main():
    pass
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
    
    # record = {1:0, 2:0, -1:0}
    # start_time = time.time()
    # for i in range(1):
    #     battles(_alpha_beta_pruning, _minimax, record)
    # print(record)
    # print(time.time() - start_time)
    print('running time of greedy')
    runningtime(_greedy)
    print('-----------------------------------')

    print('running time of heuristic')
    runningtime(_heuristic)
    print('-----------------------------------')

    print('running time of _minimax')
    runningtime(_minimax)
    print('-----------------------------------')


    print('running time of _alpha_beta_pruning')
    runningtime(_alpha_beta_pruning)
    print('-----------------------------------')
    

if __name__ == '__main__':
    main()