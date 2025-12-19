class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lis=[1 for _ in range(len(nums))]
        cnt=[1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i]>nums[j]:
                    if lis[i]==lis[j]+1:
                        cnt[i]+=cnt[j]
                    elif lis[j]+1>lis[i]:
                        lis[i]=1+lis[j]
                        cnt[i]=cnt[j]
        # print(lis, cnt)
        maxi=max(lis)
        ans=0
        for i in range(len(nums)):
            if lis[i]==maxi:
                ans+=cnt[i]
        return ans