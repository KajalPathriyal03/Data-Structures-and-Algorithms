class Solution:
    def nextGreaterElement(self, n: int) -> int:
        st=list(str(n))
        ln=len(st)
        pivot=-1

        for i in range(ln-2, -1, -1):
            if st[i]<st[i+1]:
                pivot=i
                break 

        if pivot==-1: return -1

        print(pivot)
        j = pivot+1

        while j<ln and st[j] > st[pivot]:
            j += 1

        st[pivot], st[j-1]=st[j-1], st[pivot]

        st[pivot+1:]=sorted(st[pivot+1:])

        ret=int("".join(st))

        return ret if ret < 1<<31 else -1

        