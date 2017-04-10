#!/usr/bin/env python
# -*- coding: utf-8 -*-

# solution
# Created by yangchao 25/03/2017a

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_pay = None
        for i in prices:
            if min_pay is None:
                min_pay = i
                continue
            profit = i - min_pay
            if profit > max_profit:
                max_profit = profit
            if i < min_pay:
                min_pay = i
        return max_profit

s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4])) # 4
print(s.maxProfit([7, 6, 4, 3, 1])) # 0