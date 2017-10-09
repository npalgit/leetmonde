#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 297. Serialize and Deserialize Binary Tree (H)
# Created by yangchao 17/04/2017


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return 'N'
        ret = [str(root.val)]
        last = [root]
        while last:
            temp = []
            for x in last:
                if x.left is None:
                    ret.append('N')
                else:
                    ret.append(str(x.left.val))
                    temp.append(x.left)
                if x.right is None:
                    ret.append('N')
                else:
                    ret.append(str(x.right.val))
                    temp.append(x.right)
            last = temp
            ret.append('L')
        return ','.join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data or data == 'N':
            return None
        arr = data.split(',')

        root = TreeNode(arr[0])
        last = [root]
        index = 0
        temp = []
        i = 0
        for letter in arr[1:]:
            i += 1
            if letter == 'N':
                if i % 2:
                    last[index].left = None
                else:
                    last[index].right = None
                    index += 1
            elif letter == 'L':
                last = temp
                temp = []
                i = 0
                index = 0
            else:
                node = TreeNode(int(letter))
                temp.append(node)
                if i % 2:
                    last[index].left = node
                else:
                    last[index].right = node
                    index += 1
        return root

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.left.right = TreeNode(7)
tree.left.left.right.left = TreeNode(10)

tree.right = TreeNode(4)
right = tree.right
right.left = TreeNode(5)
right.left.left = TreeNode(8)
right.left.left.right = TreeNode(12)

right = tree.right
right.right = TreeNode(6)
right.right.right = TreeNode(9)
right.right.right.left = TreeNode(13)
right.right.right.right = TreeNode(14)

s = Codec()
a = s.serialize(None)
print a
b = s.deserialize(a)
a = a