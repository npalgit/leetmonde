#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simpler
# Created by yangchao 06/04/2017
from tools import Interval, show


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        l = len(intervals)
        if l < 1:
            return [newInterval]
        intervals.append(newInterval)

        def cmp(a, b):
            if a.start > b.start:
                return 1
            if a.start < b.start:
                return -1
            if a.start == b.start:
                if a.end > b.start:
                    return -1
                if a.end < b.end:
                    return 1
            return 0
        intervals.sort(cmp)
        _from = intervals[0].start
        _reach = intervals[0].end
        ret = []
        for item in intervals:
            if item.start > _reach:
                ret.append(Interval(_from, _reach))
                _from = item.start
                _reach = item.end
            elif item.end > _reach:
                _reach = item.end
        ret.append(Interval(_from, _reach))

        return ret





s = Solution()

r = s.insert([Interval(2, 4), Interval(5, 7), Interval(8, 10), Interval(11, 13)], Interval(3, 8))  # [2, 10] [11, 13
show(r)
r = s.insert([], Interval(5, 7))  # [5, 7]
show(r)
r = s.insert([Interval(1, 1)], Interval(5, 7))  # [1, 1], [5, 7]
show(r)
r = s.insert([Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)], Interval(4, 9))  # [1, 2], [3, 10], [12, 16]
show(r)