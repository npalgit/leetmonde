#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 40. Combination Sum II
# Created by yangchao 08/04/2017


import copy
class Solution(object):
    def __init__(self):
        self.result = []
        self.length = 0
        self.unique = set()

    def combinationSum2(self, candidates, target):
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
        self.unique = set()

        # 排序
        candidates.sort()
        for i, val in enumerate(candidates):
            # 与目标值相等, 且没有负数, 至此结束
            if val == target:
                self.result.append([val])
                break
            self._process(target-val, candidates, [val], i)
        return self.result

    def _process(self, target, mapping, arr, index, val=None):
        if val:
            arr.append(val)
        if target == 0:
            t_arr = tuple(arr)
            if t_arr in self.unique:
                return False
            self.result.append(arr)
            self.unique.add(t_arr)
            return False
        if target < 0:
            return False
        for i in range(index+1, self.length):
            x = mapping[i]
            if not self._process(target-x, mapping, copy.deepcopy(arr), i, x):
                break
        return True

s = Solution()

print s.combinationSum2([10,1,2,7,6,1,5], 8)  # [[1,2,5],[1,7],[1,1,6],[2,6]]
print s.combinationSum2([2, 3, 6, 7], 7)  # [[7], [2, 2, 3]]
print s.combinationSum2([], 0)  # []
import time
print time.time()
print s.combinationSum2([8,6,4,12,5,7,3,11], 28)  # []
print time.time()



