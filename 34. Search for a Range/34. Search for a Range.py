#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 34. Search for a Range
# Created by yangchao 06/04/2017
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1, -1]
        l = len(nums)
        if l == 0:
            return result
        b = 0
        e = l
        while b < e:
            start = (b + e) / 2
            if nums[start] == target:
                left = start - 1
                if left > -1:
                    if nums[left] < target:
                        result[0] = start
                        break
                    else:
                        e = start
                        continue
                else:
                    result[0] = start
                    break
            elif nums[start] > target:
                e = start
            else:
                if b == start:
                    break
                b = start
        if result[0] == -1:
            return result
        b = result[0]
        e = l
        while b < e:
            end = (b + e) / 2
            if nums[end] == target:
                right = end + 1
                if right < l:
                    if nums[right] > target:
                        result[1] = end
                        break
                    else:
                        b = end
                        continue
                else:
                    result[1] = end
                    break
            elif nums[end] > target:
                e = end
            else:
                b = end
        return result


s = Solution()

print s.searchRange([], 0)  # [-1, -1]
print s.searchRange([1, 1, 1], 0)  # [-1, -1]
print s.searchRange([1, 1, 1], 1)  # [0, 2]
print s.searchRange([0, 1, 1, 1, 2, 2], 1)  # [1, 3]
print s.searchRange([2, 2], 3)  # [0, 1]
print s.searchRange([2, 2], 1)  # [0, 1]
