class Solution:
    def maximumSumOfHeights(self, nums: List[int]) -> int:
        n=len(nums)
        def find_sum(ind):
            prev=nums[ind]
            sm=0
            for i in range(ind-1, -1, -1):
                if nums[i]>prev:
                    sm+=prev
                else:
                    sm+=nums[i]
                    prev=nums[i]
            # print("left", sm)

            prev=nums[ind]
            for i in range(ind+1, n):
                if nums[i]>prev:
                    sm+=prev
                else:
                    sm+=nums[i]
                    prev=nums[i]
            # print("right", sm)
            return sm
        maxi=0
        for i in range(n):
            sm=nums[i]
            sm+=find_sum(i)
            # print(sm, maxi)
            maxi=max(maxi, sm)
        return maxi
