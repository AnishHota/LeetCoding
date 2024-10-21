class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        def backtrack(ind,seen):
            if ind == len(s):
                return 0
            
            max_len = 0
            for end in range(ind+1,len(s)+1):
                subs = s[ind:end]
                if subs not in seen:
                    seen.add(subs)
                    max_len = max(max_len,1+backtrack(end,seen))
                    seen.remove(subs)
            return max_len
        
        return backtrack(0,set())