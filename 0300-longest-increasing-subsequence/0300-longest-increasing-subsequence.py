import bisect

class Solution:
    def lower_bound(self, nums, ele):
        l, r=0, len(nums)-1
        ans = -1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>=ele:
                ans = mid 
                r=mid-1
            else:
                l=mid+1
        if ans==-1:
            return len(nums)
        return ans 

    def lengthOfLIS(self, nums: List[int]) -> int:
        arr=[]
        for ele in nums:
            ind = self.lower_bound(arr, ele)
            # print(ele, ind)
            if ind == len(arr):
                arr.append(ele)
            else:
                arr[ind]=ele 
        return len(arr) 
        