#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 118. Pascal's Triangle (E)
# Created by yangchao 16/04/2017


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        ret = [[1]]
        for row in range(1, numRows+1):
            line = []
            for col in range(row):
                if col == 0 or col == row-1:
                    line.append(1)
                else:
                    sum = ret[row-1][col-1] + ret[row-1][col]
                    line.append(sum)
            ret.append(line)
        return ret[1:]

s = Solution()

print s.generate(2)
print s.generate(3)
print s.generate(4)
print s.generate(5)

print s.generate(0)
print s.generate(1)