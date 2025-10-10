class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1 
        cgas=0
        j=0
        for i in range(len(gas)):
            cgas+=gas[i]-cost[i]
            if cgas<0:
                cgas=0
                j=i+1
        return j
        





        