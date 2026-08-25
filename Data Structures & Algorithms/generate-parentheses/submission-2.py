class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # any string will be of form (A) B 
        dp: list[list[str]] = [[] for _ in range(n + 1)]

        # base case
        dp[0] = [""]
        
        # solve each sub problem incrementally
        for i in range(1, n+1):
            # A in (0...i-1), B in (i-1...0)
            for j in range(0, i):            
                for eachA, eachB in product(dp[j], dp[(i - 1) - j]):
                    dp[i].append("(" + eachA + ")" + eachB)
        
        return dp[n]