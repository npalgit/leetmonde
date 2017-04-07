#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 239. Sliding Window Maximum
# Created by yangchao 07/04/2017
import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if k == 0 or len(nums) == 0:
            return []
        result = []
        heep = []
        start = 0
        for i, val in enumerate(nums):
            while len(heep) - start > 0 and nums[heep[-1]] < val:
                heep.pop()

            heep.append(i)
            if i - heep[start] >= k:
                start += 1
            if i >= k - 1:
                result.append(nums[heep[start]])
        return result

s = Solution()
print s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)   # [3, 3, 5, 5, 6, 7]