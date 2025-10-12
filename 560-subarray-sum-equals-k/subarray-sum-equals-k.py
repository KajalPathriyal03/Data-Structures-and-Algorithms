class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        preSum=0
        mp={0:1}
        for ele in nums:
            preSum+=ele
            if preSum-k in mp:
                ans+=mp[preSum-k]
            if preSum in mp:
                mp[preSum]+=1
            else:
                mp[preSum]=1
        return ans 


        