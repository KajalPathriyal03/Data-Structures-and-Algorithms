class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n=len(nums)
        pq=[]
        maxi=float('-inf')
        for i in range(n):
            heappush(pq, (nums[i][0], i,0))
            maxi=max(maxi, nums[i][0])
        
        res=[float('-inf'), float('inf')]
        while pq:
            ele, lst_ind, ind=heappop(pq)
            if maxi-ele<res[1]-res[0]:
                res[0]=ele
                res[1]=maxi
            if ind+1<len(nums[lst_ind]):
                nxt_ele=nums[lst_ind][ind+1]
                heappush(pq, (nxt_ele, lst_ind, ind+1))
                maxi=max(maxi, nxt_ele)
            else:
                break
        print(res)
        return res
