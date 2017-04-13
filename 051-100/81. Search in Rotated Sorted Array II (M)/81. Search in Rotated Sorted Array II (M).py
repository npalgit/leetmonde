#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 81. Search in Rotated Sorted Array II (M)
# Created by yangchao 12/04/2017


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = len(nums)
        if l < 1:
            return False
        if nums[l-1] < target < nums[0]:
            return False
        if target == nums[l-1] or target == nums[0]:
            return True
        if target > nums[0]:
            flag = l-1
            while flag > 0:
                if nums[flag] == target:
                    return True
                if nums[flag-1] > nums[flag]:
                    break
                flag -= 1
            return self.bs(1, flag, nums, target)
        else:
            flag = 0
            while flag < l-1:
                if nums[flag] == target:
                    return True
                if nums[flag+1] < nums[flag]:
                    break
                flag += 1
            return self.bs(flag, l-2, nums, target)

    def bs(self, b, e, nums, target):
        """
        b, e 都是nums 中的下标
        """
        while b <= e:
            mid = (b + e) / 2
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                e = mid - 1
            else:
                b = mid + 1
        return False


s = Solution()
f = False
t = True
print s.search([1,1,1,1,3], 3), t   # true
print s.search([1,1,1,3,1], 3), t   # true
print s.search([1,1,3,1,1], 3), t   # true
print s.search([1,3,1,1,1], 3), t   # true
print s.search([3,1,1,1,1], 3), t   # true
print s.search([5,1,3], 2), f   # false
print s.search([1], 0), f   # false
print s.search([4, 5, 6, 7, 10, 1, 2], 8), f   # false

print s.search([4, 5, 6, 7, 0, 1, 2], 5), t   # true
print s.search([4, 5, 6, 7, 0, 1, 2], 6), t   # true
print s.search([4, 5, 6, 7, 8, 1, 2], 6), t   # true
print s.search([4, 5, 6, 7, 9, 1, 2], 6), t   # true
print s.search([4, 5, 6, 7, 10, 1, 2], 6), t   # true
print s.search([4, 5, 6, 7, 10, 1, 2], 7), t   # true
print s.search([4, 5, 6, 7, 10, 1, 2], 4), t   # true
print s.search([4, 5, 6, 7, 10, 1, 2], 1), t   # true
print s.search([4, 5, 6, 7, 10, 1, 2], 0), f  # false
print s.search([4, 5, 6, 7, 10, 1, 2], -1), f   # false


print s.search([4, 5, 6], 3), f   # False
print s.search([4, 5, 6, 7, 0, 1, 2], 3), f   # False
print s.search([4, 5, 6, 7, 0, 1, 2], 0), t   # true
print s.search([4, 5, 6, 7, 0, 1, 2], 1), t   # true
print s.search([4, 5, 6, 7, 0, 1, 2], 2), t   # true
print s.search([4, 5, 6, 7, 0, 1, 2], 3), f   # true
print s.search([4, 5, 6, 7, 0, 1, 2], 4), t  # true
print s.search([], 4), f  # false