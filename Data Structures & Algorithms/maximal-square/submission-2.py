class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # opt is a 2d table where position (i,j) represents the 
        # optimal solution whose bottom-right corner is in position (i,j)
        w = len(matrix[0])
        h = len(matrix)

        opt = [[0 for j in range(w+1)] for i in range(h+1)]

        max_square = 0

        for row in range(1, h+1):
            for col in range(1, w+1):
                if matrix[row-1][col-1] == "0":
                    continue

                opt[row][col] = 1 + min(opt[row-1][col], opt[row][col-1], opt[row-1][col-1])

                if max_square < opt[row][col]:
                    max_square = opt[row][col]
        
        return max_square * max_square
        
