#!/usr/bin/env python
# -*- coding: utf-8 -*-

# tools
# Created by yangchao 04/04/2017

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def show(it):
    print '--------'
    for i in it:
        print i.start, i.end