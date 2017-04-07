#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 38. Count and Say
# Created by yangchao 08/04/2017


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        last_str = '1'
        n -= 1
        while n > 0:
            n -= 1
            last = last_str[0]
            l = len(last_str)
            count = 1
            for i in range(1, l):
                if last_str[i] == last:
                    count += 1
                else:
                    result.append(str(count) + last)
                    last = last_str[i]
                    count = 1
            result.append(str(count) + last)
            last_str = ''.join(result)
            result = []
        return last_str

s = Solution()
print s.countAndSay(4)  # 1211


print s.countAndSay(0)  # ''
print s.countAndSay(1)  # 1
print s.countAndSay(2)  # 11
print s.countAndSay(3)  # 21
print s.countAndSay(4)  # 1211
