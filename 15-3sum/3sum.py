class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue 
            l, r=i+1, len(nums)-1
            target=-nums[i]
            ans=[]
            while l<r:
                sm= nums[l]+nums[r]
                if nums[l]+nums[r]==target:
                    a, b, c=nums[i], nums[l], nums[r]
                    ans.extend([a, b, c])
                    if ans:
                        res.append(ans)
                        ans=[]
                    while l<r and nums[l]==b:
                        l+=1
                    while l<r and nums[r]==c:
                        r-=1
                elif sm<target:
                    l+=1
                else:
                    r-=1
            
            
        return res



        