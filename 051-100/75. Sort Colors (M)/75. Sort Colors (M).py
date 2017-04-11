#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 75. Sort Colors (M)
# Created by yangchao 11/04/2017


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        mapping = {0:0, 1:0, 2:0}
        for i in nums:
            mapping[i] += 1
        index = 0
        for i in [0, 1, 2]:
            for x in range(mapping[i]):
                nums[index] = i
                index += 1
        print nums

s = Solution()

print s.sortColors([0])
print s.sortColors([2, 1, 0])
print s.sortColors([0, 1, 1, 0, 2, 1])
