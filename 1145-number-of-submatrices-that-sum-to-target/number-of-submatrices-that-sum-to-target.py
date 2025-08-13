class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m=len(matrix), len(matrix[0])
        ans=0

        for i in range(n):
            for j in range(1, m):
                matrix[i][j]+=matrix[i][j-1]
        
        ans=0
        for sc in range(m):
            for j in range(sc, m):
                mp={}
                mp[0]=1
                cs=0
                for r in range(n):
                    if sc>0:
                        cs+=matrix[r][j]-matrix[r][sc-1]
                    else:
                        cs+=matrix[r][j]
                    
                    if (cs-target) in mp:
                        ans+=mp[cs-target]
                    
                    if (cs) not in mp:
                        mp[cs]=1
                    else:
                        mp[cs]+=1
        return ans 
        