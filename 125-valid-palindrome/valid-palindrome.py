class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = len(s)-1
        i = 0
        while i<=j:
            while i<len(s) and not s[i].isalnum():
                i+=1
            while j>=0 and not s[j].isalnum():
                j-=1
            if i<=j and i<len(s) and j>=0:
                if str(s[i]).lower()!=str(s[j]).lower():
                    print(s[i],s[j])
                    return False
            j-=1
            i+=1
        
        return True
        