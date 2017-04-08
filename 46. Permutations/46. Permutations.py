#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 46. Permutations
# Created by yangchao 08/04/2017

import copy, itertools


class Solution(object):
    def __init__(self):
        self.result = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self._process([], nums, set(), len(nums))
        return self.result

    def _process(self, arr, nums, used, left):
        if left == 0 and len(arr) > 0:
            self.result.append(arr)
            return
        for i in nums:
            if i in used:
                continue
            _used = copy.deepcopy(used)
            _arr = copy.deepcopy(arr)
            _arr.append(i)
            _used.add(i)
            self._process(_arr, nums, _used, left-1)

    def permute1(self, nums):
        return list(itertools.permutations(nums))

s = Solution()
import time
print time.time()
print s.permute1(range(8))   # []
print time.time()

exit()

print s.permute([])   # []
print s.permute([1])   # [1]
print s.permute([1, 2])   # [1, 2]   [2, 1]
