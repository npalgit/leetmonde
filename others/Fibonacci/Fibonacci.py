class Fibonacci:

    # 递归
    def method1(self, n):
        if n == 0:
            return 0
        else:
            return n + self.method1(n-1)
    # 非递归
    def method2(self, n):
        sum = 0
        for i in range(1, n+1):
            sum += i
        return sum

if __name__ == '__main__':
    fb = Fibonacci()
    print fb.method1(5)
    print fb.method2(5)