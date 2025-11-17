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
    def prefixCount(self, words: List[str], pref: str) -> int:
        tree=Trie()
        for ele in words:
            tree.insert(ele)
        
        ans=tree.cnt_words_start_with(pref)
        return ans 
        

        