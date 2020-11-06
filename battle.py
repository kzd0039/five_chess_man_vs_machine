import greedy
import alpha_beta_pruning
import heuristic
import minimax
import status

def main():
    # initialized the board
    # black = 2, white = 1, null = 0
    board = [[0 for n in range(15)] for n in range(15)]
    isBlack = True
    
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
    for i in range(100):
        isBlack = True
        chessCount = 0
        while (True):
            board = greedy(board, isBlack, chessCount)
            result = status(board, isBlack, chessCount)
            if result != 0:
                record[result] += 1
                break

            chessCount += 1
            isBlack = not isBlack

            board = minimax(board, isBlack, chessCount)
            result = status(board, isBlack, chessCount)
            if result != 0:
                record[result] += 1
                break
            
            chessCount += 1
            isBlack = not isBlack
            

    print(record)


if __name__ == '__main__':
    main()