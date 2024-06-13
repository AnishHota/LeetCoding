class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)

        ans = 0
        for x,y in zip(seats,students):
            ans += abs(x-y)
        
        return ans