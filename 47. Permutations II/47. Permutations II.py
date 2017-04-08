#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 47. Permutations II
# Created by yangchao 08/04/2017
import copy, itertools


class Solution(object):
    def __init__(self):
        self.result = []

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        mapping = {}
        for i in nums:
            if i in mapping:
                mapping[i] += 1
            else:
                mapping[i] = 1
        self.result = []
        self._process([], nums, mapping, len(nums))
        return self.result

    def _process(self, arr, nums, used, left):
        if left == 0 and len(arr) > 0:
            self.result.append(arr)
            return
        for index, i in enumerate(nums):
            if index > 0:
                if nums[index-1] == i:
                    continue
            if used[i] == 0:
                continue
            _used = copy.deepcopy(used)
            _arr = copy.deepcopy(arr)
            _arr.append(i)
            _used[i] -= 1
            self._process(_arr, nums, _used, left-1)

    def permute1(self, nums):
        return list(itertools.permutations(nums))

s = Solution()
print s.permuteUnique([1, 2, 1])  # [1, 1, 2], [1, 2, 1], [2, 1, 1]

print s.permuteUnique([])   # []
print s.permuteUnique([1])   # [1]
print s.permuteUnique([1, 2])   # [1, 2]   [2, 1]
