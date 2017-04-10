#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 76. Minimum Window Substring
# Created by yangchao 31/03/2017
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        length_string = len(s)
        length_target = len(t)
        if length_string == 0 or length_string<length_target or length_target == 0:
            return ''

        result_length = length_string + 1
        result = None

        target = {}
        for i in t:
            if i not in target:
                target[i] = {
                    'nodes': [],
                    'limit': 1,
                    'min': 0
                }
            else:
                target[i]['limit'] += 1
        left = length_target
        for i in range(0, length_string):
            letter = s[i]
            if letter not in target:
                continue
            max_index = i
            item = target[letter]
            nodes = item['nodes']
            nodes.append(i)
            length_nodes = len(nodes)
            if length_nodes < item['limit']:
                pass
            else:
                # length_nodes >= item['limit']
                item['min'] = nodes[length_nodes - item['limit']]
            if length_nodes <= item['limit']:
                left -= 1
            if left <= 0:
                min_index = length_string + 1
                for temp_letter in target:
                    temp_item = target[temp_letter]
                    if temp_item['min'] < min_index:
                        min_index = temp_item['min']
                temp_result = max_index - min_index
                if temp_result < result_length:
                    result_length = temp_result
                    result = (min_index, max_index)
        if result_length < length_string:
            return s[result[0]:result[1]+1]
        return ''

s = Solution()
print s.minWindow('adda', 'ada')  # adda
print s.minWindow('ddanc123accda', 'adc')  #cda
print s.minWindow('', '')  # ''
print s.minWindow('a', '')  # ''
print s.minWindow('', 'a')  # ''
print s.minWindow('a', 'a')  # ''




