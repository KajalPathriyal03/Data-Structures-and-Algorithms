class Solution:
    def generate(self, num: int) -> List[List[int]]:
        ans=[]
        res=[]
        res.append(1)
        ans.append(res.copy())
        print(ans)
        for i in range(1, num):
            res=[]
            for j in range(i+1):
                if j==0 or j==i:
                    res.append(1)
                else:
                    cur=ans[i-1][j-1]+ans[i-1][j]
                    res.append(cur)
            ans.append(res.copy())

        return ans 

