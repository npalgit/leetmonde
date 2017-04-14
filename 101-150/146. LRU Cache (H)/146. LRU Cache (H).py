#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 146. LRU Cache (H)
# Created by yangchao 14/04/2017


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.container = {}
        self.oldest = None
        self.newest = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.container:
            old_one = self.container[key]['old']
            new_one = self.container[key]['new']
            size = len(self.container)
            if self.newest == key or size == 1:
                return self.container[key]['val']

            if self.oldest == key:
                self.container[key]['old'] = self.newest
                self.container[self.newest]['new'] = key

                self.newest = key
                self.container[key]['new'] = None

                self.oldest = new_one
                self.container[new_one]['old'] = None
            else:
                self.container[key]['old'] = self.newest
                self.container[self.newest]['new'] = key

                self.newest = key
                self.container[key]['new'] = None

                self.container[old_one]['new'] = new_one
                self.container[new_one]['old'] = old_one

            return self.container[key]['val']
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.container:
            self.container[key]['val'] = value
            self.get(key)
        elif self.capacity == 0:
            temp_oldest = self.container[self.oldest]['new']
            self.container.pop(self.oldest)
            if len(self.container) == 0:
                self.capacity += 1
                self.newest = None
                self.put(key, value)
                return
            self.oldest = temp_oldest
            self.container[self.oldest]['old'] = None

            self.container[self.newest]['new'] = key

            self.container[key] = {
                'val': value,
                'old': self.newest,
                'new': None
            }
            self.newest = key
        else:
            self.capacity -= 1
            if self.newest:
                self.container[self.newest]['new'] = key
                self.container[key] = {
                    'val': value,
                    'old': self.newest,
                    'new': None
                }
                self.newest = key
            else:
                self.container[key] = {
                    'val': value,
                    'old': self.newest,
                    'new': None
                }
                self.newest = key
                self.oldest = key


print '----'
cache = LRUCache(3)
print cache.put(1, 1), None
print cache.put(2, 3), None
print cache.put(3, 3), None
print cache.put(4, 4), None
print cache.get(4), 4
print cache.get(3), 3
print cache.get(2), 3
print cache.get(1), -1
print cache.put(5, 5), None
print cache.get(1), -1
print cache.get(2), 3
print cache.get(3), 2
print cache.get(4), -1
print cache.get(5), 5
print '----'
cache = LRUCache(1)
print cache.put(2 ,1), None
print cache.get(2), 1
print cache.put(3, 2), None
print cache.get(2), -1
print cache.get(3), 2
print '-----'
cache = LRUCache(2)
print cache.put(1, 1), None
print cache.put(2, 2), None
print cache.get(1), 1
print cache.put(3, 3), None
print cache.get(2), -1
print cache.put(4, 4), None
print cache.get(1), -1
print cache.get(3), 3
print cache.get(4), 4
print '----'
cache = LRUCache(1)
print cache.put(2 ,1), None
print cache.get(2), 1
print cache.put(3, 2), None
print cache.get(2), -1
print cache.get(3), 2