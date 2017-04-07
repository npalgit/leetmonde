#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 149. Max Points on a Line
# Created by yangchao 07/04/2017

#Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
