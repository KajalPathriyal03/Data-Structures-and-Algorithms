class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        n, m=len(a), len(b)
        l, r=0,0
        median=(n+m)//2
        cnt=0
        first = sec=-1
        while l<n and r<m:
            if a[l]<b[r]:
                if cnt==median-1:first=a[l]
                if cnt==median: sec=a[l]
                l+=1
            else:
                if cnt==median-1: first=b[r]
                if cnt==median: sec=b[r]
                r+=1
            cnt+=1
        
        while l<n :
            if cnt==median-1:first=a[l]
            if cnt==median: sec=a[l]
            l+=1
            cnt+=1

        while r<m :
            if cnt==median-1: first=b[r]
            if cnt==median: sec=b[r]
            r+=1
            cnt+=1
        
        
        if (n+m)%2==1:
            return float(sec)
        return (first+sec)/2.0

        

        


