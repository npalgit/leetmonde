#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 55. Jump Game
# Created by yangchao 08/04/2017


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        if l == 0:
            return False
        max_position = nums[0]
        for i, val in enumerate(nums):
            if max_position >= l - 1:
                return True
            temp_position = i + val
            if max_position <= i and val == 0:
                return False
            if temp_position > max_position:
                max_position = temp_position

s = Solution()

print s.canJump([])  # False
print s.canJump([0])  # True
print s.canJump([0, 1])  # False
print s.canJump([3,2,1,0,4])  # False
print s.canJump([3,2,1,1,4])  # True
