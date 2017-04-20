#!/usr/bin/env python
# -*- coding: utf-8 -*-

# operate
# Created by yangchao 19/04/2017


class Solution():
    def operate(self, nums, ops):
        _stack = []
        l = len(nums)
        l1 = len(ops)
        i = 0
        j = 0

        a = nums[i]
        while i < l - 1 and j < l1:
            op = ops[j]
            if op == '-' or op == '+':
                _stack.append((a, op))
                i += 1
                a = nums[i]

                j += 1
                continue
            elif op == '*':
                i += 1
                b = nums[i]
                a = a * b

                j += 1
                continue
            else:
                i += 1
                b = nums[i] + 0.0
                a /= b

                j += 1
                continue
        while _stack:
            b = _stack.pop()
            if b[1] == '-':
                a = b[0] - a
            elif b[1] == '+':
                a += b[0]
        return str(a)


s = Solution()
print s.operate([1, 2], ['+'])
print s.operate([1, 2, 3, 4, 6], ['+', '*', '/', '-'])
print s.operate([1, 2], ['-'])
print s.operate([1, 2], ['*'])
print s.operate([1, 2], ['/'])




