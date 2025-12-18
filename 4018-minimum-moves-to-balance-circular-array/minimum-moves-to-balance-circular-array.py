class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if sum(nums)<0: return -1 
        idx=-1
        for i in range(len(nums)):
            if nums[i]<0:
                idx=i
                break

        if idx==-1: return 0
        moves=0
        dist=1
        while nums[idx]<0:
            prev=(idx+dist)%len(nums)
            nextt=(idx-dist+len(nums))%len(nums)
            total=nums[prev]+nums[nextt]
            units=min(abs(nums[idx]), total)
            nums[idx]+=units
            moves+=dist*units
            dist+=1
            
        return moves




        