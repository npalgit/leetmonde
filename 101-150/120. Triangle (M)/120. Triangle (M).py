#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 120. Triangle (M)
# Created by yangchao 17/04/2017


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        if m == 0:
            return 0
        ret = triangle[0][0]
        for row in range(1,m):
            for col in range(row+1):
                if col == 0:
                    triangle[row][col] += triangle[row-1][col]
                    ret = triangle[row][col]
                elif col == row:
                    triangle[row][col] += triangle[row - 1][col-1]
                    if ret > triangle[row][col]:
                        ret = triangle[row][col]
                else:
                    _min = triangle[row-1][col-1]
                    if triangle[row-1][col-1] > triangle[row-1][col]:
                        _min = triangle[row-1][col]
                    triangle[row][col] += _min
                    if ret > triangle[row][col]:
                        ret = triangle[row][col]
        return ret

s = Solution()
print s.minimumTotal([]), 0
print s.minimumTotal([[1],[2, 3],[5,4,1]]), 5
print s.minimumTotal([[-1],[2,3],[1,-1,-1]]), 0