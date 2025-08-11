class Solution:
    def calculate(self, s: str) -> int:
        n=len(s)
        stack=[]
        num, res, sign=0, 0, 1
        for i in range(n):
            if s[i].isdigit(): 
                num=num*10+int(s[i])
            elif s[i]=="+":
                res=res+(num*sign)
                num=0
                sign=1
            elif s[i]=="-":
                res=res+(num*sign)
                num=0
                sign=-1
            elif s[i]=="(":
                stack.append(res)
                stack.append(sign)
                res=0
                num=0
                sign=1
            elif s[i]==")":
                res+=(num*sign)
                num=0
                st_sign=stack.pop()
                last_res=stack.pop()
                res*=st_sign
                res+=last_res
        res+=num*sign
        return res



        