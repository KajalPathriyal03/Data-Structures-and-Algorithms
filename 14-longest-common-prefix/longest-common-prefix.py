class Node:
    def __init__(self):
        self.links=[None] *26
        self.cnt_end_with=0
        self.cnt_prefix=0


class Trie:
    def __init__(self):
        self.root=Node()

    def insert(self, word):
        cur=self.root
        for ch in word:
            idx=ord(ch)-ord('a')
            if cur.links[idx]==None:
                cur.links[idx]=Node()
            cur=cur.links[idx]
            cur.cnt_prefix+=1
        cur.cnt_end_with+=1
        
    def cnt_words_equal_to(self, prefix):
        cur=self.root
        for ch in word:
            idx=ord(ch)-ord('a')
            if cur.links[idx]==None:
                return 0
            cur=cur.links[idx]
        return cur.cnt_end_with

    def cnt_words_start_with(self, word):
        cur=self.root
        for ch in word:
            idx=ord(ch)-ord('a')
            if cur.links[idx]==None:
                return 0
            cur=cur.links[idx]
        return cur.cnt_prefix

    def erase(self, word):
        cur=self.root
        for ch in word:
            idx=ord(ch)-ord('a')
            if cur.links[idx]==None:
                return 
            else:
                cur=cur.links[idx]
                cur.cnt_prefix-=1
        cur.cnt_end_with-=1


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        tree=Trie()
        for ele in strs:
            tree.insert(ele)
        res=""
        for i in range(len(strs[0])):
            ele=strs[0][:i+1]
            print(ele, )
            if tree.cnt_words_start_with(ele)==len(strs):
                res=ele 

        return res
        