class Solution:
    def suggestedProducts(self, products: List[str], word: str) -> List[List[str]]:
        products.sort()
        ans = []
        pre=""

        for i in range(len(word)):
            pre+=word[i]
            cur=[]
            for ele in products:
                
                if ele.startswith(pre):
                    cur.append(ele)
                if len(cur)==3:
                        break
            ans.append(cur.copy())

        return ans 


        