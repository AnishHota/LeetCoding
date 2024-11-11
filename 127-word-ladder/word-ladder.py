class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)

        if endWord not in wordset:
            return 0
        
        q = deque()
        q.append(beginWord)
        dist = 1

        while q:
            n = len(q)
            dist += 1
            for _ in range(n):
                word = q.popleft()
                for i in range(len(word)):
                    for j in range(26):
                        temp = word[:i]+chr(97+j)+word[i+1:]
                        if temp == endWord:
                            return dist
                        
                        if temp in wordset:
                            q.append(temp)
                            wordset.remove(temp)
        
        return 0

