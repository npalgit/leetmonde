#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 37. Sudoku Solver
# Created by yangchao 30/03/2017
import copy, time
class Solution(object):
    def __init__(self):
        self.new_new_board = None

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        new_board = []
        mapping = {}
        nums = {unicode(str(i), "utf-8"): 0 for i in range(1, 10)}
        last = None
        left = 0
        i = 0
        for string in board:
            j = 0
            col = []
            for letter in string:
                col.append(letter)
                if letter == '.':
                    mapping[(i, j)] = {'panel': (i/3, j/3), 'vals': copy.deepcopy(nums), 'last': last}
                    last = (i, j)
                    left += 1
                j += 1
            new_board.append(col)
            i += 1
        for row in range(0, 9):
            for col in range(0, 9):
                if new_board[row][col] == '.':
                    continue
                panel = (row/3, col/3)
                val = new_board[row][col]
                for pot in mapping:
                    pot_panel = mapping[pot]['panel']
                    if pot[0] == row or pot[1] == col or panel == pot_panel:
                        if val in mapping[pot]['vals']:
                            mapping[pot]['vals'].pop(val)
        if last is not None:
            self.process(last, new_board, mapping, left)
            if self.new_new_board is not None:
                for row in range(0, 9):
                    for col in range(0, 9):
                        if board[row][col] == '.':
                            pass
                            # board[row][col] = self.new_new_board[row][col]

    def process(self, pot, board, mapping, left):
        content = mapping[pot]
        vals = content['vals']
        row = pot[0]
        col = pot[1]
        panel = content['panel']
        for val in vals:
            failed = False
            last = content['last']
            bd = copy.deepcopy(board)
            mp = copy.deepcopy(mapping)
            if self.new_new_board is not None:
                return
            bd[row][col] = val
            if left == 1:
                self.new_new_board = bd
                return
            # 通知行
            # 通知列
            # 通知块
            while last is not None:
                pot_panel = mp[last]['panel']
                if last[0] == row or last[1] == col or panel == pot_panel:
                    if val in mp[last]['vals']:
                        mp[last]['vals'].pop(val)
                if len(mp[last]['vals']) == 0:
                    failed = True
                    break
                last = mapping[last]['last']
            if failed:
                continue
            self.process(content['last'], bd, mp, left-1)

s = Solution()
print time.time()
#s.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])
#s.solveSudoku(["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"])
#s.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])
s.solveSudoku(["...2...63","3....54.1","..1..398.",".......9.","...538...",".3.......",".263..5..","5.37....8","47...1..."])
if s.new_new_board is not None:
    for j in s.new_new_board:
        print j

print time.time()