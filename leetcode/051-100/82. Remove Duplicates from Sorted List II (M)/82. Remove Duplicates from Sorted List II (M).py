#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 82. Remove Duplicates from Sorted List II (M)
# Created by yangchao 13/04/2017
from ListNode import ListNode, l1, l2, l3

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            last = head.val
            arr = [last]
            oops = False
            while head.next is not None:
                head = head.next
                if head.val == last:
                    oops = True
                else:
                    if oops:
                        if len(arr) > 0:
                            arr.pop()
                    arr.append(head.val)
                    oops = False
                last = head.val
            if oops:
                arr.pop()
            ret = ListNode(0)
            saved = ret
            for x in arr:
                ret.next = ListNode(x)
                ret = ret.next
            return saved.next
        else:
            return head

s = Solution()

r = s.deleteDuplicates(l1)
r.show()
r = s.deleteDuplicates(l2)
r.show()
r = s.deleteDuplicates(l3)
r.show()