import math

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        
        lcm = a * b // math.gcd(a, b)

        left, right = 1, n * min(a, b)
        while left < right:
            mid = (left + right) // 2
            
            if mid//a + mid//b - mid//lcm >= n:
                right = mid
            else:
                left = mid + 1

        return left % MOD
