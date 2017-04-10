#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 70. Climbing Stairs
# Created by yangchao 09/04/2017


class Solution(object):

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        mapping = [1, 1]
        for i in range(2, n+1):
            mapping.append(mapping[i-1] + mapping[i-2])

        return mapping[n]

s = Solution()

print s.climbStairs(0)  # 1
print s.climbStairs(1)  # 1
print s.climbStairs(2)  # 2
print s.climbStairs(3)  # 3
