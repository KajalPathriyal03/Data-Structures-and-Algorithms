class SnapshotArray:

    def __init__(self, n: int):
        self.mp=defaultdict(list)
        self.id=0
        for i in range(n):
            self.mp[i].append((0, 0))
    
    def set(self, index: int, val: int) -> None:
        self.mp[index].append((self.id, val))

    def snap(self) -> int:
        self.id+=1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.mp[index]
        l, r = 0, len(arr) - 1
        ans = 0

        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] <= snap_id:
                ans = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return ans