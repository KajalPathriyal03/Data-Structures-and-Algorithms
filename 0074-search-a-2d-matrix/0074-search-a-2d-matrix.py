class Solution:
    def can(self, nums, target):
        cols=len(nums)
        l, r=0, cols-1
        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                return True
            elif target<nums[mid]:
                r=mid-1
            else:
                l=mid+1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols=len(matrix), len(matrix[0])

        l, r=0, rows-1
        while l<=r:
            mid=(l+r)//2

            if target<=matrix[mid][cols-1]:
                if self.can(matrix[mid], target): 
                    return True
                r=mid-1
            else:
                l=mid+1
        
        return False

