#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 62. Unique Paths
# Created by yangchao 09/04/2017


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m * n == 0:
            return 0
        _dict = [[0 for i in range(n)] for j in range(m)]

        for i in range(n):
            _dict[0][i] = 1
        for j in range(m):
            _dict[j][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                _dict[i][j] = _dict[i-1][j] + _dict[i][j-1]
        return _dict[m-1][n-1]
s = Solution()

print s.uniquePaths(0, 0)  # 0
print s.uniquePaths(1, 1)  # 1
print s.uniquePaths(1, 2)  # 1
print s.uniquePaths(2, 2)  # 2
print s.uniquePaths(2, 3)  # 3
print s.uniquePaths(3, 3)  # 6
print s.uniquePaths(3, 4)  # 10
print s.uniquePaths(4, 4)  # 20