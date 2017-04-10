#!/usr/bin/env python
# -*- coding: utf-8 -*-

# mn
# Created by yangchao 25/03/2017
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        sum = 0
        for i in range(0, l):
            sum += i - nums[i]
        return sum + l

s = Solution()
print(s.missingNumber([0]))  # 1
print(s.missingNumber([0, 1])) # 2
print(s.missingNumber([3, 0, 1]))# 2
print(s.missingNumber([4, 3, 0, 1])) # 2
