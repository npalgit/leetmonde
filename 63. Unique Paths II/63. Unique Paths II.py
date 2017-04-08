#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 63. Unique Paths II
# Created by yangchao 09/04/2017

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        _dict = [[0 for i in range(n+1)] for j in range(m+1)]

        _dict[1][1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1] == 1 or (i == 1 and j == 1):
                    continue
                _dict[i][j] = _dict[i-1][j] + _dict[i][j-1]
        return _dict[m][n]

s = Solution()
print s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])   # 2

print s.uniquePathsWithObstacles([[0]])   # 1
print s.uniquePathsWithObstacles([[1]])   # 0
print s.uniquePathsWithObstacles([[1, 0]])   # 0
print s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])   # 2
