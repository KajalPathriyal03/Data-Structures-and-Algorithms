class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        adj = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        vis=set()
        queue=deque()
        start=""
        for i in range(2):
            for j in range(3):
                start+=str(board[i][j])
        print(start)

        def findInd(st):
            for i, ele in enumerate(st):
                if ele=="0":
                    return i
            return -1
        queue.append(start)
        target="123450"
        level=0
        while queue:
            n=len(queue)
            while n:
                cur=queue.popleft()

                if cur==target:
                    return level

                ind=findInd(cur)
                for nei in adj[ind]:
                    cur_lst=list(cur)
                    cur_lst[ind], cur_lst[nei]=cur_lst[nei], cur_lst[ind]
                    new_cur="".join(cur_lst)
                    if new_cur not in vis:
                        queue.append(new_cur)
                        vis.add(new_cur)
                n-=1
            level+=1
        return -1




        