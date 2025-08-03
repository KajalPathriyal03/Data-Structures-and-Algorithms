class Solution:
    def maximumLength(self, s: str) -> int:
        n=len(s)
        st=defaultdict(int)
        for i in range(n):
            ln=0
            ch=s[i]
            j=i
            while j<n and s[j]==ch:
                ln+=1
                st[(ch, ln)]+=1
                j+=1
                
        maxi=-1
        for (ch, ln), cnt in st.items():
            if cnt>=3:
                # print(ch, ln)
                maxi=max(maxi, ln)
        return maxi


                
                
                
        
            
            
            
            
        