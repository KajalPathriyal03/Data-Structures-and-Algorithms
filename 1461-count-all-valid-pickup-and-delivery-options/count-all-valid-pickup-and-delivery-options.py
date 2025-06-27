class Solution:
    def countOrders(self, n: int) -> int:
        # 2*n slots
        # count valid ways to array a pair p1, d1
        # choices=x*(x-1)
        # valid_choices=x*(x-1)//2

        slots=2*n
        op=1
        while slots>0:
            valid_choices=(slots*(slots-1))//2
            op*=valid_choices
            slots-=2
        return op%(10**9+7)
        