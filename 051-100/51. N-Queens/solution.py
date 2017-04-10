#!/usr/bin/env python
# -*- coding: utf-8 -*-

# solution
# Created by yangchao 26/03/2017
import copy


class Solution(object):
    def __init__(self):
        self.queen = 'Q'
        self.pot = '.'
        self.result = []

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = []
        arr = range(0, n)
        mat = [[self.pot for i in arr] for j in arr]
        self.queens(mat, 0, n)
        return self.result

    def queens(self, mat, row_num, n):
        for i in range(0, n):
            if self.check(mat, row_num, i, n):
                new_mat = copy.deepcopy(mat)
                new_mat[row_num][i] = self.queen
                if row_num < n - 1:
                    self.queens(new_mat, row_num + 1, n)
                else:
                    self.result.append([''.join(i) for i in new_mat])

    def check(self, mat, row_num, col_num, n):
        # row_num, col_num
        arr = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        for i in arr:
            row = row_num
            col = col_num
            while 1:
                row += i[0]
                col += i[1]
                if row < 0 or row >= n or col < 0 or col >= n:
                    break
                if mat[row][col] == self.queen:
                    return False
        return True

s = Solution()
print(s.solveNQueens(4))
s1 = Solution()
print(s1.solveNQueens(5))
print(len(s1.solveNQueens(5)))
r = s1.solveNQueens(5)
x = 0
for i in r:
    x += 1
    print str(x) + ") ------------------------"
    for j in i:
        print j
