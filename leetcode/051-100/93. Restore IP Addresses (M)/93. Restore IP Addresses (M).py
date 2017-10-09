#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 93. Restore IP Addresses (M)
# Created by yangchao 13/04/2017


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = len(s)
        if l < 4:
            return []
        layer1 = {}
        ever0 = False
        for i in range(1, 4):
            if ever0:
                break
            x = s[:i]
            intx = int(x)
            if 0 <= intx < 256:
                if intx == 0:
                    ever0 = True
                layer1[i] = x
        layer4 = {}
        for i in range(l-3, l):
            x = s[i:l]
            if s[i] == '0' and len(x) > 1:
                continue
            intx = int(x)
            if 0 <= intx < 256:
                layer4[l-i] = x


        layer2 = {}
        for length in layer1:
            one = layer1[length]
            ever0 = False
            for i in range(1, 4):
                if ever0:
                    break
                all_length = length + i
                if all_length > l - 2:
                    break
                x = s[length:all_length]
                intx = int(x)
                if 0 <= intx < 256:
                    if intx == 0:
                        ever0 = True
                    if all_length not in layer2:
                        layer2[all_length] = []
                    layer2[all_length].append([one, x])
        layer3 = {}
        for length in layer4:
            one = layer4[length]
            for i in range(1, 4):
                all_length = length + i
                if all_length > l - 2:
                    break
                x = s[l - all_length:l-length]
                intx = int(x)
                if 0 <= intx < 256:
                    if x[0] == '0' and len(x) > 1:
                        continue
                    if all_length not in layer3:
                        layer3[all_length] = []
                    layer3[all_length].append([x, one])
        ret = []
        for x in layer2:
            if l - x in layer3:
                for item1 in layer2[x]:
                    for item2 in layer3[l-x]:
                        ret.append('.'.join([item1[0], item1[1], item2[0], item2[1]]))
        return ret



s = Solution()

print s.restoreIpAddresses("010010")
print s.restoreIpAddresses('25525511135')
print s.restoreIpAddresses('0000')