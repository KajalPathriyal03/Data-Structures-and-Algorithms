import bisect 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr=[]
        ans=1
        arr.append(nums[0])
        for i in range(1, len(nums)):
            if arr[-1]<nums[i]:
                arr.append(nums[i])
            else:
                ind=bisect.bisect_left(arr, nums[i])
                arr[ind]=nums[i]
            ans=len(arr)
        return ans

        