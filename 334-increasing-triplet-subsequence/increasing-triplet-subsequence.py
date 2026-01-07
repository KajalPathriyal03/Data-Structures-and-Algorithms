class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1=float('inf')
        min2=float('inf')
        for ele in nums:
            if ele<=min1:
                min1=ele
            elif ele<=min2:
                min2=ele
            else:
                return True 
        return False 



