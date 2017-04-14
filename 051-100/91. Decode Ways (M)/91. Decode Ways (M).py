#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 91. Decode Ways (M)
# Created by yangchao 14/04/2017


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0 or s[0] == '0':
            return 0
        all_count = 1
        solo_cnt = 1
        for index in range(1, l):
            new_code = s[index-1:index+1]
            if s[index] == '0':
                if s[index-1] == '1' or s[index-1] == '2':
                    solo_cnt, all_count = 0, solo_cnt
                else:
                    return 0
            elif s[index-1] == '0' or int(new_code) > 26:
                solo_cnt = all_count
                continue
            else:
                solo_cnt, all_count = all_count, all_count+solo_cnt
        return all_count



s = Solution()

print s.numDecodings("12211067142"), 10
print s.numDecodings("12214067142"), 0
print s.numDecodings("12214007142"), 0
print s.numDecodings(''), 0
print s.numDecodings('0'), 0
print s.numDecodings('12'), 2
