import heapq
from sortedcontainers import SortedList
class Solution:
    def maxTotal(self, value: list[int], limit: list[int]) -> int:
        n = len(value)
        adj=defaultdict(list)

        for i in range(n):
            adj[limit[i]].append(value[i])
        active=0
        total=0
        
        for ele in range(1, n+1):
            if ele not in adj: continue
            adj[ele].sort(reverse=True)
            # print(adj[ele][-1], adj[ele], ele)
            ln=len(adj[ele])
            for i in range(min(ele, ln)):
                total+=adj[ele][i]
        return total



