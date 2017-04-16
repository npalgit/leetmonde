#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 114. Flatten Binary Tree to Linked List (M)
# Created by yangchao 16/04/2017


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def show(self, x):
        while x:
            print x.val
            x = x.right
        print '------'

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None or (root.left is None and root.right is None):
            return

        stack = []
        start = root
        temp = TreeNode(0)
        saved = temp
        while start:
            if start.left:
                temp.right = TreeNode(start.left.val)
                temp = temp.right

                stack.append(start)
                left = start.left
                start.left = None
                start = left
            else:

                if start.right:
                    temp.right = TreeNode(start.right.val)
                    temp = temp.right

                    start = start.right
                else:
                    if len(stack) < 1:
                        root.right = saved.right
                        self.show(root)
                        return
                    start = stack.pop()





s = Solution()

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)

tree.right = TreeNode(5)
tree.right.right = TreeNode(6)

s.flatten(tree)



tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)

left = tree.left
left.left = TreeNode(4)
left.right = TreeNode(5)
left.right.right = TreeNode(9)

left = left.left
left.left = TreeNode(8)

left = left.left
left.right = TreeNode(6)

right = left.right
right.left = TreeNode(5)
right.right = TreeNode(4)

right = tree.right
right.left = TreeNode(6)
right.right = TreeNode(7)
s.flatten(tree)