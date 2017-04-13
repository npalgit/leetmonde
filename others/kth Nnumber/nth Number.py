#!/usr/bin/env python
# -*- coding: utf-8 -*-

# nth Number
# Created by yangchao 13/04/2017


class Solution:
    def findKthNumber(self, nums, k):
        l = len(nums)
        if l == 0 or l < k or k < 1:
            return -1
        location = l - k
        return self.quickFind(0, l - 1, nums, location)

    def quickFind(self, begin, end, nums, location):
        key = nums[begin]
        i = begin
        j = end
        while i < j:
            if nums[j] >= key:
                j -= 1
                continue
            if nums[i] <= key:
                i += 1
                continue
            nums[i], nums[j] = nums[j], nums[i]
        nums[begin], nums[i] = nums[i], key
        if i == location:
            return key
        if i > location:
            return self.quickFind(begin, i-1, nums, location)
        return self.quickFind(i+1, end, nums, location)

    def origin(self, nums, k):
        nums.sort()
        return nums[-k]

    def compare(self, nums, k):
        import time
        print time.time(), 0
        a = self.findKthNumber(nums, k)
        print time.time(), 1
        b = self.origin(nums, k)
        print time.time(), 2, a, b



s = Solution()

s.compare(range(1000), 999)
s.compare(range(1000, 0, -1), 900)
exit()

f = False
t = True
print s.findKthNumber([4, 6, 1, 3, 2, 7, 10, 13], 1), 13
print s.findKthNumber([9, 2, 10, 3, 4, 12, 5, 1], 1), 12
print s.findKthNumber(range(0, 10), 4), 6
print s.findKthNumber(range(100, 94, -1), 4), 97
print s.findKthNumber(range(100, 1, -2), 4), 94
print s.findKthNumber(range(0, 10, 2), 4), 2
print s.findKthNumber(range(0, 10, 1), 11), -1
print s.findKthNumber([], 1), -1
print s.findKthNumber([3, 2, 1, 4, 5, 6], 2), 5
