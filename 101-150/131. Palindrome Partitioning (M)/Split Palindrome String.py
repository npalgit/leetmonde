#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Split Palindrome String
# Created by yangchao 20/04/2017


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        print '--------'
        l = len(s)
        if l == 0:
            return []
        ret = set()
        for x in s:
            ret.add(x)
        _str = ['#']
        p = [1]
        for x in s:
            _str.append(x)
            _str.append('#')
            p.append(1)
            p.append(1)

        for i in range(1, l * 2):
            left = i - 1
            right = i + 1
            while left >= 0 and right <= 2 * l:
                if _str[left] == _str[right]:
                    if _str[left] == '#':
                        ret.add(''.join(s[left / 2: right / 2]))
                    p[i] += 1
                    left -= 1
                    right += 1
                else:
                    break
        return list(ret)

sl = Solution()

print sl.partition('aba')
print sl.partition('')
print sl.partition('a')
print sl.partition('aa')
print sl.partition('abacdfgdcaba')
print sl.partition('aba121ba')
print sl.partition('aba121aba')
print sl.partition('waabwswfd')