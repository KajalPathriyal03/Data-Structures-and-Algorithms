class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        nums=sorted(envelopes, key=lambda x: (x[0], -x[1]))
        lis=[]
        lis.append(nums[0][1])
        for i in range(1, len(nums)):
            ind=bisect.bisect_left(lis, nums[i][1])
            if ind==len(lis):
                lis.append(nums[i][1])
            else:
                lis[ind]=nums[i][1]

        return len(lis)
        