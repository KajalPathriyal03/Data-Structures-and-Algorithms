class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp=defaultdict(int)
        for ele in nums:
            mp[ele]+=1
        pq=[]
        for key, val in mp.items():
            heappush(pq, (val, key))
            if len(pq)>k:
                heappop(pq)
                
        ans =[]
        # print(pq)
        while pq:
            _ , key=heappop(pq)
            ans.append(key)
        return ans 

            

        