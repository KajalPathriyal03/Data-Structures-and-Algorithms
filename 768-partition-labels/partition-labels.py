class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp=defaultdict(int)
        for i in range(len(s)):
            mp[s[i]]=i      #last occurence
        ans=[]
        l, r=0, 0
        for i in range(len(s)):
            r=max(r, mp[s[i]])
            if r==i:
                ans.append(r-l+1)
                l=i+1
        return ans



        