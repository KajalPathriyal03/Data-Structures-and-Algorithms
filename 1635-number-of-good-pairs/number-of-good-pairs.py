class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        mp=defaultdict(int)
        for ele in nums:
            mp[ele]+=1
        sm=0
        for key, val in mp.items():
            for i in range(1, val):
                sm+=i

        return sm


        