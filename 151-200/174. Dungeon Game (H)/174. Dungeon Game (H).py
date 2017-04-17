#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 174. Dungeon Game (H)
# Created by yangchao 17/04/2017


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        if m == 0:
            return 1
        n = len(dungeon[0])
        if n == 0:
            return 1
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                hp = dungeon[row][col]
                if row == m-1 and col == n-1:
                    if hp < 0:
                        dungeon[row][col] = - dungeon[row][col]
                    else:
                        hp = 0
                elif row == m - 1:
                    temp = dungeon[row][col+1] - dungeon[row][col]
                    if temp >= 0:
                        dungeon[row][col] = temp
                    else:
                        dungeon[row][col] = 0
                elif col == n - 1:
                    temp = dungeon[row+1][col] - dungeon[row][col]
                    if temp >= 0:
                        dungeon[row][col] = temp
                    else:
                        dungeon[row][col] = 0
                else:
                    _t0 = dungeon[row+1][col] - dungeon[row][col]
                    _t1 = dungeon[row][col+1] - dungeon[row][col]
                    if _t0 > _t1:
                        temp = _t1
                    else:
                        temp = _t0
                    if temp >= 0:
                        dungeon[row][col] = temp
                    else:
                        dungeon[row][col] = 0
        return dungeon[0][0] + 1



t1 = [
    [-1, 1, -1],
    [1, -1000, 5],
    [-10, 100, 4],
]  # 2

t2 = [
    [-1, 1, -1],
    [1, -1000, 5],
    [-10, 100, 4],
    [-100, -100, -44],
]  # 11

s = Solution()
print s.calculateMinimumHP([[-1], [1]]), 2
print s.calculateMinimumHP([[]]), 1
print s.calculateMinimumHP([]), 1
print s.calculateMinimumHP(t1), 2
print s.calculateMinimumHP(t2), 11