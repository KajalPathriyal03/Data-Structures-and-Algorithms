class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp=defaultdict(int)
        for i in range(len(nums)):
            ele=nums[i]
            if ele==0:
                nums[i]=-1
        mp[0]=-1
        ans =0
        prefSum=0
        for i in range(len(nums)):
            prefSum+=nums[i]
            if prefSum in mp:
                sz=i-mp[prefSum]
                ans=max(ans, sz)
            else:
                mp[prefSum]=i

        return ans 

        