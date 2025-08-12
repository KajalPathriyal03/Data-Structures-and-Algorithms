
from typing import List

class Solution:
    
    
    class TrieNode:
        def __init__(self):
            self.left: 'Solution.TrieNode' = None  
            self.right: 'Solution.TrieNode' = None 

    def insert(self, head: TrieNode, num: int) -> None:
        p_crawl = head
        for i in range(31, -1, -1):
            ith_bit = (num >> i) & 1
            if ith_bit == 0:
                if not p_crawl.left:
                    p_crawl.left = self.TrieNode()
                p_crawl = p_crawl.left
            else:  
                if not p_crawl.right:
                    p_crawl.right = self.TrieNode()
                p_crawl = p_crawl.right

    def max_xor(self, head: TrieNode, num: int) -> int:
        max_xor_val = 0
        p_crawl = head
        for i in range(31, -1, -1):
            ith_bit = (num >> i) & 1
            if ith_bit == 1:
                if p_crawl.left:
                    max_xor_val += (1 << i)  
                    p_crawl = p_crawl.left
                else:
                    p_crawl = p_crawl.right
            else:  # ith_bit == 0
                if p_crawl.right:
                    max_xor_val += (1 << i)  
                    p_crawl = p_crawl.right
                else:
                    p_crawl = p_crawl.left
        return max_xor_val

    def findMaximumXOR(self, nums: List[int]) -> int:
        
        root = self.TrieNode()
        for x in nums:
            self.insert(root, x)

        result = 0
        for x in nums:
            result = max(result, self.max_xor(root, x))
        
        return result
        