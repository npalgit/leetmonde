#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 14. Longest Common Prefix
# Created by yangchao 27/03/2017
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l = len(strs)
        if l == 0:
            return ''
        prefix = strs[0]
        len_prefix = len(prefix)
        for s in range(1, l):
            len_s = len(strs[s])
            if len_s < len_prefix:
                len_prefix = len_s
            for i in range(0, len_prefix):
                if prefix[i] != strs[s][i]:
                    len_prefix = i
                    break
        return prefix[0: len_prefix]


s = Solution()

print(s.longestCommonPrefix([]))  # ''
print(s.longestCommonPrefix(['', '1234']))  # ''
print(s.longestCommonPrefix(['12345', '1234']))  # '1234'
print(s.longestCommonPrefix(['123', '1234']))  # '123'
print(s.longestCommonPrefix(['123456', '134', '123']))  # '123'