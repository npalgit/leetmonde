#!/usr/bin/env python
# -*- coding: utf-8 -*-

# tree
# Created by yangchao 07/04/2017


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def show(self):
        print '------->'
        self._process(self, 0)
        print '<-------'

    def _process(self, node, width):
        if node is None:
            return
        print ''.join([' 'for i in range(width)]), node.val
        self._process(node.left, width+4)
        self._process(node.right, width+4)


t1 = TreeNode(10)
t1.right = TreeNode(12)
t1.left = TreeNode(11)

t2 = TreeNode(10)
t2.right = TreeNode(11)
t2.left = TreeNode(10.5)
t2.right.left = TreeNode(9)

