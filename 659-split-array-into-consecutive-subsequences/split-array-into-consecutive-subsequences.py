class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        mp=defaultdict(int)
        dp=defaultdict(int)
        for ele in nums:
            mp[ele]+=1

        for ele in nums:
            if mp[ele]<=0: continue 

            elif dp[ele]>0:
                mp[ele]-=1
                dp[ele]-=1
                dp[ele+1]+=1

            elif mp[ele]>0 and mp[ele+1]>0 and mp[ele+2]>0:
                mp[ele]-=1
                mp[ele+1]-=1
                mp[ele+2]-=1
                dp[ele+3]+=1

            else:
                return False 
        return True 

        