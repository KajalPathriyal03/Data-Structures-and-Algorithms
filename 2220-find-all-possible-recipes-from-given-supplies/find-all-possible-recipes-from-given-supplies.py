class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n=len(recipes)
        st=set(supplies)
        adj=defaultdict(list)
        ind={}
        ans=[]
        for ele in supplies:
            if ele not in ind:
                ind[ele]=0
        
        for i in range(n):
            m=len(ingredients[i])
            cnt=0
            for j in range(m):
                adj[ingredients[i][j]].append(recipes[i])
                cnt+=1
            ind[recipes[i]]=cnt
        # print(adj)
        # print(ind)
        queue=deque()
        for ele in ind:
            if ind[ele]==0:
                queue.append(ele)
        while queue:
            node=queue.popleft()
            for nei in adj[node]:
                ind[nei]-=1
                if ind[nei]==0:
                    queue.append(nei)
                    st.add(nei)

        for ele in recipes:
            if ind[ele]==0:
                ans.append(ele)
        return ans


        