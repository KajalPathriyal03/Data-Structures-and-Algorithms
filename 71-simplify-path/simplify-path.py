class Solution:
    def simplifyPath(self, path: str) -> str:
        s=path.split("/")
        print(s)
        st=[]
        for ele in s:
            if ele=="" or ele==".":
                continue 
            if ele=="..":
                if st:
                    st.pop()
            else:
                st.append(ele)
        return "/" +"/".join(st)
        