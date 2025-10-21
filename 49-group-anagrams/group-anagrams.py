class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)
        ans=[]
        for i in range(len(strs)):
            s=sorted(strs[i])
            new="".join(s)
            print(s, new)
            if new not in mp:
                mp[new]=[]
            mp[new].append(i)
        for key, vals in mp.items():
            # print(vals)
            cur=[]
            for i in range(len(vals)):
                cur.append(strs[vals[i]])
            # print(cur)
            ans.append(cur.copy())
        return ans 
                




        