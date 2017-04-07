#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 493. Reverse Pairs
# Created by yangchao 29/03/2017
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        mapping = {}
        i = 0
        for item in nums:
            if item in mapping:
                mapping[item].append(i)
            else:
                mapping[item] = [i]
            i += 1
        keys = mapping.keys()
        keys.sort()
        length = len(keys)
        # 上个数开始的位置
        last_position = length - 1
        result = 0
        for i in range(length - 1, -1, -1):
            bigger = keys[i] / 2.0
            for j in range(last_position, -1, -1):
                if bigger <= keys[j]:
                    last_position -= 1
                    continue
                # 大小符合, 判断坐标是否符合
                big_collection = mapping[keys[i]]
                for k in range(0, last_position + 1):
                    collection = mapping[keys[k]]
                    for index in collection:
                        for big_index in big_collection:
                            if big_index < index:
                                result += 1
                break
        return result

    def reversePairs2(self, nums):
        l = len(nums)
        if l == 0:
            return 0
        result = 0
        mapping = {
            nums[l-1]: {
                'key': nums[l-1],
                'val': 1,
                'next': None,
                'last': None,
            }
        }
        head = nums[l-1]
        for i in range(l-2, -1, -1):
            item = nums[i]
            bigger = item/2.0
            if item not in mapping:
                mapping[item] = {
                    'key': item,
                    'val': 0,
                    'next': None,
                    'last': None,
                }
                if head < item:
                    mapping[head]['last'] = item
                    mapping[item]['next'] = head
                    mapping[item]['val'] = mapping[head]['val']
                    head = item
                else:
                    temp = head
                    while 1:
                        mapping[temp]['val'] += 1
                        if mapping[temp]['next'] is None:
                            mapping[temp]['next'] = item
                            mapping[item]['last'] = temp
                            break
                        temp = mapping[temp]['next']
                        if temp < item:
                            last = mapping[temp]['last']
                            mapping[last]['next'] = item
                            mapping[item]['last'] = last
                            mapping[item]['next'] = temp
                            mapping[item]['val'] = mapping[temp]['val']
                            mapping[temp]['last'] = item
                            break
            else:
                temp = mapping[item]['last']
                while temp is not None:
                    mapping[temp]['val'] += 1
                    temp = mapping[temp]['last']

            if bigger < 0: # mapping[item]['key']
                result += mapping[item]['val']
            else:
                next = mapping[item]['next']
                if next is not None:
                    result += mapping[next]['val']
                    print next, mapping[next], item
            mapping[item]['val'] += 1
        print mapping, head
        return result


s = Solution()
print s.reversePairs2([2, 4, 3, 5, 1])  # 3
#print s.reversePairs2([1, 3, 2, 3, 1])  # 2
#print s.reversePairs2([-5, -5, -4])  # 3
#print s.reversePairs2([-5, -5])  # 1
#print s.reversePairs2([0, -5, -5])  # 3
