class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost): return -1 

        ans=0
        cs=0
        for i in range(len(gas)):
            cs+=gas[i]-cost[i]
            if cs<0:
                cs=0
                ans=i+1
            
        return ans 