from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        queue=deque()
        ans=[]
        for r in range(n):
            while queue and nums[queue[-1]]<=nums[r]:
                queue.pop()
            
            queue.append(r)
            if queue[0]==r-k:
                queue.popleft()
            if r>=k-1:
                ans.append(nums[queue[0]])
        return ans 

            
            
            