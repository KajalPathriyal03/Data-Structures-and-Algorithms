class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m=len(matrix),len(matrix[0])

        def area(nums):
            ln=len(nums)
            st=[]
            maxi=0
            for i in range(ln+1):
                while st  and (i==ln or nums[st[-1]]>=nums[i]):
                    h=nums[st[-1]]
                    st.pop()
                    w=0
                    if not st:
                        w=i
                    else:
                        w=i-st[-1]-1
                    maxi=max(maxi, h*w)
                st.append(i)
            return maxi

        ans=0
        dp=[0 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=="1":
                    dp[j]+=1
                else:
                    dp[j]=0
            
            res=area(dp)
            ans=max(ans,res)
        return ans 



        
        return ans 
            


                    



        