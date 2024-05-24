class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        letter_hash = Counter(letters)

        def isPossible(word,letter_hash):
            cnt_word = Counter(word)
            for x in cnt_word:
                if cnt_word[x]>letter_hash[x]:
                    return False
            return True

        def backtrack(ind):
            if ind==len(words):
                return 0
            
            res = backtrack(ind+1)
            if isPossible(words[ind],letter_hash):
                for x in words[ind]:
                    letter_hash[x]-=1
                scr=0
                for x in words[ind]:
                    scr += score[ord(x)-ord('a')]
                
                res = max(res, scr+backtrack(ind+1))
                for x in words[ind]:
                    letter_hash[x]+=1
            
            return res
            
        return backtrack(0)
        
                            