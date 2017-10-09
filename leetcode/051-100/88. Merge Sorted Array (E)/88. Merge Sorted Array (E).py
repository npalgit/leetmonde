#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 88. Merge Sorted Array (E)
# Created by yangchao 13/04/2017


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        print m, n
        if n == 0:
            return
        if m == 0:
            for i, x in enumerate(nums2):
                nums1[i] = x
            return

        last_postion = 0
        for x in nums2:
            if x >= nums1[m-1]:
                nums1[m] = x
                m += 1
                continue
            for i in range(last_postion, m):
                y = nums1[i]
                if x < y:
                    last_postion = i
                    break
            for i in range(m, last_postion, -1):
                nums1[i] = nums1[i-1]
            nums1[last_postion] = x
            m += 1
        print nums1
s = Solution()
s.merge([0], 0, [1], 1)
s.merge([0, 1, 2, 4, 0, 0, 0, 0, 0], 4, range(5), 5)
s.merge([0, 1, 0, 0, 0, 0, 0, 0,], 2, range(6), 6)
s.merge([0, 0, 0, 0, 0], 0, range(5), 5)
s.merge(range(4), 4, [], 0)
