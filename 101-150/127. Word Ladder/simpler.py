#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 参考网上生成 reaches 的方法
# 自己尽量砍掉不实用的字典, 变量等
# simpler
# Created by yangchao 01/04/2017
import time


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList.append(beginWord)
        word_size = len(beginWord)
        reaches = {}
        for word in wordList:
            reaches[word] = {}

        for word in wordList:
            for i in range(word_size):
                letters = [s for s in word]
                for j in range(97, 123):
                    letters[i] = chr(j)
                    new_word = ''.join(letters)
                    if new_word in reaches:
                        reaches[word][new_word] = 1
        last = {beginWord: 0}
        step = 1
        while 1:
            temp = {}
            step += 1
            for start_word in last:
                for word in reaches[start_word]:
                    if word not in temp:
                        if word == endWord:
                            return step
                        temp[word] = 0
                reaches[start_word] = {}
            if len(temp) == 0:
                    return 0
            last = temp
s = Solution()
from bigger import big_arr, big_arr2
print time.time()
print s.ladderLength("sand", "acne", big_arr)  # 11
print time.time()
print s.ladderLength("nape", "mild", big_arr2) # 6
print time.time()

print s.ladderLength("kiss",
"tusk",
["miss","dusk","kiss","musk","tusk","diss","disk","sang","ties","muss"]) # 5
print s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) # 5