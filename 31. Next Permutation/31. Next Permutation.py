#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 31. Next Permutation
# Created by yangchao 01/04/2017
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l < 1:
            return
        start = -1
        target = -1
        greater_one = nums[l-1]
        for i in range(l-1, 0, -1):
            if nums[i] > greater_one:
                greater_one = nums[i]
            if nums[i] > nums[i-1]:
                start = i-1
                target = nums[i-1]
                break
        if start == -1:
            nums.reverse()
            return nums, 1
        if start == l-1:
            nums[l-1], nums[l-2] = nums[l-2], nums[l-1]
            return nums, 2
        end = l-1
        for i in range(l-1, start, -1):
            if nums[i] <= greater_one and nums[i] > target:
                greater_one = nums[i]
                end = i
                break
        nums[start], nums[end] = nums[end], nums[start]

        for i in range(1, (l-start+1)/2):
            nums[start+i], nums[l-i] = nums[l-i], nums[start+i]
        return nums, 3


s = Solution()

print s.nextPermutation([1, 3, 4, 2])  # 1423
print s.nextPermutation([1, 5, 1])  # 5, 1, 1
print s.nextPermutation([1, 2, 3])  # 1, 3, 2
print s.nextPermutation([1, 3, 2])  # 2, 1, 3
print s.nextPermutation([3, 2, 1])  # 1, 2, 3
print s.nextPermutation([2, 1])  # 1, 2
print s.nextPermutation([1, 1, 2])  # 1, 2, 1
print s.nextPermutation([2, 1, 1])  # 1, 1, 2
print s.nextPermutation([1, 2, 3, 4])  # 1243
print s.nextPermutation([1, 2, 4, 3])  # 1324
print s.nextPermutation([1, 3, 2, 4])  # 1342
print s.nextPermutation([1, 4, 2, 3])  # 1432