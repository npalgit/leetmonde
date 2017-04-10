#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 57. Insert Interval
# Created by yangchao 04/04/2017
# Definition for an interval.

# @to fix Line 25: MemoryError
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
        start = intervals[0].start
        if start > newInterval.start:
            start = newInterval.start

        end = intervals[l-1].end
        if end < newInterval.end:
            end = newInterval.end

        ruler = {i: start-10 for i in range(start, end+1)}
        intervals.append(newInterval)
        for interval in intervals:
            s = interval.start
            e = interval.end
            for i in range(s, e+1):
                if ruler[i] < e:
                    ruler[i] = e
        i = start
        result = []
        while i <= end:
            if ruler[i] < start:
                i += 1
                continue
            else:
                s = i
                e = i
                temp_max = ruler[i]
                while temp_max > e:
                    e += 1
                    if ruler[e] > temp_max:
                        temp_max = ruler[e]
                result.append(Interval(s, e))
                i = e + 1
        return result





s = Solution()

r = s.insert([Interval(2, 4), Interval(5, 7), Interval(8, 10), Interval(11, 13)], Interval(3, 8))  # [2, 10] [11, 13
show(r)
r = s.insert([], Interval(5, 7))  # [5, 7]
show(r)
r = s.insert([Interval(1, 1)], Interval(5, 7))  # [1, 1], [5, 7]
show(r)
r = s.insert([Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)], Interval(4, 9))  # [1, 2], [3, 10], [12, 16]
show(r)




