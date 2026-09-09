class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpen, maxOpen=0, 0
        for ch in s:
            if ch =="(":
                minOpen+=1
                maxOpen+=1
            elif ch==")":
                minOpen-=1
                maxOpen-=1
            else:
                minOpen-=1
                maxOpen+=1

            if maxOpen<0: #too many unmatched )
                return False 
            if minOpen<0: #open are negetive 
                minOpen=0
        return minOpen==0 
        