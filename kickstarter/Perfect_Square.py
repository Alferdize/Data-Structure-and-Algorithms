class Solution:
    def solve(self, n):
        def issq(x):
            return int(x ** .5) ** 2 == x
        if issq(n):
            return 1
        for x in range(1, int(n**.5)):
            if issq(n - x * x):
                return 2
        while n % 4 == 0:
            n >>= 2
        return 4 if n % 8 == 7 else 3