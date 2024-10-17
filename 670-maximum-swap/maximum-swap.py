class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = list(str(num))
        cnt = Counter(arr)
        cnt = dict(sorted(cnt.items(),key=lambda x: x[0],reverse=True))
        p = 0
        for k,v in cnt.items():
            if k!=arr[p]:
                for i in range(len(arr)-1,-1,-1):
                    if arr[i]==k:
                        arr[i],arr[p] = arr[p],arr[i]
                        return int(''.join(arr))
                
            while k==arr[p]:
                p+=1
                cnt[k]-=1
                if cnt[k]==0:
                    break
            
            if cnt[k]!=0:
                for i in range(len(arr)-1,-1,-1):
                    if arr[i]==k:
                        arr[i],arr[p] = arr[p],arr[i]
                        return int(''.join(arr))
            
        return int(''.join(arr))
            
