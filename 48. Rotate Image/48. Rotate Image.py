#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 48. Rotate Image
# Created by yangchao 08/04/2017


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        if l == 0:
            return
        import copy
        _m = copy.deepcopy(matrix)
        for i in range(l):
            for j in range(l):
                x = j
                y = l - 1 - i
                matrix[x][y] = _m[i][j]
        return matrix



s = Solution()


print s.rotate([])    # [[]]
print s.rotate([[1]])    # [[1]]

print s.rotate([[1, 2], [3, 4]])   # [[3, 1], [4, 2]]
print s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])   # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
