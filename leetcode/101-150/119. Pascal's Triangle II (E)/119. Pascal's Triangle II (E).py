#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 119. Pascal's Triangle II (E)
# Created by yangchao 16/04/2017


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        ret = [1]
        for col in range(0, rowIndex+1):
            line = []
            for index in range(col+1):
                if index == 0 or index == col:
                    line.append(1)
                else:
                    sum = ret[index-1] + ret[index]
                    line.append(sum)
            ret = line
        return ret


s = Solution()

print s.getRow(1)
print s.getRow(2)
print s.getRow(3)
print s.getRow(4)
print s.getRow(5)
print s.getRow(0)