class Solution:
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        if a == e or b == f:
            if a == e and a == c and (d - b) * (d - f) < 0:
                return 2
            if b == f and b == d and (c - a) * (c - e) < 0:
                return 2
            return 1
        if (c - e) ==  (d - f):
            if (c - a) == (d - b) and (b - f) * (b - d) < 0:
                return 2
            return 1
        if c-e ==f-d:
            if a-e == f-b and (a-c)*(a-e)<0: return 2
            return 1
        return 2