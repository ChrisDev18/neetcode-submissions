class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        solution = [[1]]

        for row in range(2, numRows + 1):
            newRow = [1 for i in range(row)]
            
            for i in range(1, row-1):
                newRow[i] = solution[row-2][i-1] + solution[row-2][i]
            
            solution.append(newRow)

        return solution