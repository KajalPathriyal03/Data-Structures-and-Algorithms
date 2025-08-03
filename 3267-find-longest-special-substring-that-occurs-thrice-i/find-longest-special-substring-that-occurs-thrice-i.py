class Solution:
    def maximumLength(self, s: str) -> int:
        n=len(s)
        st=defaultdict(int)
        for i in range(n):
            cur=""
            for j in range(i, n):
                if cur==""  or  cur[-1]==s[j]:
                    cur+=s[j]
                    st[cur]+=1
                    # print(cur)
                else:
                    break
        maxi=-1
        for ele, cnt in st.items():
            if cnt>=3:
                maxi=max(maxi, len(ele))
        return maxi


                
                
                
        
            
            
            
            
        