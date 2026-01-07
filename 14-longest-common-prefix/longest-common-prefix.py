class TrieNode:
    def __init__(self):
        self.links=[None for _ in range(26)]
        self.cnt_end_with=0
        self.cnt_pre=0
        
class Trie:
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self, word):
        node=self.root
        for ele in word:
            ind=ord(ele)-ord('a')
            if node.links[ind]==None:
                node.links[ind]=TrieNode()
            node=node.links[ind]
            node.cnt_pre+=1
            
        node.cnt_end_with+=1
        
    def cnt_words_equal_to(self, word):
        node=self.root
        for ele in word:
            ind=ord(ele)-ord('a')
            if node.links[ind]==None:
                return 0 
            node=node.links[ind]
        return node.cnt_end_with
    
    def cnt_words_start_with(self, word):
        node=self.root
        for ele in word:
            ind=ord(ele)-ord('a')
            if node.links[ind]==None:
                return 0 
            node=node.links[ind]
        return node.cnt_pre
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie=Trie()
        for ele in strs:
            trie.insert(ele)
        res=""
        for i in range(len(strs[0])):
            ele=strs[0][:i+1]
            if trie.cnt_words_start_with(ele)==len(strs):
                res=ele
        return res

        