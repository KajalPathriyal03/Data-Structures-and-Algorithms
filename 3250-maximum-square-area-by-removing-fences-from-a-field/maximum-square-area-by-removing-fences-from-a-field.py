class Solution:
    def maximizeSquareArea(self, m: int, n: int, h: List[int], v: List[int]) -> int:
        h.append(1)
        h.append(m)
        v.append(1)
        v.append(n)
        h.sort()
        v.sort()
        # print(h, v)
        st1, st2=set(), set()
        hn,vn=len(h), len(v)
        for i in range(hn):
            for j in range(i+1, hn):
                st1.add(h[j]-h[i])
        for i in range(vn):
            for j in range(i+1, vn):
                # print(v[j]-v[i])
                st2.add(v[j]-v[i])
        ans=0
        # print(st2)
        for ele in st1:
            if ele in st2:
                # print(ele)
                area=ele*ele
                ans=max(ans, area)
        if ans == 0: return -1
        mod=10**9+7
        ans=ans%mod
        return ans 

        