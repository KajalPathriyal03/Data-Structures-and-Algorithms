class Solution:
    def reverse(self, num):
        reverse_num=0
        while num:
            digit=num%10
            reverse_num=reverse_num*10+digit
            num//=10
        return reverse_num
    def countNicePairs(self, arr: List[int]) -> int:
        mod=10**9+7
        ans=0
        mp=defaultdict(int)
        for ele in arr:
            mp[ele-self.reverse(ele)]+=1
        for val in mp.values():
            k=(val%mod*(val%mod-1))//2
            ans+=k%mod
        return ans%mod
            