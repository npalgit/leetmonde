#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 74. Search a 2D Matrix (M)
# Created by yangchao 10/04/2017


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False

        def bsx(_arr, target):
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
                        return False, mid - 1
                    return False, mid
                if _arr[mid] < target:
                    _begin = mid + 1
                elif _arr[mid] > target:
                    _end = mid - 1
            return False
        _ret = bsx([matrix[row][0] for row in range(m)], target)
        if _ret[0]:
            return True
        ret = bsx(matrix[_ret[1]], target)
        return ret[0]



s = Solution()

print s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 11)  # true
print s.searchMatrix([], 0)  # False
print s.searchMatrix([[]], 0)  # False
print s.searchMatrix([[1]], 0)  # False
print s.searchMatrix([[1]], 1)  # True
print s.searchMatrix([[1], [3]], 0)  # False
print s.searchMatrix([[1], [3]], 3)  # True
print s.searchMatrix([[1, 2, 3], [4, 5, 6]], 3)  # True
print s.searchMatrix([[1, 2, 3], [5, 6, 7]], 4)  # False
print s.searchMatrix([[1, 2, 3], [5, 6, 7]], 0)  # False
print s.searchMatrix([[1, 2, 3], [5, 6, 7]], 8)  # False
print s.searchMatrix([[1, 2, 3], [5, 6, 7]], 6)  # true
print s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 30)  # true
print s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3)  # true
print s.searchMatrix([[-8,-7,-5,-3,-3,-1,1],[2,2,2,3,3,5,7],[8,9,11,11,13,15,17],[18,18,18,20,20,20,21],[23,24,26,26,26,27,27],[28,29,29,30,32,32,34]]
,-5)  # true


