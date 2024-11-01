class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = 0
        ans = s[0]
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                cnt+=1
                if cnt<2:
                    ans+=s[i]
            else:
                cnt = 0
                ans+=s[i]
        return ans

        