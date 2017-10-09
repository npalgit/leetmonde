#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 27. Remove Element
# Created by yangchao 28/03/2017
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = len(nums)
        if l < 1:
            return l
        last = 0
        for i in range(0, l):
            if nums[i] == val:
                continue
            elif i != last:
                nums[i], nums[last] = nums[last], nums[i]
            last += 1
        return last

s = Solution()
print(s.removeElement([3, 2, 2, 3], 3))
print(s.removeElement([1, 2, 2, 3], 3))
print(s.removeElement([3, 3, 3, 2], 3))
print(s.removeElement([2], 3))
print(s.removeElement([], 3))