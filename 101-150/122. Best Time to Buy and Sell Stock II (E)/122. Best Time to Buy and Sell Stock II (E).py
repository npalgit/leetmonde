#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 122. Best Time to Buy and Sell Stock II (E)
# Created by yangchao 11/04/2017


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l < 2:
            return 0
        profit = 0
        hold = False
        prices.append(0)
        for index in range(l):
            price = prices[index]
            if hold:
                if prices[index+1] < price:
                    hold = False
                    profit += price
            else:
                if prices[index+1] > price:
                    hold = True
                    profit -= price
        return profit


s = Solution()

print s.maxProfit([]), '0'
print s.maxProfit([1]), '0'
print s.maxProfit([1, 4, 3, 7, 8]), '8'
print s.maxProfit([16, 4, 3, 7, 8]), '5'
print s.maxProfit([16, 4, 3, 7, 8, 1]), '5'
