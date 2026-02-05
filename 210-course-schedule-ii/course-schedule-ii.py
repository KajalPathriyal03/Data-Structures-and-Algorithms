class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        if n==0: return []
        adj=defaultdict(list)
        ind=[0 for _ in range(n)]
        for sec, first in prerequisites:
            adj[first].append(sec)
            ind[sec]+=1
        print(ind)
        queue=deque()
        ans=[]
        for i in range(n):
            if ind[i]==0:
                queue.append(i)
        
        while queue:
            node=queue.popleft()
            ans.append(node)
            for nei in adj[node]:
                ind[nei]-=1
                if ind[nei]==0:
                    queue.append(nei)
        if len(ans)!=n:
            return []
        
        return ans 
        