class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        mp=set(nums)
        maxi=0
        for ele in mp:
            if ele-1 not in mp:
                cur=ele
                cnt=1
                while cur+1 in mp:
                    cur+=1
                    cnt+=1
                maxi=max(maxi, cnt)
        return maxi

