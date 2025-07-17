class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        n = len(points)
        xy_sum = [x + y for x, y in points]
        xy_diff = [x - y for x, y in points]

        max_sum = max(xy_sum)
        min_sum = min(xy_sum)
        max_diff = max(xy_diff)
        min_diff = min(xy_diff)

        # Precompute frequency counts
        from collections import defaultdict
        sum_count = defaultdict(int)
        diff_count = defaultdict(int)
        for s in xy_sum:
            sum_count[s] += 1
        for d in xy_diff:
            diff_count[d] += 1

        ans = float('inf')

        for i in range(n):
            s = xy_sum[i]
            d = xy_diff[i]

            # Temporarily remove point
            sum_count[s] -= 1
            diff_count[d] -= 1

            # Recompute max/min only if necessary
            new_max_sum = max_sum if sum_count[max_sum] > 0 else max(k for k in sum_count if sum_count[k] > 0)
            new_min_sum = min_sum if sum_count[min_sum] > 0 else min(k for k in sum_count if sum_count[k] > 0)
            new_max_diff = max_diff if diff_count[max_diff] > 0 else max(k for k in diff_count if diff_count[k] > 0)
            new_min_diff = min_diff if diff_count[min_diff] > 0 else min(k for k in diff_count if diff_count[k] > 0)

            res = max(new_max_sum - new_min_sum, new_max_diff - new_min_diff)
            ans = min(ans, res)

            # Restore point
            sum_count[s] += 1
            diff_count[d] += 1

        return ans
            
            
            
                
        