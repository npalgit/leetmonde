#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 26. Remove Duplicates from Sorted Array
# Created by yangchao 28/03/2017
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l < 1:
            return 0
        tail = 0
        for i in range(1, l):
            if nums[i] == nums[tail]:
                continue
            tail += 1
            nums[tail] = nums[i]
        tail += 1
        return tail

s = Solution()
print s.removeDuplicates([1, 1, 3])  # 2  [1, 3]
print s.removeDuplicates([])  # 0  []
print s.removeDuplicates([1])  # 1  [1]