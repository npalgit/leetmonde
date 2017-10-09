#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 45. Jump Game II
# Created by yangchao 04/04/2017
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        exp_position = 0
        temp_max = 0
        step = 0
        for i, item in enumerate(nums):
            temp_position = i + item
            if exp_position >= length-1:
                break
            if temp_position > temp_max:
                temp_max = temp_position

            if i == exp_position:
                exp_position = temp_max
                step += 1
        return step


s = Solution()
print s.jump([2,3,1,1,4]) # 2
print s.jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]) # 2
print s.jump([]) # 0
print s.jump([2,6,1,1,4]) # 2
print s.jump([1]) # 0
