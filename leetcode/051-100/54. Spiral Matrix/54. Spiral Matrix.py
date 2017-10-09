#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 54. Spiral Matrix
# Created by yangchao 08/04/2017


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row_len = len(matrix)
        if row_len == 0:
            return []
        col_len = len(matrix[0])
        if col_len == 0:
            return []

        _top = row_len
        if col_len < _top:
            _top = col_len

        result = []
        for _round in range((_top + 1) / 2):
            row = _round
            col = _round
            result.append(matrix[row][col])
            for i in range(_round, col_len - _round - 1):
                col += 1
                result.append(matrix[row][col])
            for i in range(_round, row_len - _round - 1):
                row += 1
                result.append(matrix[row][col])
            for i in range(col_len - _round - 1, _round, -1):
                if (1+_round) * 2 > row_len:
                    break
                col -= 1
                result.append(matrix[row][col])
            for i in range(row_len - _round - 1, _round+1, -1):
                if (1+_round) * 2 > col_len:
                    break
                row -= 1
                result.append(matrix[row][col])

        return result


s = Solution()
print s.spiralOrder([])  # []
print s.spiralOrder([[1]])  # [1]
print s.spiralOrder([[1, 2, 4]])  # [1, 2, 4]
print s.spiralOrder([[1, 2], [3, 4]])  # [1, 2, 4, 3]
print s.spiralOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])  # [1,2,3,6,9,8,7,4,5].
print s.spiralOrder([
    [1, ],
    [4, ],
    [7, ]
])  # [1,4,7].
