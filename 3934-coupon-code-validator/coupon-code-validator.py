class Solution:
    def validateCoupons(self, code: List[str], business: List[str], isActive: List[bool]) -> List[str]:
        busi={"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3}
        ans=[]
        for c, b, a in zip(code, business, isActive):
            if not a or not c or b not in busi: continue
            for ch in c:
                if not (ch.isalnum() or ch=="_"):
                    break
            else:
                ans.append((busi[b], c))
        ans.sort(key=lambda x: (x[0], x[1]))
        return [c for _, c in ans]
            