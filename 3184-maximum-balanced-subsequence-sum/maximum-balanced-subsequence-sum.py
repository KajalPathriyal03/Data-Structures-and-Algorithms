# from sortedcontainers import SortedList
class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        from sortedcontainers import SortedList
        mp=SortedList()
        res=float('-inf')
        for i in range(len(nums)):
            ele=nums[i]-i
            ind=mp.bisect([ele+0.1,-1])
            if ind-1>=0:
                tmp=max(0, mp[ind-1][1])+nums[i]
                ln=len(mp)
                while ind < len(mp) and tmp > mp[ind][1]:
                    del mp[ind]
                    # ind+=1
            else:
                tmp=nums[i]
            mp.add([ele, tmp])
            res=max(res, tmp)
        return res
        
            