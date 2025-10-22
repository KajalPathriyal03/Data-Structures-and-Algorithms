
from typing import List

class Solution:
    def solve(self, board, word, i, j, ind):
        if ind == len(word):
            return True 

        if not (0 <= i < len(board) and 0 <= j < len(board[0])):
            return False
            
        if (i, j) in self.vis:
            return False

        res = False
        if word[ind] == board[i][j]:
            self.vis.add((i, j))
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for x, y in directions:
                newx = i + x
                newy = j + y

                if self.solve(board, word, newx, newy, ind + 1):
                    res = True
                    break 
            
            self.vis.discard((i, j))
        
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.vis = set()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.solve(board, word, i, j, 0):
                    return True
        return False