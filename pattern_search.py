from collections import Counter
import re

#pattern search method for all method
#total pattern numbers: , labeled from to 
#the score for different pattern is pre-defined by different value

#place chess on current postion and check all the pattern
#return all the existed pattern occured on current position

def pattern(board, r, c, isBlack):
    color = 2 if isBlack else 1
    board[r][c] = color
    res = search(board, r, c, color)
    board[r][c] = 0
    return score(res)

# return four direction 
def direction():
    return [[[0,1],[0,-1]],[[1,0],[-1,0]],[[1,1],[-1,-1]],[[1,-1],[-1,1]]]

# return if postion is out of range
def isValid(i, j):
    return i > -1 and i < 15 and j > -1 and j < 15

def score(patterns):
    map = {1:100000, 2:50000, 3:15000, 4:15000, 5:10000,
           6:15000, 7:5000, 8:4000, 9:3000, 10:3000,
           11:2000, 12:2000, 13:2000, 14:1500, 15:1000,
           16:500, 17:300, 18:400,19:60000,20:20000,21:400,22:60000}
    ans = 0
    for p in patterns.keys():
        ans += map[p] * patterns[p]
    return ans

# five contiguous chess on the board
def search(board, r, c, color):
    count = Counter()
    for d in direction():
        s = [[],[]]
        index = 0
        for a, b in d:
            i = r + a
            j = c + b
            while isValid(i,j):
                s[index].append(str(board[i][j]))
                i += a
                j += b
            index += 1
        index_current_chess = len(s[1])    
        s = s[1][-1::-1] + [str(color)] + s[0]
        index_reverse_chess = len(s) - index_current_chess - 1    
        s = ''.join(s)
        i = 0
        for p in all_patterns(color):
            for match in re.finditer(p, s):
                start = match.start()
                end = match.end()
                if start <= index_current_chess < end:
                    count[i+1] += 1
            if p[-1::-1] != p:
                for match in re.finditer(p[-1::-1], s):
                    start = match.start()
                    end = match.end()
                    if start <= index_reverse_chess < end:
                        count[i+1] += 1
            i += 1
    return count

def all_patterns(color):
    rival = '1' if color == 2 else '2'
    color = str(color)
    blank = '0'
    
    p1 = color * 5
    p2 = blank + color * 4 + blank
    p3= rival + color * 4 + blank
    p4 = blank + color * 3 + blank + color + blank
    p5 = blank + color * 2 + blank + color + blank
    p6 = blank + color * 3 + blank
    p7 = blank + color * 2 + blank + color + blank
    p8 = rival + color * 3 + blank
    p9 = rival + color * 2 + blank + color + blank
    p10 = rival + color + blank + color * 2 + blank
    p11 = blank + color * 2 + blank * 2 + color + blank
    p12 = blank + color + blank + color + blank + color + blank
    p13 = rival + blank + color * 3 + blank + rival
    p14 = blank + color * 2 + blank
    p15 = blank * 2 + color + blank + color + blank * 2
    p16 = rival + color * 2 + blank
    p17 = blank + color + blank
    p18 = rival + color + blank
    
    r1 = rival * 4 + color
    r2 = rival * 3 + color
    r3 = rival * 2 + color
    r4 = rival * 2 + color + rival

    return [p1, p2, p3, p4, p5, 
            p6, p7, p8, p9, p10,
            p11, p12, p13, p14, 
            p15, p16, p17, p18,
            r1,r2,r3,r4]

def main():
    print(all_patterns(2))

if __name__ == '__main__':
    main()
