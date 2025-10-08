class Solution:
    # [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    # l, r=0, 0
    # cntZeroes=0
    # cntOnes=0

    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l, r=0, 0
        cntZeroes=0
        cntOnes=0
        maxi=float('-inf')
        while r<n:
            if nums[r]==1:
                cntOnes+=1
            elif nums[r]==0:
                cntZeroes+=1
            if cntZeroes<=k:
                maxi=max(maxi, cntOnes+cntZeroes)
            else:
                # maxi=max(maxi, cntOnes+k)
                if nums[l]==1:
                    cntOnes-=1
                elif nums[l]==0:
                    cntZeroes-=1
                l+=1
            r+=1
        if maxi==float('-inf'):
            return 0
        return maxi



            