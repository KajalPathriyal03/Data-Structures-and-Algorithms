from sortedcontainers import  SortedSet
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        mp=set()
        for ele in nums:
            mp.add(ele)
        for i in range(1, n+2):
            if i not in mp:
                return i
                break
        return -1
        




        