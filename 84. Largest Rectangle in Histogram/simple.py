#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simple
# Created by yangchao 01/04/2017
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        l = len(heights)
        if l == 0:
            return 0
        max_area = 0
        arr = []

        top = 0
        for i in range(l):
            num = heights[i]
            arr.append(num)
            if num >= top:
                if num > max_area:
                    max_area = num
            else:
                j = 0
                while j < i:
                    j += 1
                    temp_top = arr[i-j]
                    if temp_top > num:
                        area = temp_top * j
                        if area > max_area:
                            max_area = area
                        arr[i-j] = num
                    else:
                        break
            top = num
        return max_area

import time
s = Solution()
print time.time()
print s.largestRectangleArea(range(0, 20000))
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
