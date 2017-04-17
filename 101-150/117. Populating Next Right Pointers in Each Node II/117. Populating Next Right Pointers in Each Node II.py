#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 117. Populating Next Right Pointers in Each Node II
# Created by yangchao 17/04/2017


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
            if root.left and root.right:
                if last_node:
                    last_node.next = root.left
                root.left.next = root.right
                last_node = root.right
            elif root.left:
                if last_node:
                    last_node.next = root.left
                last_node = root.left
            elif root.right:
                if last_node:
                    last_node.next = root.right
                last_node = root.right

            if root.next:
                root = root.next
            else:
                last_node = None

                while 1:
                    if left_most.left:
                        root = left_most.left
                        left_most = left_most.left
                        break
                    elif left_most.right:
                        root = left_most.right
                        left_most = left_most.right
                        break
                    elif left_most.next:
                        left_most = left_most.next
                    else:
                        return

tree = TreeLinkNode(1)
tree.left = TreeLinkNode(2)
tree.right = TreeLinkNode(3)

tree.left.left = TreeLinkNode(4)
tree.right.right = TreeLinkNode(5)
s = Solution()
s.connect(tree)
a = 1