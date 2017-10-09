#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Bad One
# Created by yangchao 21/04/2017


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = len(s)
        if l == 0:
            return 0

        _str = ['#']
        for x in s:
            _str.append(x)
            _str.append('#')

        group = [[] for x in s]
        for i in range(1, l * 2):
            left = i - 1
            right = i + 1
            while left >= 0 and right <= 2 * l:
                if _str[left] == _str[right]:
                    if _str[left] == '#':
                        sub_str = ''.join(s[left / 2: right / 2])
                        group[left / 2].append(sub_str)
                    left -= 1
                    right += 1
                else:
                    break
        print '---'
        print group
        _min = [l]

        def find_match(start, partition, child):
            for item in group[start]:
                reach = len(item) + start
                if reach < l:
                    find_match(reach, partition + child, [item])
                elif reach == l:
                    length = len(partition) + len(child)
                    if length < _min[0]:
                        _min[0] = length

        find_match(0, [], [])

        return _min[0]

s = Solution()
a = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
print s.minCut(a)
