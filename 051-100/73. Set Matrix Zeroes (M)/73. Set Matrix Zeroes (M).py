#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 73. Set Matrix Zeroes (M)
# Created by yangchao 10/04/2017


class Solution(object):
    def setZeroes0(self, matrix):
        """
        M + N space
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        if n == 0:
            return
        mapping = set()
        for row, line in enumerate(matrix):
            for col, item in enumerate(line):
                if item == 0:
                    mapping.add((-1, col))
                    mapping.add((row, -1))
        for x in mapping:
            row = x[0]
            col = x[1]
            if row == -1:
                for i in range(m):
                    matrix[i][col] = 0
            else:
                for j in range(n):
                    matrix[row][j] = 0


