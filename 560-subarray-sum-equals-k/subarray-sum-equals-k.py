class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref_sum, ans=0, 0
        mp={}
        mp[0]=1
        for ele in nums:
            pref_sum+=ele
            if pref_sum-k in mp:
                ans+=mp[pref_sum-k]
            if pref_sum in mp:
                mp[pref_sum]+=1
            else:
                mp[pref_sum]=1
        return ans