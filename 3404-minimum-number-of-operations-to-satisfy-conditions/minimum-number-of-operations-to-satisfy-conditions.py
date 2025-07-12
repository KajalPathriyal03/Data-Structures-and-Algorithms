class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        n, m=len(grid), len(grid[0])
        prev_moves=[0 for _ in range(10)]

        
        cnt = defaultdict(int)
        for i in range(n):
            cnt[grid[i][0]]+=1
        for i in range(10):
            prev_moves[i]=n-cnt[i]

        for j in range(1, m):
            curr_moves=[0 for _ in range(10)]
            freq=defaultdict(int)
            for ind in range(n):
                freq[grid[ind][j]]+=1
            for i in range(10):
                mini=float('inf')
                for k in range(10):
                    if k==i: continue
                    mini=min(mini, prev_moves[k])
                
                curr_moves[i]=mini+n-freq[i]
            prev_moves=curr_moves
        return min(prev_moves)
        


        