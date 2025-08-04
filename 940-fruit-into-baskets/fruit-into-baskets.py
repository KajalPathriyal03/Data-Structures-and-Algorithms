class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        n=len(nums)
        l, r=0, 0
        mp={}
        maxi=0
        if n==1: return 1
        while r<n:
            ele=nums[r]
            if len(mp)==3:
                mp[nums[l]]-=1
                if mp[nums[l]]==0:
                    del mp[nums[l]]
                l+=1
                continue
            else:
                if ele not in mp:
                    mp[ele]=1
                else:
                    mp[ele]+=1
                r+=1
                cs=0
                if len(mp)<=2:
                    for ele, cnt in mp.items():
                        cs+=cnt
                    maxi=max(maxi, cs)

        return maxi
        


        