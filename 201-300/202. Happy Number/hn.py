#!/usr/bin/env python
# -*- coding: utf-8 -*-

# hn
# Created by yangchao 25/03/2017
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        showed = [n]
        while 1:
            a = [int(i) for i in str(n)]
            n = 0
            for i in a:
                n += i * i
            if n == 1:
                return True
            if n in showed:
                return False
            showed.append(n)

s = Solution()
print(s.isHappy(19)) # True
print(s.isHappy(11)) # False
