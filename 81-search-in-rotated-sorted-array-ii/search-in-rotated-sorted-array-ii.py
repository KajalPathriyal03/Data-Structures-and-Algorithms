class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        l, r=0, n-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target: return True 
            if nums[mid]==nums[l] and nums[mid]==nums[r]:
                l+=1
                r-=1
                continue
            #if left  half is sorted--- iether of 1 half has to be sorted 
            if nums[l]<=nums[mid]:
                if nums[l]<=target and nums[mid]>=target:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[r]>=target and target>=nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
        return False


        