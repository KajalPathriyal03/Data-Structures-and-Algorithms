class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''Actually basic idea of solution 2 is the same as solution 1, but difference between solution 1 and solution 2 is that we don't have to sort each character.

First of all, we create array with 26 length. 26 is number of alphablets.'''
        ans=defaultdict(list)
        for s in strs:
            cnt=[0]*26
            for c in s:
                cnt[ord(c)-ord('a')]+=1
            ans[tuple(cnt)].append(s)
        return list(ans.values())

        