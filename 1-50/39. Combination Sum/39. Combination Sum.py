#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 39. Combination Sum
# Created by yangchao 08/04/2017


import copy
class Solution(object):
    def __init__(self):
        self.result = []
        self.length = 0

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l = len(candidates)
        if l < 1:
            return []
        self.result = []
        self.length = l

        # 排序
        candidates.sort()
        for i, val in enumerate(candidates):
            # 与目标值相等, 且没有负数, 至此结束
            if val == target:
                self.result.append([val])
                break
            # 过滤重复值, 下同
            if i > 0 and val == candidates[i-1]:
                continue
            self._process(target-val, candidates, [val], i)
        return self.result

    def _process(self, target, mapping, arr, index, val=None):
        if val:
            arr.append(val)
        if target == 0:
            self.result.append(arr)
            return False
        if target < 0:
            return False
        for i in range(index, self.length):
            x = mapping[i]
            if i >0 and mapping[i-1] == x:
                continue
            if not self._process(target-x, mapping, copy.deepcopy(arr), i, x):
                break
        return True

s = Solution()

print s.combinationSum([2, 3, 6, 7], 7)  # [[7], [2, 2, 3]]
print s.combinationSum([], 0)  # []
import time
print time.time()
print s.combinationSum([8,6,4,12,5,7,3,11], 28)  # []
print time.time()



