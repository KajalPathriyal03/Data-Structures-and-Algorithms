class Solution:
    def sortItems(self, n: int, ln: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        group_id = ln
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1
        
        ln = group_id

        adj_items = defaultdict(list)
        indegree_items = [0] * n
        adj_groups = defaultdict(list)
        indegree_groups = [0] * ln

        for i in range(n):
            for prev in beforeItems[i]:
                adj_items[prev].append(i)
                indegree_items[i] += 1
                
                if group[prev] != group[i]:
                    adj_groups[group[prev]].append(group[i])
                    indegree_groups[group[i]] += 1

        def topo(adj, indegree):
            queue = deque([i for i, deg in enumerate(indegree) if deg == 0])
            res = []
            
            while queue:
                node = queue.popleft()
                res.append(node)
                
                for neighbor in adj[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            
            return res if len(res) == len(indegree) else []

        ans1 = topo(adj_items, indegree_items)
        ans2 = topo(adj_groups, indegree_groups)

        if not ans1 or not ans2:
            return []

        ans = defaultdict(list)
        for item in ans1:
            ans[group[item]].append(item)
            
        result = []
        for grp in ans2:
            result.extend(ans[grp])
            
        return result