#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 86. Partition List (M)
# Created by yangchao 13/04/2017
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import ListNode


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head:
            new_head = ListNode(0)
            saved = new_head
            greater_head = ListNode(0)
            saved_greater = greater_head
            while head is not None:
                if head.val < x:
                    new_head.next = ListNode(head.val)
                    new_head = new_head.next
                else:
                    greater_head.next = ListNode(head.val)
                    greater_head = greater_head.next
                head = head.next
            new_head.next = saved_greater.next
            return saved.next
        else:
            return head
