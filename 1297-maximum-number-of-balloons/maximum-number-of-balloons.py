class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s="balloon"
        mp=defaultdict(int)
        for ele in text:
            mp[ele]+=1
        mini=float('inf')
        for ele in s:
            if ele not in mp:
                return 0
            if ele=="l" or ele =="o":
                mini=min(mp[ele]//2, mini)
            mini=min(mp[ele], mini)
        
        return mini

            

        