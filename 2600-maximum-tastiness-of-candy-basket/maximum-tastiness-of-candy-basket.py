class Solution:
    def check(self, mid):
        cnt=1
        lt=self.nums[0]
        for i in range(len(self.nums)):
            if self.nums[i]-lt>=mid:
                cnt+=1
                lt=self.nums[i]
            if cnt>=self.k:
                return True 
        return False

    def maximumTastiness(self, price: List[int], k: int) -> int:
        self.nums=price
        self.k=k
        self.nums.sort()
        ans =0
        l, r=0, max(self.nums)-min(self.nums)
        while l<=r:
            mid=(l+r)//2
            if self.check(mid):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans 

        
        


    
