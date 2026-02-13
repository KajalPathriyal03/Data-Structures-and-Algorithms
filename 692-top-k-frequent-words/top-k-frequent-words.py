class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp=Counter(words)
        pq=[]
        ans=[]
        for key, val in mp.items():
            heappush(pq, (-val, key))
        
        while pq:

            if k==0:
                break
            _ , key= heappop(pq)
            ans.append(key)
            k-=1
        return ans 

        