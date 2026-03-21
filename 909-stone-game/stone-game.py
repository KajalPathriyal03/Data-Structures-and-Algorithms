class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        left=sum(piles[:n-2])
        right=sum(piles[1:])
        return True 
        