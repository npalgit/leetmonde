#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 4. Median of Two Sorted Arrays (H)
# Created by yangchao 12/04/2017


class Solution(object):
    def findMedianSortedArrays(self, arr1, arr2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(arr1)
        l2 = len(arr2)
        result = 0.0
        if l1 == 0 and l2 == 0:
            return result
        sum = l1 + l2

        index1 = 0
        index2 = 0
        if sum % 2 == 1:
            for i in range(0, sum / 2):
                if index1 + 1 > l1:
                    index2 += 1
                elif index2 + 1 > l2:
                    index1 += 1
                elif arr1[index1] < arr2[index2]:
                    index1 += 1
                else:
                    index2 += 1
            if index1 + 1 > l1:
                result += arr2[index2]
            elif index2 + 1 > l2:
                result += arr1[index1]
            elif arr1[index1] < arr2[index2]:
                result += arr1[index1]
            else:
                result += arr2[index2]
            return result
        else:
            for i in range(0, sum / 2 - 1):
                if index1 + 1 > l1:
                    index2 += 1
                elif index2 + 1 > l2:
                    index1 += 1
                elif arr1[index1] < arr2[index2]:
                    index1 += 1
                else:
                    index2 += 1
            for i in range(0, 2):
                if index1 + 1 > l1:
                    result += arr2[index2]
                    index2 += 1
                elif index2 + 1 > l2:
                    result += arr1[index1]
                    index1 += 1
                elif arr1[index1] < arr2[index2]:
                    result += arr1[index1]
                    index1 += 1
                else:
                    result += arr2[index2]
                    index2 += 1
            return result / 2

s = Solution()

print s.findMedianSortedArrays([1, 3], [2])    # 2.0
print s.findMedianSortedArrays([1, 3], [2, 4]) # 2.5

