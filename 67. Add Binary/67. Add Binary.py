#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 67. Add Binary
# Created by yangchao 09/04/2017


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
        if not b:
            return a
        return str(bin(int(a, 2)+int(b, 2)))[2:]

s = Solution()

print s.addBinary('', '1')  # 0
print s.addBinary('1', '1')  # 10