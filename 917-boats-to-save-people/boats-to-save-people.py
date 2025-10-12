class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        ''' 
        1 2 2 2 2 2 3 3  l=3
        '''
        # boats
        nums.sort()
        l, r=0, len(nums)-1
        ans=0
        while l<=r:
            if nums[l]+nums[r]<=limit:
                l+=1
            r-=1
           
            ans+=1
        return ans 


        