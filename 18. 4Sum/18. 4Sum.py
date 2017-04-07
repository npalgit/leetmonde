#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 18. 4Sum
# Created by yangchao 27/03/2017


class Solution(object):
    def fourSum(self, nums, target=0):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l = len(nums)
        if l < 4:
            return []
        result = []
        nums.sort()
        last1 = None
        for i in range(0, l):
            if last1 == nums[i]:
                continue
            last1 = nums[i]
            last2 = None
            for j in range(i+1, l):
                if last2 == nums[j]:
                    continue
                last2 = nums[j]
                q = target - nums[i] - nums[j]
                end = l - 1
                begin = j + 1
                last3 = None
                last4 = None
                while begin < end:
                    if last3 == nums[begin]:
                        begin += 1
                        continue
                    if last4 == nums[end]:
                        end -= 1
                        continue
                    p = nums[begin] + nums[end]
                    if p > q:
                        end -= 1
                        continue
                    if p < q:
                        begin += 1
                        continue
                    result.append([nums[i], nums[j], nums[begin], nums[end]])
                    last3 = nums[begin]
                    last4 = nums[end]
                    begin += 1
                    end -= 1
        return result

s = Solution()
print(s.fourSum([]))   # []
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
# [  [-1,  0, 0, 1], [-2, -1, 1, 2], [-2,  0, 0, 2]]
print(s.fourSum([-1,0,-5,-2,-2,-4,0,1,-2], -9))
# [  [-1,  0, 0, 1], [-2, -1, 1, 2], [-2,  0, 0, 2]]



