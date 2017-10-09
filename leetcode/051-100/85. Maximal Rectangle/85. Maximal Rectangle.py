#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 85. Maximal Rectangle
# Created by yangchao 01/04/2017
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        l1 = len(matrix)
        if l1 == 0:
            return 0
        l2 = len(matrix[0])
        if l2 == 0:
            return 0

        max_area = 0
        mat_row = [[0 for j in range(l1)] for i in range(l2)]
        for i in range(l1):
            last = 0
            for j in range(l2):
                num = matrix[i][j]
                if num == '1':
                    last += 1
                else:
                    last = 0
                mat_row[j][i] = last
        for arr in mat_row:
            area = self.largestRectangleArea(arr)
            if area > max_area:
                max_area = area

        return max_area

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


s = Solution()

# 7
print s.maximalRectangle([[u'1', u'0', u'1', u'0', u'0'], [u'1', u'0', u'1', u'1', u'1'], [u'1', u'1', u'1', u'1', u'1'], [u'1', u'0', u'0', u'1', u'0'], [u'1', u'0', u'0', u'1', u'0'], [u'1', u'0', u'0', u'1', u'0'], [u'1', u'0', u'0', u'1', u'0']])
# 6
print s.maximalRectangle([[u'1', u'0', u'1', u'0', u'0'], [u'1', u'0', u'1', u'1', u'1'], [u'1', u'1', u'1', u'1', u'1'], [u'1', u'0', u'0', u'1', u'0'], [u'1', u'0', u'0', u'1', u'0']])