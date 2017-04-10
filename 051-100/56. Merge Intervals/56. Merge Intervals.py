#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 56. Merge Intervals
# Created by yangchao 08/04/2017
# Definition for an interval.


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        l = len(intervals)
        if l == 0:
            return []

        def _cmp(a, b):
            return 1 if (a.start > b.start or (a.start == b.start and a.end < b.end)) else -1

        result = []
        intervals.sort(_cmp)

        temp_start = intervals[0].start
        max_end = intervals[0].end
        for i in intervals:
            if max_end < i.start:
                result.append(Interval(temp_start, max_end))
                temp_start = i.start
                max_end = i.end
            elif max_end < i.end:
                max_end = i.end

        result.append(Interval(temp_start, max_end))
        return result
