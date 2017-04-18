#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simpler
# G(n) =  B(n/2) XOR B(n)
# Created by yangchao 18/04/2017


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        ret = []
        l = 2 ** n
        for i in range(l):
            ret.append((i >> 1) ^ i)
        return ret

s = Solution()
print s.grayCode(0), '[0]'
print s.grayCode(2), '[0, 1, 3, 2]'
print s.grayCode(5)
print '[0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8, 24, 25, 27, 26, 30, 31, 29, 28, 20, 21, 23, 22, 18, 19, 17, 16]'
