#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 42. Trapping Rain Water
# Created by yangchao 03/04/2017
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        if l < 3:
            return 0
        result = 0

        temp_max = 0
        temp_area = 0
        last_max = l
        for i in range(l):
            h = height[i]
            if h >= temp_max:
                result += temp_area
                temp_area = 0
                temp_max = h
                last_max = i
                continue
            temp_area += temp_max - h
        temp_max = 0
        temp_area = 0
        for i in range(l-1, last_max-1, -1):
            h = height[i]
            if h >= temp_max:
                result += temp_area
                temp_area = 0
                temp_max = h
                last_max = i
                continue
            temp_area += temp_max - h
        return result

s = Solution()
print s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) # 6
print s.trap([4, 2, 3]) # 1
