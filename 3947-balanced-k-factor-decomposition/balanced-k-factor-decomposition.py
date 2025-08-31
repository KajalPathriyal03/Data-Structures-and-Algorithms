class Solution:
    def backtrack(self, remaining: int, slots: int, path: List[int], start: int):
        if slots == 1:
            if remaining >= start:
                final_path = path + [remaining]
                diff = max(final_path) - min(final_path)
                if diff < self.min_diff:
                    self.min_diff = diff
                    self.best = final_path
            return

        for i in range(start, int(math.sqrt(remaining)) + 1):
            if remaining % i == 0:
                path.append(i)
                self.backtrack(remaining // i, slots - 1, path, i)
                path.pop()

    def minDifference(self, n: int, k: int) -> List[int]:
        self.best = []
        self.min_diff = float('inf')
        self.backtrack(n, k, [], 1)
        return self.best