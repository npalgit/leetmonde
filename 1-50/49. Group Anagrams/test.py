#!/usr/bin/env python
# -*- coding: utf-8 -*-

# test
# Created by yangchao 08/04/2017

a = set()

a.add(1)
a.add(2)
a.add(4)
while a:
    print a
    for i in a:
        a.remove(i)
        break


import itertools

a = 'aabbc'
a = 'aaaaa'

x = list(itertools.permutations(a))
result = []
uniq = set()
for item in x:
    if item in uniq:
        continue
    uniq.add(item)
    result.append(''.join(item))
print result


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
print per(["owl", "woo"])