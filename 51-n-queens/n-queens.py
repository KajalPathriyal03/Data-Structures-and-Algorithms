class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board=[["." for _ in range(n)] for _ in range(n)]

        def isSafe(row,col):
            dup_row=row
            dup_col=col
            while row>=0 and col>=0:
                if board[row][col]=="Q":
                    return False
                row-=1
                col-=1
            
            row=dup_row
            col=dup_col
            while col>=0:
                if board[row][col]=="Q":
                    return False
                col-=1

            row=dup_row
            col=dup_col

            while row<n and col>=0:
                if board[row][col]=="Q":
                    return False
                row+=1
                col-=1
            return True

        def solve(col):
            if col==n:
                cnt=[]
                for i in range(n):
                    res="".join(board[i])
                    cnt.append(res)                        
                ans.append(cnt.copy())
                return 
            for row in range(n):
                if isSafe(row, col):
                    board[row][col]="Q"
                    solve(col+1)
                    board[row][col]="."

        solve(0)
        return ans



        