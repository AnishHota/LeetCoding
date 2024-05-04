class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        boats = 0
        i,j = 0, len(people)-1
        while people[j]>=limit:
            boats+=1
            j-=1
        while i<=j:
            if people[j] < limit and (people[i]+people[j]) <= limit:
                i+=1
            boats+=1
            j-=1
        
        return boats

        