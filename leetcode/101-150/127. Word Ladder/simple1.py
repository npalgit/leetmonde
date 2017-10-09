#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simple1
# Created by yangchao 02/04/2017
import time
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        reaches = set(wordList)
        reaches.discard(beginWord)
        if endWord not in reaches:
            return 0
        word_size = len(beginWord)
        next_set = set()
        next_set.add(beginWord)

        last_set = set()
        last_set.add(endWord)
        step = 1
        while next_set and last_set:
            if len(next_set) < len(last_set):
                step += 1
                temp = set()
                for word in next_set:
                    for i in range(word_size):
                        for j in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = word[:i] + j + word[i + 1:]
                            if new_word in last_set:
                                return step
                            if new_word in reaches:
                                temp.add(new_word)
                if not temp:
                    return 0
                next_set = temp
                common = next_set & last_set
                if common:
                    step += 1
                    return step
                reaches -= next_set
            else:
                # 倒着
                step += 1
                temp = set()
                for word in last_set:
                    for i in range(word_size):
                        for j in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = word[:i] + j + word[i + 1:]
                            if new_word in next_set:
                                return step
                            if new_word in reaches:
                                temp.add(new_word)
                if not temp:
                    return 0
                last_set = temp
                common = next_set & last_set
                if common:
                    step += 1
                    return step
                reaches -= last_set
        return 0

from bigger import big_arr, big_arr2
s = Solution()

print s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) # 5   hit->hot->lot->log->cog

print time.time()
print s.ladderLength("a", "c", ["a", "b", 'c']) # 2
print time.time()

print s.ladderLength("sand", "acne", big_arr)  # 11
print time.time()
print s.ladderLength("nape", "mild", big_arr2) # 6
print time.time()
print s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) # 5   hit->hot->lot->log->cog
print time.time()