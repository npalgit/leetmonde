#!/usr/bin/env python
# -*- coding: utf-8 -*-

# nc
# Created by yangchao 24/03/2017
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        b = bin(num)
        a = ["1" for i in range(2, len(b))]
        return int(''.join(a), 2) - num

s = Solution()
print s.findComplement(5)