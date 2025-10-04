class Solution:
    def __init__(self):
        self.ans=[]
    def isValid(self, curr):
        cnt=0
        for ele in curr:
            if ele=="(":
                cnt+=1
            else: 
                cnt-=1
            if cnt<0: return False 
        
        return cnt==0
    def solve(self, curr, n):
        if len(curr)==2*n:
            if self.isValid(curr)==True:
                st="".join(curr)
                print("curr", curr)
                self.ans.append(st)
            return 
        
        curr.append("(")
        self.solve(curr, n)
        curr.pop()

        curr.append(")")
        self.solve(curr, n)
        curr.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        curr=[]
        self.solve(curr, n)
        return self.ans
        