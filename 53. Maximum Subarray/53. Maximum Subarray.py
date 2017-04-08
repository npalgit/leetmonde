#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 53. Maximum Subarray
# Created by yangchao 08/04/2017


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        max_sum = nums[0]
        score = nums[0]
        if score < 0:
            score = 0
        for i in nums[1:]:
            score += i
            if score > max_sum:
                max_sum = score
            if score < 0:
                score = 0
        return max_sum


s = Solution()

print s.maxSubArray([])   # 0
print s.maxSubArray([1, 2, 4, 5])  # 12
print s.maxSubArray([1, 2, -1, 5])  # 7
print s.maxSubArray([1, 2, -4, 5])  # 5
print s.maxSubArray([-5])  # -5
print s.maxSubArray([-5, 2])  # 2
print s.maxSubArray([5])  # 5
print s.maxSubArray([-2, -1])  # -1