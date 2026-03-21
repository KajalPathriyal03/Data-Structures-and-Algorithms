class Solution:
    def rec(self, l, r, arr):
        if l>r:
            return 0
        if l==r:
            return arr[l]
        take1=arr[l]+min(self.rec(l+2, r, arr), self.rec(l+1, r-1, arr))
        take2=arr[r]+min(self.rec(l, r-2, arr), self.rec(l+1, r-1, arr))
        
        return max(take1, take2)
    def predictTheWinner(self, nums: List[int]) -> bool:
        total=sum(nums)
        p1=self.rec(0, len(nums)-1, nums)
        p2=total-p1
        return p1>=p2

        