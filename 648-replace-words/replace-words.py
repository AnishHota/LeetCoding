class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(" ")

        for x,word in enumerate(words):
            shortest_root = float("inf")
            shortest_ind = None
            for i,root in enumerate(dictionary):
                if word.startswith(root):
                    if len(root)<shortest_root:
                        shortest_root=len(root)
                        shortest_ind = i
            if shortest_ind is not None:
                words[x]=dictionary[shortest_ind]
        
        return " ".join(words)
                

