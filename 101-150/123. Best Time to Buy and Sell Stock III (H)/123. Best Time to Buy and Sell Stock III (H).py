#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 123. Best Time to Buy and Sell Stock III (H)
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
        max_profit = [0, 0]
        min_price = prices[0]
        temp_profit = 0
        prices.append(0)
        for index in range(1, l):
            price = prices[index]

            profit = price - min_price
            if profit > temp_profit:
                temp_profit = profit

            if price <= min_price or price >= prices[index+1]:
                if temp_profit >= max_profit[1]:
                    max_profit[0], max_profit[1] = max_profit[1], temp_profit
                elif max_profit[0] < temp_profit < max_profit[1]:
                    max_profit[0] = temp_profit
                temp_profit = 0
                min_price = price

        return max_profit[0] + max_profit[1]

s = Solution()
print s.maxProfit([1,2,4,2,5,9,4,4,9,0])   # 13
print s.maxProfit([1,2,4,2,5,7,2,4,9,0])   # 13
print s.maxProfit([1, 2, 4])   # 3
print s.maxProfit([6,1,3,2,4,7])   # 7
print s.maxProfit([6,2,8,7,4,15])   # 17
print s.maxProfit([6,2,8,8,9,15])   # 13
print s.maxProfit([6,1,5,2,4,7])   # 9
print s.maxProfit([2, 1, 2, 0, 1])   # 2

print s.maxProfit([])   # 0
print s.maxProfit([1])   # 0
print s.maxProfit([1, 2])   # 1
print s.maxProfit([3, 2])   # 0
print s.maxProfit([3, 2, 5, 1, 6])   # 8
print s.maxProfit([3, 2, 5, 1, 2])   # 4
