class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if m*k>len(bloomDay):
            return -1
        def process(days):
            curr_len = 0
            val = 0
            for i in range(len(bloomDay)):
                if bloomDay[i]<=days:
                    curr_len +=1
                else:
                    curr_len = 0
                if curr_len==k:
                    val += 1
                    curr_len = 0
                # print(bloomDay[i],days,k,curr_len,val)
            return val
        # print(bloomDay,m,k)
        l,r = min(bloomDay), max(bloomDay)
        ans = max(bloomDay)+1
        while l<=r:
            mid = int((r+l)/2)
            # print(mid)
            val = process(mid)
            # print(mid,val)
            if val>=m:
                ans = min(mid, ans)
                r = mid-1
            elif val<m:
                l = mid+1
        
        return ans

            
