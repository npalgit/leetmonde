#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 43. Multiply Strings
# Created by yangchao 08/04/2017


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        if l1 == 0 or l2 == 0 or num1[0] == '0' or num2[0] == '0':
            return '0'
        result = []
        last = 0
        for i in range(l1-1, -1, -1):
            x = int(num1[i])
            last = 0
            temp = [0 for n in range(l1 - 1 - i)]
            for j in range(l2-1, -1, -1):
                y = int(num2[j])
                product = last + x * y
                temp.append(product % 10)
                last = product / 10
            if last:
                temp.append(last)
            result = self.__with(result, temp)
        result.reverse()
        return ''.join([str(x) for x in result])

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






s = Solution()
print s.multiply('157', '16')  # 2512
print s.multiply('16', '157')  # 2512

print s.multiply('0', '')  # 0
print s.multiply('0', '0')  # 0
print s.multiply('10', '0')  # 0
print s.multiply('10', '2')  # 20