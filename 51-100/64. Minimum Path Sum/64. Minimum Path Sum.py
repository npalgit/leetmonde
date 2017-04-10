#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 64. Minimum Path Sum
# Created by yangchao 09/04/2017


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0

        mapping = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for j in range(1, m + 1):
            for i in range(1, n + 1):
                if i == 1:
                    min = mapping[j - 1][i]
                elif j == 1:
                    min = mapping[1][i - 1]
                else:
                    min = mapping[j - 1][i]
                    if mapping[j - 1][i] > mapping[j][i - 1]:
                        min = mapping[j][i - 1]
                mapping[j][i] = min + grid[j - 1][i - 1]
        return mapping[m][n]


s = Solution()


arr = [[0,2,2,6,4,1,6,2,9,9,5,8,4,4],[0,3,6,4,5,5,9,7,8,3,9,9,5,4],[6,9,0,7,2,2,5,6,3,1,0,4,2,5],[3,8,2,3,2,8,8,7,5,9,6,3,4,5],[4,0,1,3,9,2,0,1,6,7,9,2,8,9],[6,2,7,9,0,9,5,2,7,5,1,4,4,7],[9,8,3,3,0,6,8,0,8,8,3,5,7,3],[7,7,4,5,9,1,5,0,2,2,2,1,7,4],[5,1,3,4,1,6,0,4,3,8,4,3,9,9],[0,6,4,9,4,1,5,5,4,2,5,7,4,0],[0,1,6,6,4,9,2,7,8,2,1,3,3,7],[8,4,9,9,2,3,8,6,6,5,4,1,7,9]]
print s.minPathSum(arr)   # 63
exit()
print s.minPathSum([[1, 2]])  # 3
print s.minPathSum([[1, 2], [1, 3]])  # 5
print s.minPathSum([[0, 2], [1, 3]])  # 4
print s.minPathSum([[1]])  # 1
print s.minPathSum([])  # 0
print s.minPathSum([[]])  # 0


