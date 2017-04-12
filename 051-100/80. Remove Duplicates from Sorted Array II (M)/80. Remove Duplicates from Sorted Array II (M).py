#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 80. Remove Duplicates from Sorted Array II (M)
# Created by yangchao 12/04/2017
# What if duplicates are allowed at most twice?


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _list = []
        ret = 0
        for i, num in enumerate(nums):
            if i > 1:
                if num == nums[i - 2]:
                    continue
            ret += 1
            _list.append(num)
        for i, x in enumerate(_list):
            nums[i] = x

        return ret

s = Solution()

print s.removeDuplicates([])  # 0
print s.removeDuplicates([1])  # 1
print s.removeDuplicates([1, 1, 1])  # 2
print s.removeDuplicates([1, 1, 2])  # 3
print s.removeDuplicates([1, 1, 2, 2])  # 4
print s.removeDuplicates([1, 1, 2, 2, 3])  # 5

