class UnionFind:
    def __init__(self, n):
        self.par=list(range(n))
        self.rank=[0 for _ in range(n)]

    def findUpar(self, node):
        if self.par[node]==node:
            return node
        self.par[node]=self.findUpar(self.par[node])
        return self.par[node]

    def union(self, u, v):
        root_u=self.findUpar(u)
        root_v=self.findUpar(v)
        if root_u==root_v:
            return 
        if self.rank[root_u]<self.rank[root_v]:
            self.par[root_u]=root_v
        elif self.rank[root_v]<self.rank[root_u]:
            self.par[root_v]=root_u
        else:
            self.par[root_v]=root_u
            self.rank[root_u]+=1
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dsu=UnionFind(n)
        stack=[]
        for i in range(n):
            prev=i
            if stack:
                prev=stack[-1]
            while stack and nums[i]<nums[stack[-1]]:
                dsu.union(stack.pop(), i)
            if nums[i]>nums[prev]:
                stack.append(i)
            else:
                stack.append(prev)
        stack=[]
        for i in range(n-1, -1, -1):
            prev=i
            if stack:
                prev=stack[-1]
            while stack and nums[i]>nums[stack[-1]]:
                dsu.union(stack.pop(), i)
            if nums[i]<nums[prev]:
                stack.append(i)
            else:
                stack.append(prev)
        mp = {} 
        for i in range(n):
            root = dsu.findUpar(i) 
            
            current_max = mp.get(root, float('-inf'))
            
            mp[root] = max(current_max, nums[i])
        print(mp)
        ans = [0] * n
        for i in range(n):
            root = dsu.findUpar(i)
            ans[i] = mp[root]

        return ans