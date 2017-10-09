#!/usr/bin/env python
# -*- coding: utf-8 -*-

# better
# Created by yangchao 07/04/2017

import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]],
        return out

s = Solution()
print s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)   # [3, 3, 5, 5, 6, 7]

