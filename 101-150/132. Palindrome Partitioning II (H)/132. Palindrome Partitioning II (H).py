#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 132. Palindrome Partitioning II (H)
# Created by yangchao 21/04/2017


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l < 2:
            return 0

        ruler = [i - 1 for i in range(l + 1)]

        for i in range(1, l):
            j = 0
            while i >= j and i + j < l and s[i - j] == s[i + j]:
                ruler[i + j + 1] = min(ruler[i + j + 1], 1 + ruler[i - j])
                j += 1
            j = 0
            while i > j + 1 and i + j < l and s[i - j - 1] == s[i + j]:
                ruler[i + j + 1] = min(ruler[j + 1], 1 + ruler[i - j - 1])
                j += 1
        return ruler[l]


sl = Solution()
print sl.minCut('brbib'), 2

print sl.minCut('ymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp'), 84
print sl.minCut('ymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdf'), 42
exit()
print sl.minCut('ab')
print sl.minCut('ccbabc')
print sl.minCut('eeyey')
print sl.minCut('yeyee')
print sl.minCut(
    'hjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatkt'), 177
print sl.minCut(
    'apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracc'), 189
print sl.minCut('abacdfgdcaba')
print sl.minCut('aba121ba')
print sl.minCut('ccbabc')
print sl.minCut('caaaac')
print sl.minCut('dbbbdccbabc')

print sl.minCut('aba')
print sl.minCut('')
print sl.minCut('a')
print sl.minCut('aa')
print sl.minCut('aba121aba')
print sl.minCut('waabwswfd')
print sl.minCut('cabacabac')
print sl.minCut('caaaac')
print sl.minCut("ababababababababababababcbabababababababababababa")
print sl.minCut("ababababababababababababcbabababababababababababa1234")
a = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
print sl.minCut(a)
