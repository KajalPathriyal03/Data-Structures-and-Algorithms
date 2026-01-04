class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res=majority=0
        for ele in nums:
            if majority==0:
                res=ele

            if ele==res:
                majority+=1
            else:
                majority-=1
        return res

        