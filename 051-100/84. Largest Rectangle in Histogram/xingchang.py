#!/usr/bin/env python
# -*- coding: utf-8 -*-

# xingchang
# Created by yangchao 01/04/2017
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 84. Largest Rectangle in Histogram
# Created by xing 2017/4/1
"""
    因为矩形肯定是以某一个矩阵为最高点构建的，而这个最高点的矩形所能成的形
    就是左右两端最后一次大于等于这个数的位置
"""
import time
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # left right 保存当前元素左面第一次比这个数小的位置
        left = [i for i in range(0, len(heights))]
        right = [i for i in range(0, len(heights))]
        print time.time(), 0
        for index in range(0, len(heights)):
            for i in range(index, -1, -1):
                if heights[i] < heights[index]:
                    left[index] = i + 1
                    break
                if heights[i] > heights[index]:
                    # 比当前元素大，那么说明第一个比它小肯定也比它小，直接跳过去就行了
                    i = left[i]
                if i == 0:
                    left[index] = 0
        print time.time(), 1
        for index in range(len(heights)-1, -1, -1):
            for i in range(index+1, len(heights)):
                print i
                #index 8, i9
                if heights[i] < heights[index]:
                    print i
                    right[index] = i - 1
                    break
                if heights[i] > heights[index]:
                    # 比当前元素大，那么说明第一个比它小肯定也比它小，直接跳过去就行了
                    i = right[i]
                    print i, index, len(heights)
                if i == len(heights)-1:
                    right[index] = len(heights)-1
                print i, '-'
        print time.time(),2
        max_area = 0
        for index in range(0, len(heights)):
            area = heights[index] * (right[index] - left[index] + 1)
            if area > max_area:
                max_area = area
        print left
        print right
        return max_area
import time

s = Solution()
print time.time()
print s.largestRectangleArea(range(0, 11))
print time.time()