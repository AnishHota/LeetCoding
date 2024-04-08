class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        cnt = Counter(students)

        for s in sandwiches:
            if cnt[s]>0:
                cnt[s]-=1
            else:
                return cnt[0]+cnt[1]
        
        return 0

        
        # stq = deque(students)
        # sndq = deque(sandwiches)

        # while stq:
        #     prev_len = len(stq)
        #     for i in range(len(stq)):
        #         if stq[0]==sndq[0]:
        #             stq.popleft()
        #             sndq.popleft()
        #         else:
        #             stq.append(stq.popleft())
        #     if len(stq)==prev_len:
        #         return len(stq)
        
        # return 0
        