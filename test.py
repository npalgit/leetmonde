#!/usr/bin/env python
# -*- coding: utf-8 -*-

# test
# Created by yangchao 12/08/2017

def re(string):
    return string[::-1]
def a(string):
    s = string.split(" ")
    if len(s) == 1:
        return re(s)
    for i in s:
        if i == s[-1]:
            return result + re(i)
        result = re(i) + " "
    return result

print a('abc bf')