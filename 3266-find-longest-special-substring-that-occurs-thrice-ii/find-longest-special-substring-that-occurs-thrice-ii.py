from collections import defaultdict, Counter

class Solution:
    def maximumLength(self, s: str) -> int:

        n = len(s)
        freq = defaultdict(Counter)
        
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            ch = s[i]
            length = j - i
            for l in range(1, length + 1):
                freq[ch][l] += (length - l + 1)
            i = j

        max_len = -1
        for ch in freq:
            for l in sorted(freq[ch].keys(), reverse=True):
                if freq[ch][l] >= 3:
                    max_len = max(max_len, l)
                    break

        return max_len
