class Solution:
    def findIndices(self, nums: List[int], idif: int, vdif: int) -> List[int]:
        r=idif
        n=len(nums)
        mini, maxi=0, 0
        while r<n:
            l=r-idif
            if nums[l]<nums[mini]:
                mini=l
            if nums[l]>nums[maxi]:
                maxi=l
            if abs(nums[r]-nums[mini])>=vdif:
                return [mini, r]
            if abs(nums[r]-nums[maxi])>=vdif:
                return [maxi, r]
        

            r+=1
 
        return [-1, -1]