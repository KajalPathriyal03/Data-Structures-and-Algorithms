class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        def max_length(ind):
            value = 0
            power = 0
            length = 0
            for i in range(n - 1, ind - 1, -1):
                bit = int(s[i])
                if bit == 1:
                    if power >= 32:
                        continue
                    value += (1 << power)
                    if value > k:
                        break
                length += 1
                power += 1
            return length

        zeroes = 0
        ans = 0
        for i in range(n):
            ans = max(ans, zeroes + max_length(i))
            if s[i] == "0":
                zeroes += 1
        return ans
