#!/usr/bin/env python
# -*- coding: utf-8 -*-

# zigzag
# Created by yangchao 27/03/2017

import copy
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = [copy.deepcopy( [i for i in range(0,5)]) for i in range(0, numRows)]
        l = len(s)
        k = 2*numRows - 2
        for i in range(0, l):
            q = i % k
            if q < numRows:
                result[q].append(s[i])
            else:
                result[k-q].append(s[i])
        return ''.join([''.join(r) for r in result])

s = Solution()
print(s.convert('PAYPALISHIRING', 3))
print(s.convert('PAYPALISHIRING', 1))



