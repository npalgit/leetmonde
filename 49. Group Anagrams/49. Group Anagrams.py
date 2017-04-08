#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 49. Group Anagrams
# Created by yangchao 08/04/2017


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapping = {}
        result = []
        for word in strs:
            temp = [0 for i in range(26)]
            for letter in word:
                temp[ord(letter)-97] += 1
            _tuple = tuple(temp)
            if _tuple in mapping:
                mapping[_tuple].append(word)
            else:
                mapping[_tuple] = [word]
        for key in mapping:
            result.append(mapping[key])
        return result

s = Solution()
import time
from bigger import a, b
print len(a)
print time.time()
print s.groupAnagrams(a)
print time.time()


print len(b)
print time.time()
print s.groupAnagrams(b)
print time.time()


print s.groupAnagrams(["owl", "woo"])  # [["owl"], ["woo"]]
print s.groupAnagrams(["tea","and","ace","ad","eat","dans"])  # [["ad"],["dans"],["ace"],["and"],["eat","tea"]]
print s.groupAnagrams([])  # []
print s.groupAnagrams(['ab'])  # [['ab']]
print s.groupAnagrams(['ab', 'ab', 'ba'])  # [['ab', 'ab', 'ba']]
print s.groupAnagrams(['ab', 'ab', 'ba', 'bd'])  # [['ab', 'ab', 'ba'], ['bd]]

