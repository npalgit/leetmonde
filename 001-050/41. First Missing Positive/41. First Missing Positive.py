#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 41. First Missing Positive
# Created by yangchao 31/03/2017
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 1
        l = len(nums)
        if l == 0:
            return result
        index = 0
        while index < l:
            val = nums[index]
            if 0 < val <= l and nums[val - 1] != val:
                nums[val - 1], nums[index] = val, nums[val - 1]
                index -= 1
            index += 1
        for index, val in enumerate(nums):
            if val != index + 1:
                return index + 1
        return l + 1


# [1,2,0] return 3,
# [3,4,-1,1] return 2.
#
#

s = Solution()
print s.firstMissingPositive([1]), 2  # 5
print s.firstMissingPositive([1, 2]), 3  # 5


print s.firstMissingPositive([-1, 4, 2, 1, 9, 10]), 3  # 3
print s.firstMissingPositive([3, 4, -1, 1]), 2  # 2
print s.firstMissingPositive([1, 2, 3, 3, 4]), 5  # 5
print s.firstMissingPositive([1, -1]), 2  # 5
print s.firstMissingPositive([1, 0]), 2  # 5
print s.firstMissingPositive([1, 1]), 2  # 5
print s.firstMissingPositive([1, 3]), 2  # 5
print s.firstMissingPositive([1, 4]), 2  # 5

print s.firstMissingPositive([2, 1, 1, 2, 1, 2, 1, 0]), 3  # 3
print s.firstMissingPositive([-1, 1, 2, 3]), 4  # 4
print s.firstMissingPositive([1, 2, 4]), 3  # 3
print s.firstMissingPositive([1000, -1]), 1  # 1
print s.firstMissingPositive([1, 2, 0]), 3  # 3
print s.firstMissingPositive([0, 1, 2, 0]), 3  # 3
print s.firstMissingPositive([3, 2, 0]), 1  # 1
print s.firstMissingPositive([2, 4, 6, 1]), 3  # 3
print s.firstMissingPositive(range(4)), 4  # 4
print s.firstMissingPositive([]), 1  # 1
