from sortedcontainers import SortedList
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        def can_form_word(word, letter_cnt):
            word_cnt=Counter(word)
            for ch in word:
                if word_cnt[ch]>letter_cnt[ch]:
                    return False
            return True
        
        def get_score(word):
            ans=0
            for ch in word:
                ind=ord(ch)-ord('a')
                ans+=score[ind]
            return ans 

        self.letter_cnt=Counter(letters)
        n=len(words)
        def backtrack(i):
            if i>=n:
                return 0
            res=backtrack(i+1)
            if can_form_word(words[i], self.letter_cnt):
                for ch in words[i]:
                    self.letter_cnt[ch]-=1
                res=max(res, get_score(words[i])+backtrack(i+1))
                for ch in words[i]:
                    self.letter_cnt[ch]+=1
            return res
        
        return backtrack(0)





        