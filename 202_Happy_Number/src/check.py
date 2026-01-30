class Solution:
    def check(self, n: int) -> int:
        sum = 0
        while n > 0:
            last = n % 10
            sum += last ** 2
            n //= 10
        return sum

    def isHappy(self, n: int) -> bool:
        result = set()
        while n > 0:
            sum = self.check(n)
            if sum == 1:
                return True
            if sum in result:
                return False
            result.add(sum)
            n = sum
        return False
