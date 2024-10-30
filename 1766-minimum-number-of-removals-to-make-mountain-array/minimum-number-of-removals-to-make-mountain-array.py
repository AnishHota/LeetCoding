class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        self.lis = [-1]*n
        self.lds = [-1]*n
        self.lis[0]=1
        self.lds[-1]=1

        def lisfn(i):
            if i==0:
                return 1
            
            if self.lis[i]!=-1:
                return self.lis[i]
            
            mx = 1
            for j in range(i):
                if nums[j]<nums[i]:
                    mx = max(mx,lisfn(j)+1)
            
            self.lis[i]=mx
        
        for i in range(n):
            lisfn(i)
        
        def ldsfn(i):
            if i==n-1:
                return 1
            
            if self.lds[i]!=-1:
                return self.lds[i]
            
            mx = 1
            for j in range(i+1,n):
                if nums[j]<nums[i]:
                    mx = max(mx,ldsfn(j)+1)
            self.lds[i] = mx
        
        for i in range(n-1,-1,-1):
            ldsfn(i)

        print(self.lis,self.lds)
        ans = n-1
        for i in range(n):
            if self.lis[i]!=1 and self.lds[i]!=1:
                ans = min(ans,n-self.lis[i]-self.lds[i]+1)

        return ans
            
        