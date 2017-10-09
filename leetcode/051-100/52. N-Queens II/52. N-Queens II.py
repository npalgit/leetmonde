#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 52. N-Queens II
# Created by yangchao 04/04/2017
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# solution
# Created by yangchao 26/03/2017
import copy


class Solution(object):
    def __init__(self):
        self.queen = 'Q'
        self.pot = '.'
        self.result = 0

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = 0
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
                    self.result += 1

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
print(s.totalNQueens(4))
s1 = Solution()
print(s1.totalNQueens(5))
print(s1.totalNQueens(8))
