class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            if i>0 and nums[i-1] ==nums[i]: continue
            for j in range(i+1, len(nums)):
                
                if j>i+1 and nums[j-1]==nums[j]: continue 
                l, r= j+1, len(nums)-1
                while l<r:
                    a, b, c, d=nums[i], nums[j], nums[l], nums[r]
                    sm=a+b+c+d
                    if sm==target:
                        ans.append((a, b, c, d))
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1

                    elif sm<target:
                        l+=1
                    else:
                        r-=1
        return ans 

        