class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        ''' [3,3,3,1,2,1,1,2,3,3,4]
        l=3
        r=7
        ans=5
        st=[1 2
        if len(st)>2: discard(nums(l)): l+=1
        '''
        l, r, n=0, 0, len(nums)
        mp=defaultdict(int)
        ans=0
        while r<n:
            mp[nums[r]]+=1
            while len(mp)>2:
                mp[nums[l]]-=1
                if mp[nums[l]]==0:
                    del mp[nums[l]]
                l+=1
            ans =max(ans, r-l+1)
            # print(ans, mp)
            r+=1
        return ans 
            

