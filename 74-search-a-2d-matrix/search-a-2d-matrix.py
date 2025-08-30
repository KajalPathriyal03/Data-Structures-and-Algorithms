class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m=len(matrix), len(matrix[0])
        low, high=0, n-1
        while  low<=high:
            mid=(low+high)//2
            first, last=matrix[mid][0], matrix[mid][m-1]
            if target>=first and target<=last:
                l, r=0, m-1
                while l<=r:
                    m=(l+r)//2
                    if matrix[mid][m]==target:
                        return True
                    elif matrix[mid][m]>target:
                        r=m-1
                    else:
                        l=m+1
                return False

            elif target<first:
                high=mid-1
            elif target>last:
                low=mid+1
            else:
                return False
        return False
                


        