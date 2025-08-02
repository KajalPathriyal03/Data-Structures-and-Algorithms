from sortedcontainers import SortedList
class Solution:
    def minCost(self, nums1: List[int], nums2: List[int]) -> int:
        cnt=Counter()
        mini=float('inf')
        for ele in nums1:
            cnt[ele]+=1
            mini=min(mini, ele)
        for ele in nums2:
            cnt[ele]-=1
            mini=min(mini, ele)
        
        merge=[]
        for ele, freq in cnt.items():
            if freq%2==1: return -1
            merge.extend([ele]*(abs(freq)//2))
        
        if not merge: return 0
        merge.sort()
        print(merge)
        ans=0
        for ele in range(len(merge)//2):
            print(merge[ele], 2*mini)
            ans+=min(merge[ele], 2*mini)
        return  ans



        

        