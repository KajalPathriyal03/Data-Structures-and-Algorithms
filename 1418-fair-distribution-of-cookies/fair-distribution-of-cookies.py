class Solution:
    def distributeCookies(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort(reverse=True)
        def solve(i, child):
            if i==n:
                ans=0
                for ch in child:
                    ans=max(ans, ch)
                return ans
            ans=float('inf')
            ln=len(child)
            for ch in range(ln):
                child[ch]+=nums[i]
                ans=min(ans, solve(i+1, child))
                child[ch]-=nums[i]
                if child[ch]==0:
                    break
            return ans 

        child=[0 for _ in range(k)]
        return solve(0, child)
        