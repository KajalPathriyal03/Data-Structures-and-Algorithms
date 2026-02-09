class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0 
        maxi=0
        st=set(nums)
        for ele in st:
            if ele-1 not in st:
                cnt=1
                cur=ele
                while cur+1 in st:
                    cnt+=1
                    cur+=1
                maxi=max(maxi, cnt)

        return maxi
        