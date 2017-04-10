#!/usr/bin/env python
# -*- coding: utf-8 -*-

# bs
# Created by yangchao 10/04/2017


def bs1(_arr, target):
    """找到target 或者target 的应该的位置"""
    _end = len(_arr)
    if _end == 0:
        return False
    _end -= 1
    _begin = 0
    while _begin <= _end:
        mid = (_begin + _end) / 2
        if _arr[mid] == target:
            return True
        if _arr[mid] < target:
            _begin = mid + 1
        elif _arr[mid] > target:
            _end = mid -1
    return False

def bs(_arr, target):
    _end = len(_arr)
    if _end == 0:
        return False, -1
    if _arr[0] > target:
        return False, -1
    _end -= 1
    if _arr[_end] < target:
        return False, _end
    _begin = 0
    while _begin <= _end:
        mid = (_begin + _end) / 2
        if _arr[mid] == target:
            return True, mid
        if mid == _begin:
            if _arr[mid] > target:
                return False, mid-1
            return False, mid
        if _arr[mid] < target:
            _begin = mid + 1
        elif _arr[mid] > target:
            _end = mid -1



print bs([0, 1, 3], 4), 'false, 2'
print bs(range(0), 4), 'false, -2'
print bs(range(1), 4), 'false, 0'
print bs(range(2), 4), 'false, 1'
print bs(range(3), 4), 'false, 2'
print bs(range(4), 4), 'false, 3'
print bs(range(5), 4), 'true, 4'
print bs(range(6), 4), 'true, 4'
print bs(range(7), 4), 'true, 4'
print bs(range(8), 4), 'true, 4'
print bs(range(9), 4), 'true, 4'
print bs(range(9), -1), 'false, -1'
print bs(range(9), 6), 'true, 6'
print bs([1, 10, 23], 11), 'false, 1'
print bs([1, 10, 23], 3), 'false, 0'
