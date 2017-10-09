#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 33. Search in Rotated Sorted Array
# Created by yangchao 06/04/2017
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = -1
        for i, val in enumerate(nums):
            if val == target:
                return i
        return index


s = Solution()

print s.search([], 5)  # -1
print s.search([4,5,6,7,0,1,2], 4)  # 0
print s.search([4,5,6,7,0,1,2], 3)  # -1
