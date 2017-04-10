#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 16. 3Sum Closest
# Created by yangchao 08/04/2017


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        if l < 3:
            return 0
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        distance = abs(target - closest)
        for i, val in enumerate(nums):
            t = target - val
            b = i + 1
            e = l - 1
            while b < e:
                temp = t - nums[b] - nums[e]
                if


s = Solution()

print s.threeSumClosest([], 1) # 0

print s.threeSumClosest([1], 2) # 1

print s.threeSumClosest([-1, 2, 1, -4], 1)  # 2