class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque([x for x in range(len(deck))])
        ans = [0 for x in range(len(deck))]
        sorted_deck = sorted(deck)
        i=0
        while queue:
            ind = queue.popleft()
            ans[ind] = sorted_deck[i]
            i+=1
            if queue:
                queue.append(queue.popleft())
        
        return ans