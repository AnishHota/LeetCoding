class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        chef = 0
        wait = 0
        for arr, time in customers:
            wait += max(time, chef+time-arr)
            chef = max(arr+time,chef+time)

        return round(float(wait/len(customers)),5)