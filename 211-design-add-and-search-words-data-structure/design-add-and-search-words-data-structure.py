class TrieNode:
    def __init__(self):
        self.child = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.dictionary = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.dictionary
        for w in word:
            if w not in node.child:
                node.child[w] = TrieNode()
            node = node.child[w]
        
        node.word=True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.word
            
            if word[index]=='.':
                for ch in node.child:
                    if dfs(node.child[ch],index+1):
                        return True
            
            if word[index] in node.child:
                return dfs(node.child[word[index]], index+1)
            
            return False
        return dfs(self.dictionary,0)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)