class trieNode:
    def __init__(self):
        self.child = [None for _ in range(26)]
        self.word = False

class Trie:

    def __init__(self):
        self.root = trieNode()
        self.curr = self.root

    def insert(self, word: str) -> None:
        self.curr = self.root
        for x in word:
            if self.curr.child[ord(x)-ord('a')] is None:
                self.curr.child[ord(x)-ord('a')] = trieNode()
                
            self.curr = self.curr.child[ord(x)-ord('a')]

        self.curr.word = True
                

    def search(self, word: str) -> bool:
        self.curr = self.root
        for x in word:
            if self.curr.child[ord(x)-ord('a')] is None:
                print(ord(x)-ord('a'))
                return False
            else:
                self.curr = self.curr.child[ord(x)-ord('a')]
            
        return self.curr.word

    def startsWith(self, prefix: str) -> bool:
        self.curr = self.root
        for x in prefix:
            if self.curr.child[ord(x)-ord('a')] is None:
                return False
            else:
                self.curr = self.curr.child[ord(x)-ord('a')]       
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)