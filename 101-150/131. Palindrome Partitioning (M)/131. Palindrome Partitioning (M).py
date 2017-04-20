#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 131. Palindrome Partitioning (M)
# Created by yangchao 20/04/2017


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        l = len(s)
        if l == 0:
            return []

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
        result = []

        def find_match(start, partition, child):
            for item in group[start]:
                reach = len(item)+start
                if reach < l:
                    find_match(reach, partition+child, [item])
                elif reach == l:
                    result.append(partition+child+[item])
        find_match(0, [], [])

        return result

sl = Solution()

print sl.partition('aba')
print sl.partition('')
print sl.partition('a')
print sl.partition('aa')
print sl.partition('abacdfgdcaba')
print sl.partition('aba121ba')
print sl.partition('aba121aba')
print sl.partition('waabwswfd')
print sl.partition('cabacabac')
print sl.partition('caaaac')