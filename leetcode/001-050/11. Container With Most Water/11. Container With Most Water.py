#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 11. Container With Most Water
# Created by yangchao 27/03/2017
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        e = len(height)-1
        b = 0
        max_area = 0
        l = e - b
        while l > 0:
            if height[e] > height[b]:
                area = height[b]*l
                b += 1
            else:
                area = height[e]*l
                e -= 1
            if area > max_area:
                max_area = area
            l = e - b
        return max_area
s = Solution()
print(s.maxArea([1, 3]))   # 1
print(s.maxArea([1, 3, 2, 5, 3])) # 9