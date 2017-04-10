#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 84. Largest Rectangle in Histogram
# Created by yangchao 31/03/2017
import time
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        l = len(heights)
        if l == 0:
            return 0
        max_area = 0
        for i in range(l):
            min = heights[i]
            for j in range(i, l):
                if min * (l - i) <= max_area:
                    break
                if heights[j] < min:
                    min = heights[j]
                length = j-i+1
                area = min * length
                if area > max_area:
                    max_area = area
        return max_area

s = Solution()
print time.time()
print s.largestRectangleArea(range(0, 20))
print time.time()
print s.largestRectangleArea([9,8,4,9,2,6,9,0,5,4,9,5,3,8,2,9]) # 18
print s.largestRectangleArea([3,6,5,7,4,8,1,0])  # 20
print s.largestRectangleArea([4,2,0,3,2,5])  # 6
print s.largestRectangleArea([2,1,5,6,2,3])  # 10
print s.largestRectangleArea([2,1,5,6,3,3])  # 12
print s.largestRectangleArea([2,2,5,6,2,3])  # 12
print s.largestRectangleArea([])  # 0
print s.largestRectangleArea([1, 0])  # 1
print s.largestRectangleArea([0, 0])  # 0