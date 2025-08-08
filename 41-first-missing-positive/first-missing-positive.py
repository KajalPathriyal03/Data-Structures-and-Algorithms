from sortedcontainers import  SortedSet
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        # modifying actual array but TC: O(n), SC: O(1)

        for i, ele in enumerate(nums):
            if ele<=0:
                nums[i]=n+1
        
        for i in range(n):
            if abs(nums[i])<=n and abs(nums[i])-1>=0 and abs(nums[i])-1<n:
                ind=abs(nums[i])-1
                if nums[ind]<0: continue
                nums[ind]=nums[ind]*(-1)
        # print(nums)
        for i, ele in enumerate(nums):
            if ele>0:
                return i+1
        
        return n+1

        