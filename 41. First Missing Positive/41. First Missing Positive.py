#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 41. First Missing Positive
# Created by yangchao 31/03/2017
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 1
        l = len(nums)
        if l == 0:
            return result





# [1,2,0] return 3,
# [3,4,-1,1] return 2.
#
#

s = Solution()
print s.firstMissingPositive([-1,4,2,1,9,10]) # 3
print s.firstMissingPositive([2, 1, 1, 2, 1, 2, 1, 0]) # 3
print s.firstMissingPositive([-1, 1, 2, 3]) # 4
print s.firstMissingPositive([1, 2, 4]) # 3
print s.firstMissingPositive([1000, -1]) # 1
print s.firstMissingPositive([1,2,0])  # 3
print s.firstMissingPositive([0,1,2,0])  # 3
print s.firstMissingPositive([3,2,0])  # 1
print s.firstMissingPositive([3,4,-1,1]) # 2
print s.firstMissingPositive([2,4,6,1]) # 3
print s.firstMissingPositive(range(4)) # 4
print s.firstMissingPositive([]) # 1