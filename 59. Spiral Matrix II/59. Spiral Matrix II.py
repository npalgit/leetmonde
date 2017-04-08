#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 59. Spiral Matrix II
# Created by yangchao 08/04/2017


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        matrix = [[0 for i in range(n)] for j in range(n)]

        count = 1
        for _round in range((n + 1) / 2):
            row = _round
            col = _round
            matrix[row][col] = count
            count += 1
            for i in range(_round, n - _round - 1):
                col += 1
                matrix[row][col] = count
                count += 1
            for i in range(_round, n - _round - 1):
                row += 1
                matrix[row][col] = count
                count += 1
            for i in range(n - _round - 1, _round, -1):
                col -= 1
                matrix[row][col] = count
                count += 1
            for i in range(n - _round - 1, _round+1, -1):
                row -= 1
                matrix[row][col] = count
                count += 1
        return matrix

s = Solution()

print s.generateMatrix(0)  # []
print s.generateMatrix(1)  # [[1]]
print s.generateMatrix(2)
print s.generateMatrix(3)
print s.generateMatrix(4)