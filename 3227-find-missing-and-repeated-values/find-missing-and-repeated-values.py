class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        mp=defaultdict(int)
        n, m=len(grid), len(grid[0])
        arr=[]
        for i in range(n):
            for j in range(m):
                arr.append(grid[i][j])
        n=len(arr)
        print(arr)
        xor=0
        for i in range(n):
            xor^=arr[i]
            xor^=(i+1)

        #bitnumber is where the bits are differentiating
        # 001 101=100
        bitno=xor & ~(xor-1)
        # print(bitno)
        ones, zeroes=0, 0
        for ele in arr:
            #part of  one club 
            if ele & bitno:
                ones^=ele
            else:
                zeroes^=ele
        for ele in range(1, n+1):
            if (ele & bitno):
                ones^=ele
            else:
                zeroes^=ele
        cnt=0
        print(ones, zeroes, xor, bitno)
        for ele in arr:
            if ones==ele:
                cnt+=1
        if cnt!=0:
            return [ones, zeroes]
        return [zeroes, ones]





