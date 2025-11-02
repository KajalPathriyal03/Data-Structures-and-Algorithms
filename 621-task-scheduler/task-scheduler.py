class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count frequency of each task
        freq = Counter(tasks)

        # Step 2: Create a max heap by using negative counts
        pq=[]
        for val in freq.values():
            heappush(pq, -val)

        # Total time required
        time = 0

        # Step 3: Process tasks in cycles of size (n + 1)
        while pq:

            # Temporary list to store remaining tasks
            temp = []

            # Set cycle size as cooldown + 1
            cycle = n + 1

            # Track number of tasks run in this cycle
            i = 0

            # Run up to (n+1) tasks or until heap is empty
            while i < cycle and pq:

                # Get the task with highest remaining count
                count = heapq.heappop(pq)
                cnt=(-1)*count

                # Decrease count since task used once
                cnt -= 1  # since it's negative

                # If still tasks remaining, push to temp
                if cnt > 0:
                    temp.append((-1)*cnt)

                # Count 1 unit of time
                time += 1
                i += 1
                

            # Step 4: Push remaining tasks back into the heap
            for item in temp:
                heapq.heappush(pq, item)

            # Step 5: Add idle time if heap still has tasks
            if pq:
                time += (cycle - i)

        # Return total time taken
        return time