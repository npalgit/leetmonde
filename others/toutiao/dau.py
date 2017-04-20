#!/usr/bin/env python
# -*- coding: utf-8 -*-

# dau
# Created by yangchao 18/04/2017


diction = set()
while True:
    input_str = raw_input()
    uid = input_str.split()[0]
    if uid == '0':
        break
    else:
        print uid
        diction.add(uid)
print len(diction)