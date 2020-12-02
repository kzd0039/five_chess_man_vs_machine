# five_chess_man_vs_machine battle

## running instructions
1. environments: python 3.8.1
2. baseline battle: select the code segment in main() of battle.py and run
3. man vs machine: run main() of start_gomoku.py and follow the instruction to play

## documents clarification
1. baseline algorithms: alpha_beta_pruning.py, greedy.py, minimax.py, heuristic.py
2. customized algorithms: enhanced_minimax.py
3. game status check: status.py
4. pattern discovery and score function: pattern_search.py
5. man vs machine model: start_gomoku.py
6. test for function and syntax: sandbox.py, function_test.py

## baseline algorithms
alpha_beta_pruning<br>
minimax<br>
heuristic<br>
greedy<br>
### input/output
input: <br>
    1. board -> 15*15 2-D array<br>
         contains only 3 possible integers:<br>
         black token: 2<br>
         white token: 1<br>
         blank/null: 0<br>
    2. isBlack -> True(black token)/False(white token)<br>
    3. chessCount -> number of chess on the current board<br>
    4. k -> max depth of search, only used in minimax and alpha_beta_pruning<br>
output: <br>
     board -> 15*15 2-D array<br>

## customized algorithm: 
input/output: same as baseline algorithms


## status of board
check(board, isBlack, chessCount)<br>
input: 
    board -> 15*15 2-D array<br>
         contains only 3 possible integers:<br>
         black token: 2<br>
         white token: 1<br>
         blank/null: 0<br>
    isBlack -> True(black token)/False(white token)<br>
    chessCount -> number of chess on the current board<br>

output:<br>
    1 -> white wins<br>
    2 -> black wins<br>
    0 -> game is still going<br>
    -1 -> draw<br>

## score function & pattern discovery
pattern definiation(22 patterns total):<br>
    p1 = color * 5<br>
    p2 = blank + color * 4 + blank<br>
    p3= rival + color * 4 + blank<br>
    p4 = blank + color * 3 + blank + color + blank<br>
    p5 = blank + color * 2 + blank + color*2 + blank<br>
    p6 = blank + color * 3 + blank<br>
    p7 = blank + color * 2 + blank + color + blank<br>
    p8 = rival + color * 3 + blank<br>
    p9 = rival + color * 2 + blank + color + blank<br>
    p10 = rival + color + blank + color * 2 + blank<br>
    p11 = blank + color * 2 + blank * 2 + color + blank<br>
    p12 = blank + color + blank + color + blank + color + blank<br>
    p13 = rival + blank + color * 3 + blank + rival<br>
    p14 = blank + color * 2 + blank<br>
    p15 = blank * 2 + color + blank + color + blank * 2<br>
    p16 = rival + color * 2 + blank<br>
    p17 = blank + color + blank<br>
    p18 = rival + color<br>
    p19 = rival * 4 + color<br>
    p20 = blank + rival * 3 + color<br>
    p21 = blank + rival * 2 + color<br>
    p22 = rival * 2 + color + rival<br>

score of pattern:<br>
    1:1000000, 2:50000, 3:15000, 4:15000, 5:8000,<br>
    6:15000, 7:5000, 8:4000, 9:3000, 10:3000,<br>
    11:2000, 12:2000, 13:2000, 14:1500, 15:1000,<br>
    16:500, 17:300, 18:500,19:100000,20:100000,21:1000,22:100000<br>

score calculation depends on specific algorithm<br>

## baseline algorithms evaluation protocol
battle interface: <br>
    battles(f1,f2,record) <br>
    f1, f2 -> selected algorighms to battle(f1 holds black, f2 holds white)<br>
    record -> dict records the winner<br>

battle protocol of two algotithms f1, f2:<br>
    let f1 holds black, f2 holds white, battle 100 times<br>
    (call battles(f1,f2, record) for 100 times)<br>
    Then let f2 holds black, f1 holds white, battle 100 times<br>
    (call battles(f2,f1,record) for 100 times)<br>

multiprocessBattle:<br>
    To save running time, multiprocessBattle can be used for battle of two algorthms.<br>

running time:<br>
    let selected algorithm battle with itself for 5 times, <br>
    count total steps and total running time, then calculate <br>
    average running time of each step <br>

## running results of baseline battle
### success rate
1. heuristic vs greedy -> 106 : 94
2. alpha_beta_pruning vs minimax -> 31 : 19
3. heuristic vs alpha_beta_pruning -> 17 : 33
4. enhanced_alpha_beta_pruning vsalpha_beta_pruning -> 27 : 23

### running time
1. heuristic -> 0.73 second per step
2. greedy -> 0.05 second per step
3. alpha_beta_pruning -> 79.52 second per step
4. minimax -> 9.69 second per step
5. enhanced_alpha_beta_pruning -> 9.51 second per step

## man vs machine model:
    1. select one of the five algorithms to battle
    2. enter the postition to place your chess(by default, AI plays first and holds black)

