class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        work = sorted(zip(difficulty,profit))
        worker.sort()
        profit = 0
        j = 0
        curr_prof = 0
        n = len(work)
        for x in worker:
            while j<n and work[j][0]<=x:
                curr_prof = max(curr_prof,work[j][1])
                j+=1
            profit += curr_prof
        
        return profit