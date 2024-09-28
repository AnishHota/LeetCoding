class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        great = max(candies)
        for x in candies:
            if x+extraCandies>=great:
                res.append(True)
            else:
                res.append(False)
        return res