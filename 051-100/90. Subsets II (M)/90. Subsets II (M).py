#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 90. Subsets II (M)
# Created by yangchao 14/04/2017


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [nums]
        import itertools
        for i in range(len(nums)):
            r = itertools.combinations(nums, i)
            subset = set()
            for x in r:
                _x = list(x)
                _x.sort()
                tuple_x = tuple(_x)
                if tuple_x in subset:
                    continue
                subset.add(tuple_x)
                ret.append(_x)
        return ret


s = Solution()
print s.subsetsWithDup([])
print s.subsetsWithDup([1, 2, 2])