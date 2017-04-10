#!/usr/bin/env python
# -*- coding: utf-8 -*-

# solution
# Created by yangchao 25/03/2017
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        h = head
        while head.next is not None:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
        return h