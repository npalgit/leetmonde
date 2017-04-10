#!/usr/bin/env python
# -*- coding: utf-8 -*-

# hd
# Created by yangchao 24/03/2017
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        r = x ^ y
        b = bin(r)
        x = 0
        for i in b[2:]:
            x += int(i)
        print x

s = Solution()
s.hammingDistance(1, 1)