# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from sortedcontainers import SortedList
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp=defaultdict(lambda: defaultdict(SortedList))
        queue=deque()
        queue.append((root, 0, 0))
        while queue:
            node, vertical, level=queue.popleft()
            mp[vertical][level].add(node.val)
            if node.left:
                queue.append((node.left, vertical-1, level+1))
            if node.right:
                queue.append((node.right, vertical+1, level+1))
        ans=defaultdict(list)
        mini, maxi=float('inf'), float('-inf')
        for key, val in mp.items():
            mini=min(mini, key)
            maxi=max(maxi, key)
            col=[]
            for v in val.values():
                for ele in v:
                    col.append(ele)
            ans[key].append(col)
        res=[]
        for i in range(mini, maxi+1):
            if i not in ans:
                continue
            else:
                for ele in ans[i]:
                    res.append(ele)
        # print(res)
        return res
