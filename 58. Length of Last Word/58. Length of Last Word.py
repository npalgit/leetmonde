#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 58. Length of Last Word
# Created by yangchao 08/04/2017


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        l = len(s)
        if l == 0:
            return 0
        arr = s.split(' ')
        _l = len(arr)
        if _l == 0:
            return 0
        return len(arr[_l-1])

s = Solution()
print s.lengthOfLastWord('')   # 0
print s.lengthOfLastWord('  ')   # 0
print s.lengthOfLastWord(' aa ')   # 2
print s.lengthOfLastWord(' aa ab ')   # 2