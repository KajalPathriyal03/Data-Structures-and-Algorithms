class TrieNode:
    def __init__(self):
        self.links=[None for _ in range(26)]
        self.flag=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        node=self.root
        for i in range(len(word)):
            idx=ord(word[i])-ord('a')
            if node.links[idx]==None:
                node.links[idx]=TrieNode()
            node=node.links[idx]
        node.flag=True

    def dfs(self, node, ind):

        if node is None:          # extra safety check
            return False

        if ind == len(self.word):
            return node.flag

        if self.word[ind] == ".":
            for child in node.links:
                if child and self.dfs(child, ind + 1):
                    return True
            return False
        else:
            idx = ord(self.word[ind]) - ord('a')
            if node.links[idx] is None:
                return False

            return self.dfs(node.links[idx], ind + 1)

    def search(self, word: str) -> bool:
        self.word=word
        return self.dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)