# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, nums: 'MountainArray') -> int:
        n=nums.length()
        l, r=1, n-2
        m=0
        while l<=r:
            mid=(l+r)//2
            val=nums.get(mid)
            left, right, middle=nums.get(mid-1), nums.get(mid+1), val
            if left<middle<right:
                l=mid+1
            elif left>middle>right:
                r=mid-1
            else:
                m=mid
                break
        peak=m
        l, r=0,peak
        while l<=r:
            mid=(l+r)//2
            val=nums.get(mid)
            if val==target:
                return mid
            elif val<target:
                l=mid+1
            else:
                r=mid-1

        l, r=peak, n-1
        while l<=r:
            mid=(l+r)//2
            val=nums.get(mid)
            if val==target:
                return mid
            elif val>target:
                l=mid+1
            else:
                r=mid-1
                
        return -1
        



        
        