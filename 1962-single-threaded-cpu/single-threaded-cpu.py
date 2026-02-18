class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks=sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        pq=[]
        ans=[]
        time=tasks[0][0]
        i=0
        while len(ans)<len(tasks):
            while i<len(tasks) and tasks[i][0]<=time:
                heappush(pq, (tasks[i][1], tasks[i][2]))
                i+=1
            
            if pq:
                mini, ind=heappop(pq)
                time+=mini
                ans.append(ind)
            
            elif i<len(tasks):
                time=tasks[i][0]
        return ans 



        