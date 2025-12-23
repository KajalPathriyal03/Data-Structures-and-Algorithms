class Solution:
    def rec(self, r1, c1, r2, c2, grid ):
        if r1>=len(grid) or c1>=len(grid[0]) or grid[r1][c1]==-1 or r2>=len(grid) or c2>=len(grid[0]) or grid[r2][c2]==-1:
            return float('-inf')
        if (r1, c1, r2, c2) in self.dp:
            return self.dp[(r1, c1, r2, c2)]
        q1=grid[r1][c1]
        q2=grid[r2][c2]
        cheries=0
        if r1==r2 and c1==c2:
            cheries+=grid[r1][c1]
            if r1==len(grid)-1 and c1==len(grid[0])-1:
                return grid[r1][c1]
            grid[r1][c1]=0

        else:
            cheries+=grid[r1][c1]+grid[r2][c2]
            grid[r1][c1]=0
            grid[r2][c2]=0

        p1=self.rec(r1+1, c1, r2+1,c2,grid )
        p2=self.rec(r1+1, c1, r2, c2+1, grid)
        p3=self.rec(r1, c1+1,r2+1, c2, grid)
        p4=self.rec(r1, c1+1, r2,c2+1, grid)
        grid[r1][c1]=q1
        grid[r2][c2]=q2

        self.dp[(r1, c1, r2, c2)]= cheries+max(max(p1, p2), max(p3,p4))
        return self.dp[(r1, c1, r2, c2)]
        # return cheries+max(max(p1, p2), max(p3,p4))
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.dp={}
        n=len(grid)
        ans=self.rec(0,0,0, 0, grid)
        if ans<0: return 0
        return ans 
        
        