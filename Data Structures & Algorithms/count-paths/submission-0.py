class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[1 for i in range(n)] for i in range(m)]

        max_col = n-1
        max_row = m-1

        for row in reversed(range(m)):
            for col in reversed(range(n)):
                if row == max_row and col == max_col:
                    continue
                if row == max_row:
                    res[row][col] = res[row][col+1]
                elif col == max_col:
                    res[row][col] = res[row+1][col]
                else:
                    res[row][col] = res[row+1][col] + res[row][col+1]
        
        return res[0][0]