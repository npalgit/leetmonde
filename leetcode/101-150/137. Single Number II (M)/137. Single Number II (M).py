#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 137. Single Number II (M)
# Created by yangchao 09/05/2017

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        once = 0
        twice = 0
        for i in nums:
            once ^= i & (~twice)
            twice ^= i & (~once)
        return once


s = Solution()

print s.singleNumber([1, 2, 1, 1]), 2
