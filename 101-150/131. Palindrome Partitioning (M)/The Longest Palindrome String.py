#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The Longest Palindrome String
# Created by yangchao 20/04/2017


class Solution:
    def run(self, s):
        l = len(s)
        if l == 0:
            return s
        _str = ['#']
        p = [1]
        for x in s:
            _str.append(x)
            _str.append('#')
            p.append(1)
            p.append(1)

        _max = 1
        _ret = [s[0]]

        for i in range(1, l * 2):
            left = i - 1
            right = i + 1
            while left >= 0 and right <= 2 * l:
                if _str[left] == _str[right]:
                    if p[i] > _max and _str[left] == '#':
                        _ret = s[left / 2: right / 2]
                        _max = p[i]
                    p[i] += 1
                    left -= 1
                    right += 1
                else:
                    break
        print '--------'
        return _max, ''.join(_ret)


sl = Solution()

print sl.run('aba')
print sl.run('')
print sl.run('a')
print sl.run('aa')
print sl.run('abacdfgdcaba')
print sl.run('aba121ba')
print sl.run('aba121aba')
print sl.run('waabwswfd')
