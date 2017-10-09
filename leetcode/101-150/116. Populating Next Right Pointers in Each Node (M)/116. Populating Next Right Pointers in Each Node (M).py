#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 116. Populating Next Right Pointers in Each Node (M)
# Created by yangchao 17/04/2017


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return

        left_most = root
        last_node = None
        while root:
            if root.left:
                if last_node:
                    last_node.next = root.left
                root.left.next = root.right
                last_node = root.right

            if root.next:
                root = root.next
            else:
                root = left_most.left
                left_most = left_most.left
                last_node = None

tree = TreeLinkNode(1)
tree.left = TreeLinkNode(2)
tree.right = TreeLinkNode(3)

s = Solution()
s.connect(tree)
a = 1
