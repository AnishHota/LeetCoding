class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        if nums[0]<0:
            if nums[-1]>=0:
                for i in range(1,len(nums)):
                    if nums[i-1]<0 and nums[i]>=0:
                        a,b = i-1,i
                        break
                
                while a>=0 and b<len(nums):
                    if nums[a]*-1 < nums[b]:
                        ans.append(nums[a]**2)
                        a-=1
                    else:
                        ans.append(nums[b]**2)
                        b+=1
                
                while a>=0:
                    ans.append(nums[a]**2)
                    a-=1
                while b<len(nums):
                    ans.append(nums[b]**2)
                    b+=1
                return ans
            else:
                return [a**2 for a in nums][::-1]
        else:
            return [a**2 for a in nums]
