#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 95. Unique Binary Search Trees II (M)
# Created by yangchao 14/04/2017
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def show(self, _root=''):
        return
        if _root == '':
            _root = self
        if _root is None:
            return
        self.show(_root.left)
        print _root.val
        self.show(_root.right)


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.process(range(1, 1+n))

    def process(self, arr):
        l = len(arr)
        if l == 0:
            return [None]
        if l == 1:
            return [TreeNode(arr[0])]
        ret = []

        for i in range(0, l):
            left_ret = self.process(arr[:i])
            right_ret = self.process(arr[i + 1:])

            for x in left_ret:
                for y in right_ret:
                    node = TreeNode(arr[i])
                    node.left = x
                    node.right = y
                    ret.append(node)
        return ret

s = Solution()


r = s.generateTrees(2)
print '---------', 2, len(r), 2


r = s.generateTrees(3)
print '---------', 3, len(r), 5


r = s.generateTrees(0)
print '---------', 0, len(r), 0



r = s.generateTrees(1)
print '---------', 1, len(r), 1




r = s.generateTrees(4)
print '---------', 4, len(r), 14




r = s.generateTrees(5)
print '---------', 5, len(r), 42





