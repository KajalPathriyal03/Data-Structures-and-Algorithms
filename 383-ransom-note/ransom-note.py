class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp=defaultdict(int)
        dp=defaultdict(int)
        for ele in ransomNote:
            dp[ele]+=1
        for ele in magazine:
            mp[ele]+=1
        
        for key, val in dp.items():

            if key in mp:
                mp[key]-=val
                if mp[key]<0:
                    return False 
            else:
                return False 

        return True 
        