class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastOcc=defaultdict(int)
        for i in range(len(s)):
            lastOcc[s[i]]=i
        ans=""
        st=[]
        vis=set()

        for i in range(len(s)):
            if s[i] in vis:
                continue
            while st and s[st[-1]]>s[i] and lastOcc[s[st[-1]]]>i: 
                vis.discard(s[st.pop()])
            st.append(i)
            vis.add(s[i])
        
        while st:
            ans+=s[st.pop()]
        a=list(ans)
        a.reverse()
        return "".join(a)

        