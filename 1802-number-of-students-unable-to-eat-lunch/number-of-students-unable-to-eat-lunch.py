class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        stq = deque(students)
        sndq = deque(sandwiches)

        while stq:
            prev_len = len(stq)
            for i in range(len(stq)):
                if stq[0]==sndq[0]:
                    stq.popleft()
                    sndq.popleft()
                else:
                    stq.append(stq.popleft())
            if len(stq)==prev_len:
                return len(stq)
        
        return 0
        