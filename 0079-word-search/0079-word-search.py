class Solution:
    def dfs(self, ind, r, c, board, w):
        if ind == len(w): 
            return True 
            
        if r<0 or r>=len(board) or c<0 or c>=len(board[0]) or (r, c) in self.vis:
            return False 
    
        directions=[[1, 0], [-1, 0], [0, 1], [0, -1]]

        if w[ind]==board[r][c]:
            self.vis.add((r, c))
            for x, y in directions:
                newx=x+r
                newy=y+c
                if self.dfs(ind+1, newx, newy, board, w): return True 
            self.vis.discard((r, c))
        return False 
            
    def exist(self, board: List[List[str]], word: str) -> bool:
        w=list(word)
        self.vis=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==w[0]:
                    if self.dfs(0, i, j, board, w): return True 
        return False 
        