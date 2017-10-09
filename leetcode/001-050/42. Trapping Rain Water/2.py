#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2
# Created by yangchao 04/08/2017


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        if l < 3:
            return 0
        right = height[0]
        ret = 0
        right_index = 0
        for i in range(1, l):
            h = height[i]
            if h >= right:
                for j in range(right_index, i):
                    ret += right - height[j]
                right = h
                right_index = i
        left_index = l-1
        left = height[left_index]
        for i in range(left_index, right_index-1, -1):
            h = height[i]
            if h > left:
                for j in range(left_index, i, -1):
                    ret += left - height[j]
                left = h
                left_index = i
        return ret

if __name__ == '__main__':
    s = Solution()
    print s.trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6
    print s.trap([4, 2, 3]), 1
    print s.trap([2, 0, 2]), 2