#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 78. Subsets (M)
# Created by yangchao 11/04/2017


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        if l == 0:
            return [[]]
        ret = [[], nums]
        import itertools
        for i in range(1, l):
            for x in itertools.combinations(nums, i):
                ret.append(list(x))
        return ret

s = Solution()

print s.subsets([])  # [[]]
print s.subsets([1])  # [[], [1]]
print s.subsets([1, 2])  # [[], [1]]
print s.subsets([1, 2, 3])  # [[3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], [] ]
print s.subsets([1, 1, 3])  # [[],[3],[1],[1,3],[1],[1,3],[1,1],[1,1,3]]
