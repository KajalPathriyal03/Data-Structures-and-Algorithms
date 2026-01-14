class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        mp=defaultdict(list)
        for i, ele in enumerate(s):
            mp[ele].append(i)
        cnt=0
        for ele in words:
            prev=-1
            for i in range(len(ele)):
                ind=bisect.bisect_right(mp[ele[i]], prev)
                if ind==len(mp[ele[i]]):
                    break
                prev=mp[ele[i]][ind]
                if i == len(ele)-1:
                    cnt+=1
                
        return cnt 
                


        