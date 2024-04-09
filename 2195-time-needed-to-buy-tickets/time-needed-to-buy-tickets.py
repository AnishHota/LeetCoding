class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
    
        ans = 0
        for i,x in enumerate(tickets):
            ans += min(x,tickets[k]-(i>k))
        
        return ans