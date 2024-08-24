class Solution:
    def nearestPalindromic(self, n: str) -> str:
        number = int(n)
        if number<=10:
            return str(number-1)
        if number==11:
            return "9"

        def palindrome(leftHalf,isEven):
            if isEven==0:
                return int(str(leftHalf)+str(leftHalf)[::-1])
            if isEven==1:
                return int(str(leftHalf)+str(leftHalf)[::-1][1:])

        length = len(n)
        leftHalf = int(n[:(length+1)//2])

        palCand = [
            palindrome(leftHalf+1,length%2),
            palindrome(leftHalf,length%2),
            palindrome(leftHalf-1,length%2),
            10**(length-1)-1,
            10**(length)+1
        ]

        minDiff = float("inf")
        ans = 0

        for p in palCand:
            if p==number:
                continue
            if abs(number-p)<minDiff or (abs(number-p)==minDiff and abs(number-p)<ans):
                minDiff = abs(number-p)
                ans = p
        
        return str(ans)
