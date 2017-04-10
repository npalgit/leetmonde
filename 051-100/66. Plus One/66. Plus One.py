#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 之前写过, -> 43
# 66. Plus One
# Created by yangchao 09/04/2017


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]
        digits.reverse()
        rst = self.__with(digits, [1])
        rst.reverse()
        return rst

    def __with(self, arr1, arr2):
        l1 = len(arr1)
        l2 = len(arr2)
        if l1 == 0:
            return arr2
        if l2 == 0:
            return arr1

        length = l1
        if l1 > l2:
            for i in range(l1 - l2):
                arr2.append(0)
        elif l1 < l2:
            length = l2
            for i in range(l2 - l1):
                arr1.append(0)
        last = 0
        result = []
        for i in range(length):
            _sum = last + arr2[i] + arr1[i]
            result.append(_sum % 10)
            last = _sum / 10
        if last:
            result.append(last)
        return result