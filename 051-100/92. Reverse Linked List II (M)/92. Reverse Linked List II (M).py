#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 92. Reverse Linked List II (M)
# Created by yangchao 14/04/2017


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or m == 0 or n == 0:
            return head
        longer = ListNode(0)
        longer.next = head
        head = longer

        pre = head
        saved = head.next
        while 1:
            if m == 1:
                break
            m -= 1
            n -= 1
            head = head.next
            pre = head
            saved = head.next

        last_one = None
        next_one = None
        while 1:
            if n == 0:
                break
            n -= 1
            if next_one:
                head = next_one
            else:
                head = head.next
            next_one = head.next
            if last_one:
                head.next = last_one
            last_one = head
        saved.next = next_one
        pre.next = last_one

        return longer.next

s = Solution()

from ListNode import l1, l2, l3, l4
import copy
l = s.reverseBetween(copy.deepcopy(l2), 3, 5)
l.show() # 0->1->2->3->4->5->2
l = s.reverseBetween(copy.deepcopy(l2), 2, 4)
l.show() # 0->3->4->1->2->5->2
l = s.reverseBetween(copy.deepcopy(l2), 1, 4)
l.show() # 3->4->1->0->2->5->2
l = s.reverseBetween(l1, 0, 0)
l.show()