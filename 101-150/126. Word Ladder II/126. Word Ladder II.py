#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 126. Word Ladder II
# Created by yangchao 03/04/2017
import time
import copy
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
        paths_front = {beginWord: []}
        paths_end = {endWord: []}
        common_result = set()
        while next_set and last_set:
            common_result = set()
            if len(next_set) < len(last_set):
                temp = set()
                for word in next_set:
                    for i in range(word_size):
                        for j in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = word[:i] + j + word[i + 1:]
                            if new_word in last_set:
                                path = copy.deepcopy(paths_front[word])
                                path.append(word)
                                paths_front[new_word] = path
                                common_result.add(new_word)
                            elif new_word in reaches:
                                path = copy.deepcopy(paths_front[word])
                                path.append(word)
                                paths_front[new_word] = path
                                temp.add(new_word)
                if common_result:
                    break
                if not temp:
                    return []
                next_set = temp
                common_result = next_set & last_set
                if common_result:
                    break
                reaches -= next_set
            else:
                # 倒着
                temp = set()
                for word in last_set:
                    for i in range(word_size):
                        for j in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = word[:i] + j + word[i + 1:]
                            if new_word in next_set:
                                path = copy.deepcopy(paths_end[word])
                                path.append(new_word)
                                paths_end[new_word] = path
                                common_result.add(new_word)
                            elif new_word in reaches:
                                path = copy.deepcopy(paths_end[word])
                                path.append(new_word)
                                paths_end[new_word] = path
                                temp.add(new_word)
                if common_result:
                    break
                if not temp:
                    return []
                last_set = temp
                common_result = next_set & last_set
                if common_result:
                    break
                reaches -= last_set
        result = []
        for common_word in common_result:
            temp = []
            for word in paths_front[common_word]:
                temp.append(word)
            temp_list = paths_end[common_word]
            for i in range(len(temp_list)-1, -1, -1):
                temp.append(temp_list[i])
            result.append(temp)
        print len(temp)
        return result

from bigger import big_arr, big_arr2
s = Solution()
print time.time()
print s.ladderLength("a", "c", ["a", "b", 'c']) # 2

print s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) # 5   hit->hot->lot->log->cog

print time.time()

print s.ladderLength("sand", "acne", big_arr)  # 11
print time.time()
print s.ladderLength("nape", "mild", big_arr2) # 6
print time.time()
print s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) # 5   hit->hot->lot->log->cog
print time.time()