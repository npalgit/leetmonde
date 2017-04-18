#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 136. Single Number (E)
# Created by yangchao 17/04/2017


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for x in nums:
            ret ^= x
        return ret

s = Solution()

print s.singleNumber([1]), 1
print s.singleNumber([1, 2, 2]), 1
print s.singleNumber([23, 2, 23]), 2