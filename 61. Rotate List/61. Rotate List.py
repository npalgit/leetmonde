#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 61. Rotate List
# Created by yangchao 09/04/2017
# 这道题题意模糊, 完全不知道想干嘛, 虾蟹的 )|
# Definition for singly-linked list.

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        if not k:
            return head
        saved = head
        slow = head

        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        k %= length
        while k:
            k -= 1
            head = head.next
        while head.next is not None:
            head = head.next
            slow = slow.next
        head.next = saved
        new_head = slow.next
        slow.next = None
        return new_head


s = Solution()

from tools import head, head1
import copy
ret = s.rotateRight(copy.deepcopy(head), 7)
ret.show()

ret = s.rotateRight(copy.deepcopy(head), 2)
ret.show()

ret = s.rotateRight(head1, 1)
ret.show()

ret = s.rotateRight(head1, 99)
ret.show()

print s.rotateRight(None, 0)
