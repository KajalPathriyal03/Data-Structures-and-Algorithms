class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue=deque()
        for i in range(1, n+1):
            queue.append(i)
        print(queue)

        while len(queue)>1:
            print(queue)
            for i in range(1, k):
                queue.append(queue[0])
                queue.popleft()
            queue.popleft()
        return queue[0]
        