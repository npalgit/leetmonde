#!/usr/bin/env python
# -*- coding: utf-8 -*-

# clean
# Created by yangchao 30/03/2017
import copy, time
class Solution(object):
    def __init__(self):
        self.board = None

    def solveSudoku(self, board):
        new_board = []
        for line in board:
            arr = []
            for i in line:
                arr.append(i)
            new_board.append(arr)
        self.board = new_board
        self.process(0, 0)
        for i in range(0, 9):
            for j in range(0, 9):
                board[i][j] = self.board[i][j]

    def process(self, row, col):
        """
        :param row:
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if row > 8:
            return True
        while col <= 8 and self.board[row][col] != '.':
            col += 1
        if col > 8:
            return self.process(row + 1, 0)
        for letter in range(1, 10):
            c = str(letter)
            if self.check(row, col, c):
                self.board[row][col] = c
                if self.process(row, col + 1):
                    return True
        self.board[row][col] = '.'
        return False

    def check(self, row, col, target):
        for i in range(0, 9):
            if self.board[row][i] == target or self.board[i][col] == target:
                return False
        row = row / 3 * 3
        col = col / 3 * 3
        for i in range(row, row+3):
            for j in range(col, col+3):
                if self.board[i][j] == target:
                    return False
        return True

s = Solution()
print time.time()
#s.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])
#s.solveSudoku(["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"])
s.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])
#s.solveSudoku(["...2...63","3....54.1","..1..398.",".......9.","...538...",".3.......",".263..5..","5.37....8","47...1..."])
if s.board is not None:
    for j in s.board:
        print j

print time.time()
