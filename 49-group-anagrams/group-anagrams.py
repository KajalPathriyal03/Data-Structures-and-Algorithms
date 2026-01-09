class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)
        for ele in strs:
            s="".join(sorted(ele))
            mp[s].append(ele)

        ans=[]
        for val in mp.values():
            ans.append(val)
        return ans
        