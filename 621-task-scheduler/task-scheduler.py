class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        pq=[]
        for val in freq.values():
            heappush(pq, -val)

        time = 0

        while pq:

            temp = []

            cycle = n + 1

            i = 0

            while i < cycle and pq:

                count = heapq.heappop(pq)
                cnt=(-1)*count

                cnt -= 1

                if cnt > 0:
                    temp.append((-1)*cnt)

                time += 1
                i += 1

                
            for item in temp:
                heapq.heappush(pq, item)

            if pq:
                time += (cycle - i)

        return time