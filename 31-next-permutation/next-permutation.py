class Solution:
    def reverse(self, nums):
        ans=[]
        for i in range(len(nums)-1, -1, -1):
            ans.append(nums[i])
        return ans 
    def nextPermutation(self, arr):
        n=len(arr)
        #find a dip
        dip=-1
        for i in range(n-2, -1, -1):
            if arr[i]<arr[i+1]:
                dip=i
                break
        if dip==-1:
            ans=self.reverse(arr)
            # print(ans)
            i=0
            for ele in ans:
                # print(ele)
                arr[i]=ele
                i+=1
        else:
            mini=float('inf')
            for i in range(n-1, dip, -1):
                if arr[dip]<arr[i]:
                    arr[dip], arr[i]=arr[i], arr[dip]
                    break
            ans=self.reverse(arr[dip+1:n])
            k=0
            for i in range(dip+1, n):
                arr[i]=ans[k]
                k+=1
                
            