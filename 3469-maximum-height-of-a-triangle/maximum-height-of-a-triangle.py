class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        odd, even=0, 0
        ht=0
        for i in range(1, 101):
            if i%2==0:
                odd+=i
            else:
                even+=i
            if max(odd, even)<=max(red, blue) and min(odd, even)<=min(red, blue):
                ht=i
            else: break
        return ht

        