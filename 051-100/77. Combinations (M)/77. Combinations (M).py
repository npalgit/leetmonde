#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 77. Combinations (M)
# Created by yangchao 11/04/2017

class Solution(object):
    def combine1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 0 or k > n:
            return []
        ret = []
        default_arr = range(0, n+1)

        import copy
        def _com(arr, index):
            if len(arr) == k:
                ret.append(arr)
            for i in default_arr[index:]:
                _arr = copy.deepcopy(arr)
                _arr.append(i)
                _com(_arr, i+1)
        _com([], 1)
        return ret

    def combine(self, n, k):
        import itertools
        if n == 0 or k > n:
            return []
        ret = []
        for x in itertools.combinations(range(1, n+1), k):
            ret.append(list(x))

        return ret


s = Solution()
print s.combine(0, 0), '[]'
print s.combine(4, 2), '[[1,2], [1,3], [1,4], [2, 3], [2, 4], [3, 4]]'
print s.combine(4, 6), '[]'
print s.combine(20, 4), '[]'
