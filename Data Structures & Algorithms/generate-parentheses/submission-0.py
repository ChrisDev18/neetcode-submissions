class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # any string will be of form (A) B 
        dp: list[list[str]] = []

        # base case
        dp.append([""])
        
        # solve each sub problem incrementally
        for i in range(1, n+1):
            dp.append([])
            # A in (0...i-1), B in (i-1...0)
            for a, b in zip(range(0, i, 1), range(i-1, -1, -1)):            
                for eachA, eachB in product(dp[a], dp[b]):
                    dp[i].append("(" + eachA + ")" + eachB)
        
        return dp[n]