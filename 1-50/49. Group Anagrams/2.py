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
        last = set()
        for word in strs:
            if word in mapping:
                mapping[word] += 1
            else:
                last.add(word)
                mapping[word] = 1

        def per(_strs):
            # type: (list) -> list
            _key = _strs[0]
            _result = [_key]
            _letter_dict = {}
            for _letter in _key:
                if _letter in _letter_dict:
                    _letter_dict[_letter] += 1
                else:
                    _letter_dict[_letter] = 1
            _length = len(_key)
            for _w in _strs[1:]:
                if len(_w) != _length:
                    continue
                _temp_dict = {}
                _matched = True
                for _letter in _w:
                    if _letter not in _letter_dict:
                        _matched = False
                        break
                    if _letter in _temp_dict:
                        if _temp_dict[_letter] == _letter_dict[_letter]:
                            _matched = False
                            break
                        _temp_dict[_letter] += 1
                    else:
                        _temp_dict[_letter] = 1
                if _matched:
                    _result.append(_w)
            return _result


        result = []
        while last:
            _arr = list(last)
            _temp = []
            per_arr = per(_arr)
            for x in per_arr:
                if x in last:
                    last.remove(x)
                    for i in range(mapping[x]):
                        _temp.append(x)
            result.append(_temp)
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

