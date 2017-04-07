#!/usr/bin/env python
# -*- coding: utf-8 -*-

# fb
# Created by yangchao 24/03/2017


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def x(i):
            if i % 15 == 0:
                return 'FizzBuzz'
            elif i % 3 == 0:
                return 'Fizz'
            elif i % 5 == 0:
                return 'Buzz'
            else:
                return str(i)

        return [x(i) for i in range(1, n+1)]

    def fb(self, n):
        r = ["1"]
        for i in range(2, n+1):
            if i % 15 == 0:
                r.append( 'FizzBuzz')
            elif i % 3 == 0:
                r.append( 'Fizz')
            elif i % 5 == 0:
                r.append( 'Buzz')
            else:
                r.append( str(i))
        return r

    def fb1(self, n):
        r = ["1"]
        f = 1
        b = 1
        for i in range(2, n+1):
            f += 1
            b += 1
            if f==3 and b==5:
                r.append('FizzBuzz')
                f = 0
                b = 0
            elif f==3:
                r.append('Fizz')
                f=0
            elif b==5:
                r.append('Buzz')
                b=0
            else:
                r.append(str(i))
        return r


s = Solution()
print s.fb1(15)
