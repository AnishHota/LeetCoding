class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        window = deque()
        extra = 0
        max_extra = 0
        start,end = 0,0
        for i,x in enumerate(zip(customers, grumpy)):
            if len(window)<minutes:
                window.append(x[0])
                if x[1]==1:
                    extra += x[0]
                    if extra>max_extra:
                        max_extra = extra
                        start = 0
                        end = i
            else:
                window.popleft()
                if grumpy[i-minutes]==1:
                    extra -= customers[i-minutes]
                window.append(x[0])
                if x[1]==1:
                    extra += x[0]
                    if extra>max_extra:
                        max_extra = extra
                        start = i-minutes+1
                        end = i
        
        for i in range(start,end+1):
            grumpy[i]=0

        ans = 0
        for x,y in zip(customers, grumpy):
            if y==0:
                ans += x
        
        return ans
