#!/usr/bin/env python
# -*- coding: utf-8 -*-

# daomu
# Created by yangchao 26/04/2017

class Daomu:
    def run(self, nums):
        start = (0, 0)
        end = (nums[0], nums[1])
        n = nums[2]
        lasers = []
        f = []
        for i in range(3, 3+n*4, 4):
            lasers.append((nums[i], nums[i+1], nums[i+2], nums[i+3]))
            if nums[i] != nums[i+2]:
                f.append((
                    (nums[i+3]-nums[i+1])/(nums[i]-nums[i+2]+0.0),
                    (nums[i+3]-nums[i+1])/(nums[i+2]-nums[i]+0.0)*nums[i]-nums[i+1],
                    min([nums[i], nums[i+2]]),
                    max([nums[i], nums[i+2]]),
                ))
            else:
                f.append((None, nums[i], nums[i+1], nums[i+3]))
        print lasers
        print f






d = Daomu()
nums = [100, 80, 3, 10, 2, 8, 25, 44, 12, 6, 6, 5, 6, 10, 51]
print d.run(nums)
