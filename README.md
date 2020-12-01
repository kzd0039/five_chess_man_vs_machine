# five_chess_man_vs_machine battle

## running instructions
environments: python 3.8.1<br>
baseline battle: run the main() in battle.py<br>
man vs machine: run main() of start_gomoku.py and follow the instruction to play<br>

## documents clarification
baseline algorithms: alpha_beta_pruning.py, greedy.py, minimax.py, heuristic.py<br>
customized algorithms: enhanced_minimax.py<br>
game status check: status.py<br>
pattern discovery and score function: pattern_search.py<br>
man vs machine model: start_gomoku.py<br>
test for function and syntax: sandbox.py, function_test.py<br>

## baseline algorithms
alpha_beta_pruning<br>
minimax<br>
heuristic<br>
greedy<br>
### input/output
input: <br>
<t> board -> 15*15 2-D array<br>
        <t><t> contains only 3 possible integers:<br>
        <t><t> black token: 2<br>
        <t><t> white token: 1<br>
        <t><t> blank/null: 0<br>
<t> isBlack -> True(black token)/False(white token)<br>
<t> chessCount -> number of chess on the current board<br>
<t> k -> max depth of search, only used in minimax and alpha_beta_pruning<br>
output: <br>
<t> board -> 15*15 2-D array<br>

## status of board
check(board, isBlack, chessCount)<br>
input: 
<t> board -> 15*15 2-D array<br>
        <t><t> contains only 3 possible integers:<br>
        <t><t><t> black token: 2<br>
        <t><t><t> white token: 1<br>
        <t><t><t> blank/null: 0<br>
<t>isBlack -> True(black token)/False(white token)<br>
<t>chessCount -> number of chess on the current board<br>

output:<br>
<t> 1 -> white wins<br>
<t> 2 -> black wins<br>
<t> 0 -> game is still going<br>
<t> -1 -> draw<br>

## score function & pattern discovery
pattern definiation(22 patterns total):<br>
<t>  p1 = color * 5<br>
<t> p2 = blank + color * 4 + blank<br>
<t> p3= rival + color * 4 + blank<br>
<t> p4 = blank + color * 3 + blank + color + blank<br>
<t> p5 = blank + color * 2 + blank + color*2 + blank<br>
<t> p6 = blank + color * 3 + blank<br>
<t> p7 = blank + color * 2 + blank + color + blank<br>
<t> p8 = rival + color * 3 + blank<br>
<t> p9 = rival + color * 2 + blank + color + blank<br>
<t> p10 = rival + color + blank + color * 2 + blank<br>
<t> p11 = blank + color * 2 + blank * 2 + color + blank<br>
<t> p12 = blank + color + blank + color + blank + color + blank<br>
<t> p13 = rival + blank + color * 3 + blank + rival<br>
<t> p14 = blank + color * 2 + blank<br>
<t> p15 = blank * 2 + color + blank + color + blank * 2<br>
<t> p16 = rival + color * 2 + blank<br>
<t> p17 = blank + color + blank<br>
<t> p18 = rival + color<br>
<t> p19 = rival * 4 + color<br>
<t> p20 = blank + rival * 3 + color<br>
<t> p21 = blank + rival * 2 + color<br>
<t> p22 = rival * 2 + color + rival<br>

score of pattern:<br>
<t> 1:1000000, 2:50000, 3:15000, 4:15000, 5:8000,<br>
<t> 6:15000, 7:5000, 8:4000, 9:3000, 10:3000,<br>
<t> 11:2000, 12:2000, 13:2000, 14:1500, 15:1000,<br>
<t> 16:500, 17:300, 18:500,19:100000,20:100000,21:1000,22:100000<br>

score calculation depends on specific algorithm<br>

## baseline algorithms evaluation protocol
battle interface: battles(f1,f2,record) <br>
<t>               f1, f2 -> selected algorighms to battle(f1 holds black, f2 holds white)<br>
<t>               record -> dict records the winner<br>
battle protocol of two algotithms f1, f2:<br>
<t>               let f1 holds black, f2 holds white, battle 150 times<br>
<t>               (call battles(f1,f2, record) for 150 times)<br>
<t>               Then let f2 holds black, f1 holds white, battle 150 times<br>
<t>               (call battles(f2,f1,record) for 150 times)<br>
running time:<br>


## man vs machine model:


## customized algorithm: 
input/output: same as baseline algorithms


## battle results of enhanced_minimax vs baseline algorithm: