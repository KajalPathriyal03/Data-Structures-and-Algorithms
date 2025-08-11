from sortedcontainers import SortedList
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n=len(arr)
        greater_ele=SortedList([(arr[n-1], n-1)])
        smaller_ele=SortedList([(-1*arr[n-1], n-1)])
        even, odd=[False for _ in range(n)], [False for _ in range(n)]
        odd[n-1]=True
        even[n-1]=True

        cnt=1
        for i in range(n-2, -1, -1):
            ele=arr[i]
            ng_ind=bisect_left(greater_ele, (ele, i))
            ns_ind=bisect_left(smaller_ele, (-1*ele, i))

            ln=len(greater_ele)
            if ng_ind!=ln:
                x, ind=greater_ele[ng_ind]
                odd[i]=even[ind]
            if ns_ind!=ln:
                x, ind=smaller_ele[ns_ind]
                even[i]=odd[ind]
            
            greater_ele.add((ele, i))
            smaller_ele.add((-1*ele, i))

            if odd[i]:
                cnt+=1
        return cnt
        