#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 01backpack
# Created by yangchao 19/04/2017


class PackageItem:
    def __init__(self, weight, value, name):
        self.name = name
        self.weight = weight
        self.value = value


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def get01PackageAnswer(bag_items, bag_size):
        l = len(bag_items)
        bag_matrix = [[0 for j in range(bag_size+1)]for i in range(l)]

        for i in range(1, bag_size+1):
            for j in range(l):
                item = bag_items[j]
                if item.weight > i:
                    # i背包转不下item
                    if j == 0:
                        bag_matrix[j][i] = 0
                    else:
                        bag_matrix[j][i] = bag_matrix[j - 1][i]
                else:
                    # 将item装入背包后的价值总和
                    if j == 0:
                        bag_matrix[j][i] = item.value
                        continue
                    else:
                        item_in_bag = bag_matrix[j - 1][i - item.weight] + item.value
                    if bag_matrix[j - 1][i] > item_in_bag:
                        bag_matrix[j][i] = bag_matrix[j - 1][i]
                    else:
                        bag_matrix[j][i] = item_in_bag
        # find answer
        answers = []
        cur_size = bag_size
        value = 0
        for i in range(l-1, -1, -1):
            item = bag_items[i]
            if cur_size == 0:
                break
            if i == 0 and cur_size > 0:
                answers.append(item.name)
                value += item.value
                cur_size -= item.weight
                break
            if bag_matrix[i][cur_size] - bag_matrix[i - 1][cur_size - item.weight] == item.value:
                answers.append(item.name)
                value += item.value
                cur_size -= item.weight
        return answers, cur_size, value

s = Solution()
# 有编号分别为a,b,c,d,e的五件物品，它们的重量分别是2,2,6,5,4，它们的价值分别是6,3,5,4,6
bags = [
    PackageItem(2, 6, 'a'),
    PackageItem(2, 3, 'b'),
    PackageItem(6, 5, 'c'),
    PackageItem(5, 4, 'd'),
    PackageItem(4, 6, 'e'),
]


print s.get01PackageAnswer(bags, 10)
