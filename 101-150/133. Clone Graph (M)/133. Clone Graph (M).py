#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 133. Clone Graph (M)
# Created by yangchao 18/04/2017


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        ret = UndirectedGraphNode(node.label)
        for x in node.neighbors:
            r = self.cloneGraph(x)
            if r:
                ret.neighbors.append(r)
        return ret

