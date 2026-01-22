class Solution:
    def isPair(self, last, cur):
        if last=="(" and cur==")" or last=="[" and cur=="]" or last=="{" and cur=="}":
            return True 
        return False 
    def isValid(self, s: str) -> bool:
        stack=[]
        for ele in s:
            if stack:
                if self.isPair(stack[-1], ele):
                    stack.pop()
                    continue 
            stack.append(ele)
            
        return not stack


                
                    







































        stack=[]
        for ele in s:
            
            if ele == ")"  or ele == "]" or ele =="}" :
                if stack:
                    if (ele == ")" and stack[-1]=="(") or (ele == "]" and stack[-1]=="[") or (ele =="}" and stack[-1]=="{"):
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(ele)
        if not stack:
            return True 
        return False
        