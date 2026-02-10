class Solution:
    def canEat(self, bananas, piles, h):
        cnt=0
        for ele in piles:
            cnt+=ceil(ele/bananas)
        
        if cnt<=h:
            return True 
        return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r=1, max(piles)
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if self.canEat(mid, piles, h):
                ans=mid
                r=mid-1
            else:
                l=mid+1

        return ans 
        