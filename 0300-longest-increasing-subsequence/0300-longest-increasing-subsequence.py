import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr=[]
        for ele in nums:
            ind = bisect.bisect_left(arr, ele)
            if ind == len(arr):
                arr.append(ele)
            else:
                arr[ind]=ele 
        return len(arr) 
        