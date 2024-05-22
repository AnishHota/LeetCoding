class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        self.ans = []    

        def isPalindrome(st):
            return st == st[::-1]

        def part(ind,curr):

            if ind==len(s):
                self.ans.append(curr[:])
                return
                
            for i in range(ind+1, len(s)+1):
                temp = s[ind:i]
                if isPalindrome(temp):
                    curr += [temp]
                    part(i,curr)
                    curr.pop()

        part(0,[])
        return self.ans