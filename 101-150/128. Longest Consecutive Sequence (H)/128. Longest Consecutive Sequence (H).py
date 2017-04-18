#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 128. Longest Consecutive Sequence (H)
# Created by yangchao 18/04/2017


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        _set = set(nums)
        _max = 1
        while _set:
            temp = set()
            for x in _set:
                temp.add(x)
                temp_ret = 1
                left = x - 1
                while left in _set:
                    temp_ret += 1
                    temp.add(left)
                    left -= 1

                right = x + 1
                while right in _set:
                    temp_ret += 1
                    temp.add(right)
                    right += 1
                if temp_ret > _max:
                    _max = temp_ret
                _set -= temp
                break
        return _max


s = Solution()

print s.longestConsecutive([100, 4, 1, 8, 3, 2]), 4
print s.longestConsecutive(range(10)), 10
print s.longestConsecutive([]), 0
print s.longestConsecutive([1]), 1
