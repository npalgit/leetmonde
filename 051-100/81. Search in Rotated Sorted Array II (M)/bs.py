#!/usr/bin/env python
# -*- coding: utf-8 -*-

# bd
# Created by yangchao 13/04/2017




def bs(b, e, nums, target):
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


print bs(0, 10, range(11), -1)
print bs(0, 10, range(11), 0)
print bs(0, 10, range(11), 1)
print bs(0, 10, range(11), 2)
print bs(0, 10, range(11), 3)
print bs(0, 10, range(11), 4)
print bs(0, 10, range(11), 5)
print bs(0, 10, range(11), 6)
print bs(0, 10, range(11), 7)
print bs(0, 10, range(11), 8)
print bs(0, 10, range(11), 9)
print bs(0, 10, range(11), 10)
print bs(0, 10, range(11), 11)


print bs(0, 4, [0, 1, 4, 6, 9], 7)
print bs(0, 5, [0, 1, 2, 6, 7, 9], 7)
print bs(0, 0, [0, 1, 2, 6, 7, 9], 7)
print bs(0, 1, [0, 1, 2, 6, 7, 9], 7)
print bs(0, 0, [0, 7, 2, 6, 7, 9], 7)
print bs(0, 1, [0, 7, 2, 6, 7, 9], 7)
print bs(0, 0, [7, 7, 2, 6, 7, 9], 7)
print bs(0, 1, [7, 7, 2, 6, 7, 9], 7)
