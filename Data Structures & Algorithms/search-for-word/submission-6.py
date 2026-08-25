from itertools import product

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word

        # search for any nodes with the first letter
        for y, row in enumerate(board):
            for x, cell in enumerate(row):
                if cell == word[0]:
                    found = self.explore(x,y,1)
                    if found:
                        return True
        
        return False

    # explore neighbours for point (x,y)
    def explore(self, x, y, pos) -> bool:
        if pos == len(self.word):
            return True

        temp = self.board[y][x]
        # cover up current node
        self.board[y][x] = "#"

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if not 0 <= x + dx < len(self.board[0]):
                continue
            if not 0 <= y + dy < len(self.board):
                continue
            
            if self.board[y+dy][x+dx] == self.word[pos]:
                # explore that node
                completed = self.explore(x+dx, y+dy, pos+1)
                if completed:
                    return True

        # restore board state for backtrack
        self.board[y][x] = temp
        return False

