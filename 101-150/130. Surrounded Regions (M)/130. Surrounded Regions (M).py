#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 130. Surrounded Regions (M)
# Created by yangchao 19/04/2017


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        if n == 0:
            return
        saved = set()

        def reach(points, reached):
            temp = set()
            completed = False
            for point in points:
                if point in saved:
                    completed = True
                    break
                i = point[0]
                j = point[1]
                if i == 0 or i == m -1 or j ==0 or j == n-1:
                    completed = True
                if (i-1, j) not in reached and i >0 and board[i-1][j] == 'O':
                    temp.add((i-1, j))
                if (i+1, j) not in reached and i <m-1 and board[i+1][j] == 'O':
                    temp.add((i+1, j))
                if (i, j-1) not in reached and j >0 and board[i][j-1] == 'O':
                    temp.add((i, j-1))
                if (i, j+1) not in reached and j <n-1 and board[i][j+1] == 'O':
                    temp.add((i, j+1))

            if completed:
                for point in reached:
                    saved.add(point)
            elif temp:
                reach(temp, reached|points)
            else:
                for point in reached:
                    board[point[0]][point[1]] = 'X'
                for point in points:
                    board[point[0]][point[1]] = 'X'

        for i, line in enumerate(board):
            for j, x in enumerate(line):
                loc = (i, j)
                if x == 'X':
                    continue
                if loc in saved:
                    continue
                if i == 0 or i == m -1 or j ==0 or j == n-1:
                    saved.add(loc)
                    continue
                points = set()
                points.add(loc)
                reach(points, set())
        for line in board:
            print line
        print '---'


s = Solution()

b1 = [
    ['X', 'X', 'X', 'X', ],
    ['X', 'O', 'O', 'X', ],
    ['X', 'X', 'O', 'X', ],
    ['X', 'O', 'X', 'X', ],
]
b2 = [
    ['O', 'X', 'X', 'X', ],
    ['X', 'X', 'O', 'X', ],
    ['X', 'O', 'O', 'X', ],
    ['X', 'O', 'X', 'X', ],
]

b3 = [
    ['X', 'O', 'X', 'X', ],
    ['X', 'O', 'O', 'X', ],
    ['X', 'X', 'O', 'X', ],
    ['X', 'O', 'X', 'X', ],
]
b4 = [
    "XOXOXOOOXO",
    "XOOXXXOOOX",
    "OOOOOOOOXX",
    "OOOOOOXOOX",
    "OOXXOXXOOO",
    "XOOXXXOXXO",
    "XOXOOXXOXO",
    "XXOXXOXOOX",
    "OOOOXOXOXO",
    "XXOXXXXOOO"]
def pre(arr):
    ret = []
    for line in arr:
        l = []
        for x in line:
            l.append(x)
        ret.append(l)
    return ret

b5 = ["XOXOXOOOXO","XOOXXXOOOX","OOOOOOOOXX","OOOOOOXOOX","OOXXOXXOOO","XOOXXXXXXO","XOXXXXXOXO","XXOXXXXOOX","OOOOXXXOXO","XXOXXXXOOO"]
for line in pre(b5):
    print line
print '----'

s.solve(pre(b4))
s.solve(b1)
s.solve(b2)
s.solve(b3)