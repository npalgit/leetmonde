#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 96. Unique Binary Search Trees (M)
# Created by yangchao 14/04/2017


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        ret = [1, 1, 2, 5]
        for i in range(4, n+1):
            ret.append(0)
            for j in range(0, i):
                ret[i] += ret[j]*ret[i-j-1]

        return ret[n]

s = Solution()

print s.numTrees(0), 0
print s.numTrees(1), 1
print s.numTrees(2), 2
print s.numTrees(3), 5
print s.numTrees(4), 14
print s.numTrees(5), 42
print s.numTrees(6), 132
