import collections
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
       
        if source == target:
            return 0

        adj_list = collections.defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                adj_list[stop].append(i)

        q = collections.deque()
        visited_routes = set()

        for route_index in adj_list[source]:
            q.append(route_index)
            visited_routes.add(route_index)
        
        bus_count = 1
        while q:
            level_size = len(q)
            for _ in range(level_size):
                current_route_index = q.popleft()

                for stop in routes[current_route_index]:
                    if stop == target:
                        return bus_count

                    for next_route_index in adj_list[stop]:
  
                        if next_route_index not in visited_routes:
                            visited_routes.add(next_route_index)
                            q.append(next_route_index)
            

            bus_count += 1

        return -1