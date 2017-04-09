#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 69. Sqrt(x)
# Created by yangchao 09/04/2017


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        low, high = 1, x
        while low < high:
            mid = (low + high) / 2
            if mid * mid > x:
                high = mid
            else: low = mid + 1
        return low - 1

s = Solution()
print s.mySqrt(0)   # 0
print s.mySqrt(1)   # 0
print s.mySqrt(9)   # 3