import math

class Solution:

    def climbStairs(self, n: int) -> int:
        return round((1.61803398874989484820 ** (n+1) - (-0.61803398874989484820) ** (n+1)) / math.sqrt(5))
