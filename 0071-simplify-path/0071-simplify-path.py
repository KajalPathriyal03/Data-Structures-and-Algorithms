class Solution:
    def simplifyPath(self, path: str) -> str:
        n=len(path)
        s=""
        st=[]
        for i in range(n+1):
            if i==n or path[i]=="/":
                if s=="" or s==".":
                    s=""
                    continue 
                elif s=="..":
                    if st: st.pop()
                else:
                    st.append(s)
                s=""
            else:
                s+=path[i]
    
        return "/"+"/".join(st)




        